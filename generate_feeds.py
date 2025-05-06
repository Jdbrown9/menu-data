import csv
import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

# Make sure feeds folder exists
os.makedirs("feeds", exist_ok=True)

with open("menu.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        item = row.get("item", "").strip().lower()
        price = row.get("price", "").strip()
        if not item or not price:
            continue  # Skip empty rows

        rss = Element("rss", version="2.0")
        channel = SubElement(rss, "channel")
        title = SubElement(channel, "title")
        title.text = f"{item.capitalize()} Price"

        xml_item = SubElement(channel, "item")
        item_title = SubElement(xml_item, "title")
        item_title.text = item.capitalize()

        desc = SubElement(xml_item, "description")
        desc.text = price

        xml_str = parseString(tostring(rss)).toprettyxml(indent="  ")
        with open(f"feeds/{item}.xml", "w") as out:
            out.write(xml_str)
