import requests
from bs4 import BeautifulSoup


def scrap_content(pages, sections):
	content = []
	for section in sections:
		for page in range(1, pages+1):
			res = requests.get('https://www.quantamagazine.org/' + str(section) + '/page/' + str(page))
			soup = BeautifulSoup(res.text, 'html.parser') 
			content += soup.select('.card__content')
	return content_separation(content)


def content_separation(content):
	hn = []
	for index, item in enumerate(content):
		title = content[index].find('h2', class_='card__title').getText()
		author = content[index].find('span', class_='byline__author').getText()
		hrefs = content[index].find_all('a', href=True)
		link = hrefs[1].get('href', None)

		hn.append({
				"title": title,
				"author": author,
				"link": "https://www.quantamagazine.org" + link
				})
	return hn


def start_scraper(pages, sections):
	for i in scrap_content(pages, sections):
		print("Title: {title}\nLink: {link}\nAuthor: {author}\n"
				.format(title = i["title"], link = i["link"], author = i["author"]))