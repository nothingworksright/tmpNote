# ----------------------------------------------------------------------
# This file was generated by img2py.py
# python img2py.py -i path/to/your/icon.ico myIcon.py

from wx.lib.embeddedimage import PyEmbeddedImage

catalog = {}
index = []

tmpNoteIcon = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAN5J"
    "REFUWIXtl8ttRCEMRQ/pZZpwQaxTCts0QglTQZRFPL3cLBg/wXw0b5HR29grY8zlGCMkCiAO"
    "tI8jN0+ABEiABEiABEiABEiABEiAFcAa8rZ7oSR6Dd8f5riE7dGids1G7fJp3Ix1Hm58X2LG"
    "mh95m2avYnyIxOZYk7wpgHodIliTN9uE+wTUXKpXgIhD3YD8uib2mOEj9vQO/H7fx87ACfg5"
    "j/HnqfClvT87Ay4AlFJuWjARRguiyvkEpFHxXMXonk9H3PVQEwS2aAAq0YdXJumO/D9sN8C7"
    "7PB34A9CYBEFFqJdwwAAAABJRU5ErkJggg==")
gettmpNoteIconData = tmpNoteIcon.GetData
gettmpNoteIconImage = tmpNoteIcon.GetImage
gettmpNoteIconBitmap = tmpNoteIcon.GetBitmap
gettmpNoteIconIcon = tmpNoteIcon.GetIcon
