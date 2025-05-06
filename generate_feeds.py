import csv
import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

os.makedirs("feeds", exist_ok=True)

with open("menu.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if not row["item"] or not row["price"]:
            continue  # skip empty lines

        rss = Element("rss", version="2.0")
        channel = SubElement(rss, "channel")
        title = SubElement(channel, "title")
        title.text = f"{row['item']} Price"

        item = SubElement(channel, "item")
        item_title = SubElement(item, "title")
        item_title.text = row["item"].capitalize()

        desc = SubElement(item, "description")
        desc.text = row["price"]

        xml_str = parseString(tostring(rss)).toprettyxml(indent="  ")
        with open(f"feeds/{row['item'].lower()}.xml", "w") as out:
            out.write(xml_str)
