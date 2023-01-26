from bs4 import BeautifulSoup
import requests
# with open("website.html",encoding="utf8") as file:
#     contents = file.read()


# print(soup.title)
# print(soup.title.name)
# print(soup.prettify())
# print(soup.p)

# all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)
#
# for tag in all_anchor_tag:
#     # print(tag.getText())
#     print(tag.get("href"))# it is used for attributes

# heading = soup.find_all(name="h1",id = "name")
# print(heading)
#
# section_heading = soup.find(name="h3",class_ = "heading")
# print(section_heading.getText)
# print(section_heading.name)
#
# company_url =  soup.select_one(selector="p a") # getting anchor tag
# print(company_url)
# company_url =  soup.select_one(selector="#name")# id use #
# print(company_url)
#
# headings = soup.select(selector=".heading") # class use .
# print(headings)


# article_data = soup.select(selector=".titleline>a")
# for tag in article_data[:30]:
#     print(tag.getText())
# # article_upvote = soup.select(selector="#score_34424854")
# # for id_ in article_upvote:
# #     print(id_.getText())
#
# article_upvote = soup.find(name="span",class_="score").getText()
# print(article_upvote)


response =  requests.get(url="https://news.ycombinator.com/")
website_data = response.text
soup = BeautifulSoup(website_data,"html.parser")
#-----------------for first class --------------------
# articles_tag= soup.find(name="span", class_="titleline")
# print(articles_tag.getText())
# articles_link = articles.get("href")
# print(articles_link)
# article_upvote = soup.find(name="span",class_="score").getText()
# print(article_upvote)


#-----------------for multiple------------------
articles_list = []
articles_link = []
up_list_number = []
# Selecting and adding to articles list
articles_tag= soup.find_all(name="span", class_="titleline")
for tag in articles_tag:
    articles_list.append(tag.getText())

# Selecting and adding to articles link
links= soup.select(selector=".titleline>a")
for link in links:
    articles_link.append(link.get("href"))


# selecting upvoting
upvote_lists = [int(point.getText().split()[0]) for point in soup.find_all(name="span", class_="score")]

print(articles_list)
print(articles_link)
print(upvote_lists)

# finding the highest index
largest_number = max(upvote_lists)
largest_index = upvote_lists.index(largest_number)

print(articles_list[largest_index])
print(articles_link[largest_index])
# new_sorting = sorted(upvote_lists,reverse=True)
# print(new_sorting)