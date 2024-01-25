from urllib.request import urlopen
import xml.etree.ElementTree as ET
with urlopen('https://careers.boozallen.com/jobs/search/?1487=%5B3581%5D&1487_format=1019&2111=%5B9148446%5D&2111_format=1307&listFilterMode=1&jobRecordsPerPage=20&jobOffset=120') as a:
    tree = ET.parse(a)
notags = ET.tostring(tree.getroot(), encoding='utf-8',method='text')

a = open('test.txt','w')
a.write(notags)
a.close()

ET.parse()