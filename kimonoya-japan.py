import requests as req
from bs4 import BeautifulSoup as bs

URL = "https://www.kimonoya-japan.net/"
rs = req.get(URL)
pCont = bs(rs.content, "html.parser")

results = pCont.find_all("div", class_="list_item_data")

for result in results:
	print(result.prettify())
