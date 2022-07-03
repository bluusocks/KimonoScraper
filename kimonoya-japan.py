import requests as req
from bs4 import BeautifulSoup as bs
import PySimpleGUI as psg

URL = "https://www.kimonoya-japan.net/"
rs = req.get(URL)
pCont = bs(rs.content, "html.parser")

results = pCont.find_all("div", class_="list_item_data")

ly = [[]]

for result in results:
	print(result.prettify())

psg.Window(title="results", layout=ly, margins=(200,200)).read()