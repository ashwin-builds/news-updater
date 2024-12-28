from bs4 import BeautifulSoup
import requests

#WEBSITES
#WORLD NEWS: https://www.thehindu.com/news/international/
#INDIA NEWS: https://www.thehindu.com/news/national/

def get_th_titles(link):
    titles = []
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    h3 = soup.find_all("h3")
    for tag in h3:
        class_name = tag.get("class")
        if class_name:
            if("title" in class_name):
                titles.append(tag.text.replace("\n", "").strip())
    return titles

WORLD_NEWS_LINK = 'https://www.thehindu.com/news/international/'
INDIA_NEWS_LINK = 'https://www.thehindu.com/news/national/'

world_news_titles = get_th_titles(WORLD_NEWS_LINK)
india_news_titles = get_th_titles(INDIA_NEWS_LINK)

#outputting into terminal
print("-" * 20)
print('\n')
print("---WORLD NEWS---\n\n")
for title in world_news_titles:
    print(title + '\n')
print("\n\n\n---INDIA NEWS---\n\n\n")
for title in india_news_titles:
    print(title + "\n")
print("\n")
print("-" * 20)