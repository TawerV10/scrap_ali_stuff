import requests, json, csv

headers = {
    'accept': 'application/json, text/plain, */*',
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'x-frame-options': 'DENY',
    'x-robots-tag': 'noindex',
    'x-xss-protection': '1; mode=block'
}

def get_json():
    url = 'https://www.aliexpress.com/glosearch/api/product?trafficChannel=af&catName=hair-trimmers&CatId=205849704&ltype=affiliate&SortType=default&page=2&isrefine=y&origin=y&pv_feature=1005003495039452,1005003888237075,1005004194479986,1005004282663233,1005002459868921,1005004110028688,1005004417054882,1005004410470266,1005004085902025,1005003716945438,4000106945073,1005004442510822,1005004370541304,1005004481816119,1005004419880879,4001159089014,1005003415869986,1005004480709115,1005003969578749,1005003834832719,1005003804334559,1005004221073676,1005004474142367,1005002194418281,1005004324830154,1005003769600548,1005004463132093,1005004486227536,1005004451876175,1005004350952895,1005004409041653,1005004480283825,1005003991559022,1005004193940054,1005003202519064,1005004318924221,1005004481465750,1005004478111634,1005004437700058,1005004451768389'
    r = requests.get(url, headers)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(r.text, file, indent=4, ensure_ascii=False)

def get_data():
    data = []
    with open('data.json', encoding='utf-8') as file:
        JSON = json.load(file)

    all_stuff = JSON['mods']['itemList']['content']
    for stuff in all_stuff:
        image = stuff['image']['imgUrl']
        title = stuff['title']['displayTitle']
        sale_price = stuff['prices']['salePrice']['formattedPrice'].replace('US ', '')
        store = stuff['store']['storeName']

        data.append({
            'title': title,
            'image': image,
            'sale_price': sale_price,
            'store': store,
        })

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    # get_json()
    get_data()

if __name__ == '__main__':
    main()