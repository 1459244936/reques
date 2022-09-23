import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
for num in range(1,4):
    url = "https://www.zongheng.com/rank/details.html?rt=7&d=1&p={}".format(num)
    response = requests.get(url,headers = headers)
    response.encoding = "utf-8"
    file_name = "纵横小说第--{}--页.html".format(num)
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(response.text)
        print(file_name, "写入完成")
