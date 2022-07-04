import requests as req
from bs4 import BeautifulSoup as bs
import PySimpleGUI as psg

URL = "https://www.kimonoya-japan.net/"
rs = req.get(URL)
pCont = bs(rs.content, "html.parser")

names = pCont.find_all("span", class_="goods_name")

nameArr = []

for name in names:
	nameArr.append([psg.Text(name.text)])

print(nameArr)

ly = [[psg.Text('total found: ' + str(len(nameArr)))],[nameArr]]

psg.Window(title="results", layout=ly, margins=(200,200)).read()