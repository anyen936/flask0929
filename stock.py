import requests
from bs4 import BeautifulSoup


def scrape_stocks():
    url = "https://histock.tw/%E5%9C%8B%E9%9A%9B%E8%82%A1%E5%B8%82"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    trs = soup.find(string="小日經").find_parent("div").find_all("tr")
    datas = []
    for tr in trs:
        data = []
        for th in tr.find_all("th"):
            print(th.text.strip(), end="\t")
        for td in tr.find_all("td"):
            print(td.text.strip(), end="\t")
            data.append(td.text.strip())
        datas.append(data)
        print()
    return datas


if __name__ == "_main_":
    print(scrape_stocks())
