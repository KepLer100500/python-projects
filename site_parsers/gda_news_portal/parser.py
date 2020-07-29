from requests import get
from re import findall, sub
from pymysql import connect
from pymysql.cursors import DictCursor
from bs4 import BeautifulSoup


class question:
	def __init__(self, url):
		self.soup = self.get_soup(url)
		self.links = self.get_links(self.soup)
		self.numbers = self.get_numbers()
		self.users = self.get_users(self.soup)
		self.datetimes = self.get_datetimes(self.soup)
		self.texts = self.get_texts(self.soup)
		self.count_posts = len(self.numbers)
	
	def get_soup(self, url):
		# return object parser type
		r = get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		return soup
		
	def get_links(self, soup):
		# return list of links, format - http://aus017/AskMe/Search?SearchRequest=2341 
		links = soup.find('div', class_='container body-content').find_all('div', class_='col-md-12')
		links = ['http://aus017' + link.find('a').get('href') for link in links if link.find('a') != None]
		return links
		
	def get_numbers(self):
		# return id number of question
		return [int(findall(r'\=.+', number)[0][1:]) for number in self.links]
		
	def get_users(self, soup):
		# return list of users, who asked question
		users = soup.find('div', class_='container body-content').find_all('div', class_='col-md-12')
		users = [user.find('em').text.strip() for user in users if user.find('em') != None]
		return users

	def get_datetimes(self, soup):
		# return list of dates/times when asked question, format - 2018-04-09 15:45:47
		datetimes = soup.find('div', class_='container body-content').find_all('div', class_='col-md-2')
		datetimes = [datetime.text.strip() for datetime in datetimes if datetime.find('span', class_='glyphicon glyphicon-calendar') != None]
		datetimes = [sub('(\d{2}).(\d{2}).(\d{4})(\s.+)', '\g<3>-\g<2>-\g<1>\g<4>', datetime) for datetime in datetimes]
		return datetimes

	def get_texts(self, soup):
		# return list of bodys questions 
		texts = soup.find('div', class_='container body-content').find_all('div', class_='col-md-12')
		texts = [text.find('p').text.strip() for text in texts if text.find('p') != None]
		return texts


class database:
	def __init__(self):
		self.connection = connect(host='1.1.1.1',
		                          user='user',
								  password='user',
								  db='test',
								  charset='utf8',
								  cursorclass=DictCursor)

	def already_in_database(self, number_q):
		# check, question already is in database? return 0 if post not in database
		try:
			with self.connection.cursor() as cursor:
				sql = "select count(*) from appeal_portal where number_q = " + str(number_q)
				cursor.execute(sql)
			rows = cursor.fetchall()
		finally:
			return int(rows[0]['count(*)'])

	def insert_new_question(self, number_q, datetime_q, user_q, link_q, text_q):
		# insert into database new question
		try:
			with self.connection.cursor() as cursor:
				sql = "insert into appeal_portal values(0, " + str(number_q) + ", '" + datetime_q + "', '" + user_q + "', '" + link_q + "', '" + text_q + "')"
				cursor.execute(sql)
			self.connection.commit()
		finally:
			return 1

	def close_connection(self):
		# correctly close connection
		self.connection.close()


def main():
	db = database()
	url = 'http://aus017/AskMe/Question/Show/dfdf5c6a-7513-4bec-b668-d56af530b42d'
	q = question(url)
	for post in range(q.count_posts):
		if not db.already_in_database(q.numbers[post]):
			db.insert_new_question(q.numbers[post], q.datetimes[post], q.users[post], q.links[post], q.texts[post])
	db.close_connection()
	
if __name__ == '__main__':
	main()