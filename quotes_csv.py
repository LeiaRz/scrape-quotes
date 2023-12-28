import requests #library for making HTTP requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'http://quotes.toscrape.com'
url = base_url

quotes_data = [] #list to store the quotes

while url:
    response = requests.get(url)
    #print(response.status_code) #200 means that the request was successful

    soup = BeautifulSoup(response.text, 'html.parser') #creating a BeautifulSoup object
    quotes = soup.find_all('div', class_='quote') #finding all the elements that contain quotes

    for quote in quotes:
        text = quote.find('span', class_='text').get_text() #Extracting the text of the quote
        author = quote.find('small', class_='author').get_text() #Extracting author's name
        quotes_data.append({'Quote': text, 'Author': author})
   
    next_link = soup.find('li', class_='next')  #going to the next page
    if next_link and next_link.find('a') and next_link.find('a').get('href'):
        url = base_url + next_link.find('a')['href']
    else:
        url = None #no more next pages
df = pd.DataFrame(quotes_data)
q_path = 'C:/Users/Desktop/quotes.csv' #the path needs to be changed
df.to_csv(q_path, index=False)