import xml.etree.ElementTree as ET


def extract_title_and_desc(svg_content: str):
  root = ET.fromstring(svg_content)
  try:
    title_element = root.find(".//{http://www.w3.org/2000/svg}title")
    title_text = title_element.text.strip() if title_element is not None else None
  except:
    title_text="none"
  try:
    desc_element = root.find(".//{http://www.w3.org/2000/svg}desc")
    desc_text = desc_element.text.strip() if desc_element is not None else None
  except:
    desc_text="none"

  return title_text, desc_text
