import requests

URL_ZILLOW = ''.join([
    'https://www.zillow.com/search/GetSearchPageState.htm?',
    'searchQueryState={"pagination":{},"mapBounds":',
    '{"north":45.934765171573396,"east":-121.17736409101153,"south":44.92673760314442,"west":-123.65752766523028},'
    '"usersSearchTerm":"Portland OR","regionSelection":[{"regionId":13373,"regionType":6}],"isMapVisible":true,',
    '"filterState":{"price":{"max":268848,"min":192034},"beds":{"min":1},"isForSaleForeclosure":{"value":false},',
    '"monthlyPayment":{"max":1400,"min":1000},"isAuction":{"value":false},"isNewConstruction":{"value":false},'
    '"isForRent":{"value":true},"isForSaleByOwner":{"value":false},"isComingSoon":{"value":false},',
    '"isForSaleByAgent":{"value":false}},"isListVisible":true,"mapZoom":9}',
    '&wants={"cat1":["listResults","mapResults"]}&requestId=11'
])

cookies = {
    "_pxvid": "0f03dacd-36d0-11ee-bfd1-cc7a1b999b67",
}

headers = {
    "User-Agent": ''.join([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    ]),
    "Accept": ''.join([
        "text/html,application/xhtml+xml,application/xml;",
        "q=0.9,image/avif,image/webp,image/apng,*/*;",
        "q=0.8,application/signed-exchange;v=b3;q=0.7"
    ]),
    "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "sec-ch-ua-platform": "Windows",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
}


class Zillow:
    def __init__(self):
        print(URL_ZILLOW)
        response = requests.get(URL_ZILLOW, headers=headers, cookies=cookies)
        json = response.json()
        print(type(json))
        print(json)
