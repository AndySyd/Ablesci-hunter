import requests
import re
import os
from urllib.parse import quote

urls = []
for i in range(1,100):
    urls.append(f"https://www.ablesci.com/assist/index?status=waiting&publisher=elsevier&page=" + str(i))
    urls.append(f"https://www.ablesci.com/assist/index?status=waiting&publisher=springer&page=" + str(i))

def lets_hunt(url):
    # print(url)
    response = requests.get(url, headers={"User-Agent": "Your edge head"})
    response.raise_for_status()
    html_content = response.text
    li_pattern = re.compile(r'<li>(.*?)</li>', re.DOTALL)
    li_matches = li_pattern.findall(html_content)
    for li_content in li_matches:
        if '天前' not in li_content and '材料' not in li_content and '置顶' not in li_content and '求助中' in li_content and 'Book' not in li_content:
            points_match = re.findall(r'jifen"></i>(.*?)</span>', li_content)
            if 29 <= int(points_match[0]) <= 99999:
                print(url)
                print('积分',int(points_match[0]))
                name = re.findall(r'<a data-clipboard-text="(.*?)" href', li_content)
                os.system(f'echo {name[0]}| clip')
                if 'Elsevier' in li_content:
                    print(name[0])
                    print(str('https://www.sciencedirect.com/search?qs='+quote(name[0])))
                if 'Springer' in li_content:
                    print(name[0])
                    print(str('https://link.springer.com/search?query='+quote(name[0])))
                print('====================================================================')

for i in urls:
    url = i
    lets_hunt(url)

