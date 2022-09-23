from pydoc import resolve
import  requests
class Novel_Data(object):
    def __init__(self):
        self.url = "https://www.zongheng.com/rank/details.html?rt=7&d=1&p={}.html"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    def get_url_page(self):
        url_list = []
        for num in range(1,4):
            url_list.append(self.url.format(num))
        return url_list
    
    def get_data_index(self,url):
        response = requests.get(url,headers=self.headers)
        response.encode  = "utf-8"
        if response.status_code == 200:
            return response.text
        else:
            return None
    def write_data(self,resp,number):
        file_name = "纵横小说第--{}--页.html".format(number)
        with open(file_name,"a",encoding="utf-8") as f:
            f.write(resp)
            print (file_name,"写入完成")
           
    def run(self):
        url_list = self.get_url_page()
        for url in url_list:
            resp = self.get_data_index(url)
            number = url_list.index(url)+1
            self.write_data(resp,number)


            

        



if __name__ == '__main__':
    spider = Novel_Data()
    spider.run()

            
