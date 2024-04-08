from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

div_tags = soup.findAll(name="div", class_="jsx-3523802742 listicle-item")
count = 100
for tag in div_tags:
    movie_name = tag.find(name="img", class_="jsx-2590794431 loading").get("alt")
    print(f"{count}. {movie_name}")
    count -= 1







