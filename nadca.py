import urllib.request
import csv
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()

        sp = BeautifulSoup(html, "html.parser")

        for tag in sp.find_all("a"):
            url = tag.get("href")
            #print (url)
            #print("\n" + url)

        all_data1 = []
        all_data2 = []
        all_data = {}
        

        for tag1 in sp.find_all('td', class_='views-field views-field-nothing'):
            text1 = tag1.get_text()
            text1_list = text1.splitlines()
            text1_list = [i for i in text1_list if i]
            all_data1.append(text1_list)

        for tag2 in sp.find_all('td', class_='views-field views-field-nothing-1'):
            text2 = tag2.get_text()
            text2_list = text2.splitlines()
            text2_list = [i for i in text2_list if i]
            all_data2.append(text2_list)
    
        for idx, all_data1 in enumerate(all_data1):
            all_data1 = tuple(all_data1)
            all_data[all_data1] = all_data2[idx]

        with open("C:/tmp/nadca.csv", "w", newline='') as f:
            write=csv.writer(f, delimiter=",")
            write.writerow(["Company Name","Contact", "Street","City", "StateZip", "Email", "Phone"])

            for key in all_data:
                #print (key, all_data[key])
                key_list = key
                city_state = key_list[2].split(",")
                #state_zip = city_state[1].split(" ")
                write.writerow ([key_list[0], all_data[key][0][9:], key_list[1], city_state[0], city_state[1], all_data[key][3], all_data[key][1][4:]])
                #print ("next\n")

scr = Scraper('https://nadca.com/find-a-professional?page=1')
scr.scrape()
