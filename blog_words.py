from lxml import html
import requests


def words(body):
    return sum([len(p.split()) for p in body])


# first_entry = requests.get("https://grrm.livejournal.com/850.html")
first_entry = requests.get("https://grrm.livejournal.com/169018.html")
tree = html.fromstring(first_entry.content)

date = tree.xpath('//ul[@class=\'asset-meta-list clearfix\']/li/span/abbr/text()')
text = tree.xpath('//*[@class=\'asset-body \']/text()')
next_entry = tree.xpath('//a[text()=\'Next Entry\']/@href')

ds = date
ws = [words(text)]

while next_entry:
    raw = requests.get(next_entry[0])
    tree = html.fromstring(raw.content)
    date = tree.xpath('//ul[@class=\'asset-meta-list clearfix\']/li/span/abbr/text()')
    if not date:
        break
    if len(date[0]) < 9:
        title = tree.xpath('//h2[@class=\'asset-name page-header2\']/a/text()')
        date[0] = title[0] + "at " + date[0]
    print(date)
    ds.extend(date)
    ws.append(words(tree.xpath('//*[@class=\'asset-body \']/text()')))
    next_entry = tree.xpath('//a[text()=\'Next Entry\']/@href')

with open("blog_data.tsv", "a") as file:
    for d, wc in zip(ds, ws):
        file.write(d + "\t" + str(wc)+'\n')
