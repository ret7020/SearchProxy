import requests

def make_req_requests(query, country_search_code, res_number):
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
    req = requests.get(f"http://www.google.com/search?q={query}&cr=country{country_search_code}&num={res_number}", headers={'User-agent': ua})
    return req.text