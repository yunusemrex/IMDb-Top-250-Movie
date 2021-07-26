from bs4 import BeautifulSoup
import requests

source = "https://www.imdb.com/chart/top/"

html = requests.get(source).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr",limit=250)


def Web_Scraping():
    count = 0
    for tr in list:
        title = tr.find("td", {"class":"titleColumn"}).find("a").text
        year = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
        rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
        count += 1

        print(f"Rank:{count} - Movie: {title} - Year: {year} - IMBD Rating: {rating}") 

if __name__== "__main__":
    Web_Scraping()