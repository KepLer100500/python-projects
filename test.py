from tkinter import *

def move(event):
    x = root.winfo_pointerx() - root.winfo_rootx()
    y = root.winfo_pointery() - root.winfo_rooty()
    test = str(x) + " " + str(y)
    #test = root.winfo_pointerxy()
    l['text'] = test


# 1625 / 991
root = Tk()
l = Label(bg='white', fg='black', width=50)
l.pack()
root.bind('<Motion>', move)
root.mainloop()




#btn = Button(root, text="Click me", width=30,height=5, bg="white",fg="black")
#btn.bind("<Button-1>", Hello)
#btn.pack()

#Button(root, text = '1').pack(side = 'left')
