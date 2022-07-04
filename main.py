import PySimpleGUI as psg

import Sites.kimonoyaJapan as kimJ

names = kimJ.getGoodNames()

ly = [[psg.Text('total found: ' + str(len(names)))],[names]]

psg.Window(title="results", layout=ly, margins=(200,200)).read()
