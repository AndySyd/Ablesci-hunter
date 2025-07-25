import requests
import re

urls = []
for i in range(1,50):
    urls.append(f"https://www.ablesci.com/assist/index?status=waiting&publisher=elsevier&page=" + str(i))
    urls.append(f"https://www.ablesci.com/assist/index?status=waiting&publisher=springer&page=" + str(i))

def lets_hunt(url):
    # print(url)
    response = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"})
    response.raise_for_status()
    html_content = response.text
    li_pattern = re.compile(r'<li>(.*?)</li>', re.DOTALL)
    li_matches = li_pattern.findall(html_content)
    for li_content in li_matches:
        if '材料' not in li_content and '置顶' not in li_content and '求助中' in li_content and 'Book' not in li_content: #'2天前' not in li_content and
            points_match = re.findall(r'jifen"></i>(.*?)</span>', li_content)
            if 30 <= int(points_match[0]) <= 99999:
                print('  ')
                print('积分',int(points_match[0]))
                # print(url)
                # print(li_content)
                name = re.findall(r'<a data-clipboard-text="(.*?)" href', li_content)
                url1 = re.findall(r'<a target="_blank" title="查看详情" href="(.*?)"', li_content)[0]

                print(name[0])
                print(url1)

                response = requests.get(url1, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
                })
                response.raise_for_status()
                html_content = response.text
                pdf_url = re.findall(r'<a href="(.*?)" target="_blank" title="『', html_content)
                print(pdf_url)

                print('  ')

for i in urls:
    url = i
    lets_hunt(url)

