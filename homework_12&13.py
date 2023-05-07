import csv
import time
import requests
from bs4 import BeautifulSoup
for i in range(1, 3):
      page = i
      url = f"https://books.toscrape.com/catalogue/page-{page}.html"
      r = requests.get(url)
      print(r.status_code)
      content = r.text
      soup = BeautifulSoup(content,'html.parser')
      body = soup.find("body")
      wrapper = body.find("div",{'class':'container-fluid page'})
      pg_inner = wrapper.find('div',{'class':'page_inner'})
      row_1 = pg_inner.find('div',{'class':'row'})
      column = row_1.find('div',{'class':'col-sm-8 col-md-9'})
      section = column.find("section")
      div = section.find("div")
      row_2 = section.find("ol")
      col = section.find("li")
      article=col.find("article")
      all_books = section.find_all('li')

      with open('books.csv','w',encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['title','price'])


      for container in all_books:
            book_title = container.find('h3')
            book_price = container.find('div',{'class':'product_price'})
            title = book_title.a.text
            price = book_price.p.text
            print(title, price)
            time.sleep(1)

# file = open('books.csv','w',encoding='utf-8')
# file.write()
