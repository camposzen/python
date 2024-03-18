import bs4
# import lxml

with open(file="website.html") as file:
    contents = file.read()

soup = bs4.BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.p)
# print(soup.a)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
print([a.get("href") for a in all_anchor_tags])

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select(selector="p a")
print(company_url.pop().get("href"))

all_tags_with_class = soup.select(".heading")
print(all_tags_with_class)
