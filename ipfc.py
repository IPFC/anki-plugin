# should install this in Documents/Anki/addons folder
# upload to Addons page
# https://apps.ankiweb.net/docs/addons20.html
# https://github.com/dae/

#import backend, which includes data structures for cards and exporter
import anki
# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

from anki.hooks import addHook


def exportCards():
    #prompt login to IPFC

    #select deck of cards to export
    mw.col.decks


    showInfo("Exporting Cards complete.")
    
def onIPFC():
    #export card

    showInfo("Sent card to IPFC!")
    
def addMyButton(buttons, editor):
    editor._links['IPFC'] = onIPFC
    return buttons + [editor._addButton(
        "IPFC_icon.png", 
        "IPFC",
        "tooltip")]

action_1 = QAction("Export Cards to Inter Planetary Flash Cards", mw)
# set it to call importCards when it's clicked
action_1.triggered.connect(exportCards)
# and add it to the tools menu
mw.form.menuTools.addAction(action_1)

#make an option to immediately IPFC a card as soon as it's made?
addHook("setupEditorButtons", addMyButton)