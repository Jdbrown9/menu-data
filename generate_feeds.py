import csv
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import os

os.makedirs("feeds", exist_ok=True)

with open("menu.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rss = Element('rss', version="2.0")
        channel = SubElement(rss, 'channel')
        title = SubElement(channel, 'title')
        title.text = f"{row['item']} Price"

        item = SubElement(channel, 'item')
        item_title = SubElement(item, 'title')
        item_title.text = row["item"].capitalize()

        desc = SubElement(item, 'description')
        desc.text = row["price"]

        xml_pretty = parseString(tostring(rss)).toprettyxml(indent="  ")
        with open(f"feeds/{row['item'].lower()}.xml", "w") as out:
            out.write(xml_pretty)
