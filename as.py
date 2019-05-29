import requests
import codecs
from bs4 import BeautifulSoup

url = "http://csie.asia.edu.tw/project/182-107%E5%AD%B8%E5%B9%B4#%E7%AC%AC%E4%BA%8C%E7%B5%84"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

out_file = codecs.open('result.csv', 'w', 'big5')



tb = soup.find('table', class_='table table-bordered table-hover')

for tr_data in tb.find_all('tr'):

    for td_data in tr_data.find_all('td'):
       td_value = td_data.text
       td_value = td_value.replace('\n', '')
       td_value = td_value.replace('\r', '')
       out_file.write(td_value)
       out_file.write(',')

       
    out_file.write('\n')

out_file.close()        
 