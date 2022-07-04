import requests as req
from bs4 import BeautifulSoup as bs
import PySimpleGUI as psg


qString = ""
URL = "https://www.kimonoya-japan.net/"
nameArr = []

def getGoodNames():
	rs = req.get(URL)
	pCont = bs(rs.content, "html.parser")
	names = pCont.find_all("span", class_="goods_name")

	for name in names:
		nameArr.append([psg.Text(name.text)])

	return nameArr