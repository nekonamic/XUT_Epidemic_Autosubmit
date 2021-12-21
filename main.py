import time
import requests

url = "https://app.xaut.edu.cn/ncov/wap/default/save"
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "2078",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "",
    # TODO: fill the Cookie
    "Host": "app.xaut.edu.cn",
    "Origin": "https://app.xaut.edu.cn",
    "Referer": "https://app.xaut.edu.cn/ncov/wap/default/index",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
data = {
    "zgfxdq": "0",
    "mjry": "0",
    "csmjry": "0",
    "tw": "2",
    "sfcxtz": "0",
    "sfjcbh": "0",
    "sfcxzysx": "0",
    "qksm": "",
    "sfyyjc": "0",
    "jcjgqr": "0",
    "remark": "",
    "address": "陕西省西安市碑林区东关南街街道咸宁西路11号西安理工大学金花校区",
    "geo_api_info": '{"type":"complete","info":"SUCCESS","status":1,"fEa":"jsonp_848797_","'
                    'position":{"Q":34.25177,"R":108.99191000000002,"lng":108.99191,"lat":34.25177},'
                    '"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,'
                    '"isConverted":true,"addressComponent":{"citycode":"029","adcode":"610103","businessAreas":[],'
                    '"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"咸宁西路",'
                    '"streetNumber":"11号","country":"中国","province":"陕西省","city":"西安市","district":"碑林区",'
                    '"towncode":"610103004000","township":"东关南街街道"},'
                    '"formattedAddress":"陕西省西安市碑林区东关南街街道咸宁西路11号西安理工大学金花校区","roads":[],"crosses":[],"pois":[]}',
    "area": "陕西省 西安市 碑林区",
    "province": "陕西省",
    "city": "西安市",
    "sfzx": "0",
    "sfjcwhry": "0",
    "sfjchbry": "0",
    "sfcyglq": "0",
    "gllx": "",
    "glksrq": "",
    "jcbhlx": "",
    "jcbhrq": "",
    "ismoved": "0",
    "bztcyy": "",
    "sftjhb": "0",
    "sftjwh": "0",
    "jcjg": "",
}
print("[" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))) + "] " +
      eval(requests.post(url=url, data=data, headers=headers).text)["m"])
