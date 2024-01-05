from bs4 import BeautifulSoup
import requests, json, lxml

query = "how to learn earn money online"
# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": query,    # query example
    "hl": "en",                         # language
    "gl": "uk",                         # country of the search, UK -> United Kingdom
    "start": 0,                         # number page by default up to 0
    "num": 200                         # parameter defines the maximum number of results to return.
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

page_num = 0

data = []

while True:
    page_num += 1
    print(f"page: {page_num}")
        
    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, 'lxml')
    
    for result in soup.select(".tF2Cxc"):
        title = result.select_one(".DKV0Md").text

        # Handle image gracefully
        image_element = result.select_one(".XNo5Ab")
        image = image_element.get("src") if image_element else None
        try:

           snippet = result.select_one(".VwiC3b.r025kc.hJNv6b.Hdw6tb").text
        except:
           snippet = None
        links = result.select_one(".yuRUbf a")["href"]
      
        data.append({
          "title": title,
          "Image": image,
          "Description": snippet,
          "links": links
        })
      
    if soup.select_one(".d6cvqb a[id=pnnext]"):
        params["start"] += 10
    else:
        break
print(json.dumps(data, indent=2, ensure_ascii=False))
