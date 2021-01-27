import sys
from time import strftime
from PyQt5.QtCore import QSize, Qt
from pysnmp.hlapi import SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, nextCmd
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QDesktopWidget, QPushButton
from PyQt5.QtGui import QColor, QIcon


class SNMP:
    def __init__(self):
        '''
        Define snmp settings
        '''
        self.password = 'public'
        self.oid = '1.3.6.1.4.1.248.14.5.1.1.7'
        with open('id_ip.txt', 'r') as file:
            self.hosts = {line.split('=')[0].strip(): line.split('=')[1].strip() for line in file}


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        Create user interface
        '''
        self.setWindowTitle('Hyper Rings')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setGeometry(500, 400, 350, 400)
        self.setMinimumSize(QSize(333, 500))        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid = QGridLayout()
        central_widget.setLayout(grid)
        table = QTableWidget(self)
        btn = QPushButton('Request', self)
        btn.clicked.connect(lambda: self.fill_table(table))
        grid.addWidget(table, 0, 0)
        grid.addWidget(btn, 1, 0)
        self.center()
        self.show()

    def fill_table(self, table):
        '''
        Insert received data into table
        '''
        snmp = SNMP()
        data = get_data(snmp)
        table.clear()
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(['Time', 'Name', 'IP', 'Status'])
        table.setRowCount(len(data))
        for i, rows in enumerate(data):
            for j, val in enumerate(rows):
                table.setItem(i, j, QTableWidgetItem(val))
                color = QColor(255, 255, 255)
                if j == len(rows) - 1:
                    if val == '3':
                        val = 'ON'
                        color = QColor(0, 125, 0)
                    else:
                        val = 'OFF'
                        color = QColor(125, 0, 0)
                table.setItem(i, j, QTableWidgetItem(val))
                table.item(i, j).setBackground(color)
        table.resizeColumnsToContents()

    def center(self):
        '''
        Put created window into center display
        '''
        window = self.frameGeometry() 
        monitor = QDesktopWidget().availableGeometry().center()
        window.moveCenter(monitor) 
        self.move(window.topLeft())


def get_data(snmp):
    '''
    Get states ring manager of all RS's
    '''
    link_states = []
    for rs_name in snmp.hosts:
        ip = snmp.hosts[rs_name]
        for (_, _, _, values) in nextCmd(SnmpEngine(),
                                            CommunityData(snmp.password),
                                            UdpTransportTarget((ip, 161)),
                                            ContextData(),
                                            ObjectType(ObjectIdentity(snmp.oid)),
                                            lookupMib=False,
                                            lexicographicMode=False):
            resolve = [value[1] for value in values][0]
            link_states.append([strftime('%Y-%m-%d %H:%M:%S'), rs_name, ip, str(resolve).strip()])
    return link_states

def main():
    app = QApplication(sys.argv)
    mf = MainForm()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()