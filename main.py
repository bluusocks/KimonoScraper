import PySimpleGUI as psg

from Sites.kimonoyaJapan import *

names = getGoodNames()

ly = [[psg.Text('total found: ' + str(len(names)))],[names]]

psg.Window(title="results", layout=ly, margins=(200,200)).read()
