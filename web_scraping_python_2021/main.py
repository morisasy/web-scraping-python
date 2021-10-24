from bs4 import BeautifulSoup

with open('home.html', 'r') as page:
	content = page.read()
	#print(content)
	#soup = BeautifulSoup(content, 'lxml')
	soup = BeautifulSoup(content, 'html.parser')
	#print(soup.prettify())

	#tags = soup.find('h5') # find first h5 tags
	#print(tags) 

	course_html_tags = soup.find_all('h5') # find all h5 tags and create a list 
	#for course  in course_html_tags:
		#print(course)

	course_cards = soup.find_all('div',class_='card')
	for course in course_cards:
		#print(course)
		course_name = course.h5.text
		course_price = course.a.text.split()[-1] # get the price

		#print(course_name)
		#print(course_price)
		print(f'{course_name} costs {course_price}')

