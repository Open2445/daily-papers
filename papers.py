import urllib, xml.etree.ElementTree as ET, requests, os

TOKEN = os.environ["TG_TOKEN"]
CHAT = os.environ["TG_CHAT"]

url = "http://export.arxiv.org/api/query?search_query=cat:cs.CR&sortBy=submittedDate&max_results=10"
data = urllib.request.urlopen(url).read()
root = ET.fromstring(data)
ns = {"a": "http://www.w3.org/2005/Atom"}
entries = root.findall("a:entry", ns)

paper = entries[0]
title = paper.find("a:title", ns).text.strip()
link = paper.find("a:id", ns).text
abstract = paper.find("a:", ns).text.strip()[:400]

msg = f"📄 *Today's Cybersecurity Paper*\n\n*{title}*\n\n{abstract}...\n\n{link}"
requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
              data={"chat_id": CHAT, "text": msg, "parse_mode": "Markdown"})
