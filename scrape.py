import requests
from bs4 import BeautifulSoup


def scrape_pm25():
    url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"
    try:
        datas = requests.get(url).json()["records"]
        columns = list(datas[0].keys())
        values = [list(data.values()) for data in datas]

        return columns, values
    except Exception as alert:
        return alert
    return None, 404


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
    # print(scrape_stocks())
    print(scrape_pm25())
