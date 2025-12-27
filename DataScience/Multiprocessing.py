import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup

urls=["http://en.wikipedia.org/wiki/Python_(programming_language)", "http://en.wikipedia.org/wiki/Web_scraping"]

def scrape(url):
	try:
		headers = {'User-Agent': 'Mozilla/5.0'}
		response = requests.get(url, headers=headers, timeout=5)
		soup = BeautifulSoup(response.text,'html.parser')
		title=soup.find('title').text
		return title
	except Exception as e:
		return f"Error: {str(e)}"
	
if __name__=="__main__":
	with Pool(processes=4) as pool:
		results=pool.map(scrape,urls)
	
	for url, title in zip(urls, results):
		print(f"title of {url} is {title}")
	
	