import requests
from bs4 import BeautifulSoup
from time import sleep

position = "CEO"
region = "Africa"


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36"
}

n_pages = 20
results = []
for page in range(1, n_pages):
    sleep(5)

    try:
        url_query = f"https://www.google.com/search?q=site:linkedin.com/in/+AND+{position}+AND+{region}&start={str((page - 1) * 10)}"
        data = requests.get(
            url_query,
            headers=header,
        )
        if data.status_code == 429:
            raise ConnectionRefusedError
    except Exception as e:
        print("Too many requests")
        break

    if data.status_code == 200:
        soup = BeautifulSoup(data.content, "html.parser")
        for div in soup.find_all("div", {"class": "g"}):
            anchors = div.find_all("a")
            if anchors:
                link = anchors[0]["href"]
                title = div.find("h3").text
                try:
                    description = div.find("div", {"data-sncf": "2"}).text
                except Exception as e:
                    description = "-"
                results.append(str(title) + ";" + str(link) + ";" + str(description))
                print(str(title) + ";" + str(link) + ";" + str(description))
    else:
        print(data.status_code)
        print(data.reason)
        break

print(results)
