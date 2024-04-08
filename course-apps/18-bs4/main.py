from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
# print(response)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
print(soup.title)
# print([(t.getText(), t.findNext(name="a").get("href")) for t in soup.find_all(class_="titleline")])
# print([s.getText() for s in soup.find_all(name="span", class_="score")])
all_articles = [(t.getText(), t.findNext(name="a").get("href")) for t in soup.find_all(class_="titleline")]
all_scores = [int(s.getText().split()[0]) for s in soup.find_all(name="span", class_="score")]
i = all_scores.index(max(all_scores))
print(all_scores[i], all_articles[i])

