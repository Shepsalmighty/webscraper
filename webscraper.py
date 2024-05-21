#!/home/sheps/webscraper/.venv/bin/python
import sys
import requests
import webbrowser
from bs4 import BeautifulSoup


url = "https://www.gamespot.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

site_elements = soup.select('.js-click-tag.card-item__link.text-decoration--none')


# top 3 function grabs the first 3 articles (in our case the most popular therefore top)
def top3():
    site = []
    # without zip, the code would fail/error out if we had less than 3 articles
    for _, element in zip(range(3), site_elements):
        # print(site_elements[num].text)
        # print(url + site_elements[num].attrs["href"] + "")
        update = url + element.attrs["href"] + ""
        site.append(update)

    return site

print(type(top3))
top3()



# if __name__ == "__main__":
#     main()


