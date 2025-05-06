import csv
import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

print("Starting RSS feed generation...")

# Ensure feeds directory exists
os.makedirs("feeds", exist_ok=True)

with open("menu.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        item = row.get("item", "").strip().lower()
        price = row.get("price", "").strip()

        if not item or not price:
            print(f"Skipping invalid row: {row}")
            continue

        print(f"Generating RSS for: {item} (${price})")

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
        path = f"feeds/{item}.xml"
        with open(path, "w") as out:
            out.write(xml_str)

print("RSS generation complete.")
