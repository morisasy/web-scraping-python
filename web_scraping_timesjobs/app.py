from bs4 import BeautifulSoup

import requests

import time

print("Put some skill that you are not familiar with:")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
	html_page = "http://www.timesjobs.com/candidate/jobs-search-result.html?txtKeywords=python&txtLocation=&cboWorkExp1=-1"
	page = requests.get(html_page)

	#print(page.text)
	#soup = BeautifulSoup(page, 'html.parser')
	soup = BeautifulSoup(page, 'lxml')
	jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
	#jobS = soup.find("li", class_="clearfix job-bx wht-shd-bx")
	#print(jobs)
	for index, job in enumerate(jobs):
		published_date = job.find('span', class_="sim-posted").span.text
		#print(published_date)
		
		if 'few' in published_date:
			company_name = job.find('h3',class_="joblist-comp_name").text.replace('','')
			skills = job.find('span', class_="srp-skills").text.replace(' ','')
			more_info = job.header.h2.a['href']
			#print(company_name)
			#print(skills)
			if unfamiliar_skill not in skills:
				with open(f'posts/{index}.txt', 'w') as f:

					f.write(f'Company Name: {company_name.strip()} \n')
					f.write(f'Required Skills: {skills.strip()} \n')
					f.write(f'More Info: {more_info}')
					#print(f'Company Name: {company_name.strip()}')
					#print(f'Required Skills: {skills.strip()}')
					#print(f'More Info: {more_info}')
				print(f"File saved")
					
			

if __name__ == '__main__':

	while True:

		find_jobs()

		time_wait = 10
		print(f'waiting {time_wait} minutes....')
		time.sleep(time_wait * 60) # run after every 10m

