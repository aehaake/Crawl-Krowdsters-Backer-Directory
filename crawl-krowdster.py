# Import required libraries
import os
import time
import numpy as np
import pandas as pd
import codecs
import scipy.interpolate as si
from bs4 import BeautifulSoup
from random import randint
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome Driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the target URL
driver.get("https://app.krowdster.co/backer/directory")

# Enter username
username = driver.find_element("xpath", '/html/body/div/div[2]/div[1]/form/div[1]/input')
username.send_keys("YOURMAIL@gmail.com")

# Enter password
password = driver.find_element("xpath", '/html/body/div/div[2]/div[1]/form/div[2]/div/input')
password.send_keys("YOURPW")

# Click to submit form
driver.find_element("xpath", "/html/body/div/div[2]/div[1]/form/div[3]/input").click()

# Define curve base for mouse movement
points = [[0, 0], [0, 2], [2, 3], [4, 0]]  # curve base
points = np.array(points)

x = points[:, 0]
y = points[:, 1]

t = range(len(points))
ipl_t = np.linspace(0.0, len(points) - 1, 100)

x_tup = si.splrep(t, x, k=3)
y_tup = si.splrep(t, y, k=3)

x_list = list(x_tup)
xl = x.tolist()
x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

y_list = list(y_tup)
yl = y.tolist()
y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

x_i = si.splev(ipl_t, x_list)  # x interpolate values
y_i = si.splev(ipl_t, y_list)  # y interpolate values

# Perform actions on webpage
for ind in range(1, 5):
    htmlS = driver.execute_script("return document.body.innerHTML;")
    Html_file = open("p_"+str(ind)+".html", "w", encoding="utf-8")
    Html_file.write(htmlS,)
    Html_file.close()
    action = ActionChains(driver)

    startElement = driver.find_element(
        By.XPATH, '//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/form/div/div/div[2]/select')

    action.move_to_element(startElement)
    action.move_to_element(startElement)
    action.perform()

    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_by_offset(mouse_x, mouse_y)
        action.perform()

    time.sleep(randint(2, 5))
    driver.find_element(
        "xpath", '//*[@id="wrapper"]/article/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/ul/li[12]/a').click()
    time.sleep(10)

# Generate profile List
listBackers = []
for file in os.listdir():
    if "html" in file:
        print(file)

        f = codecs.open(file, 'r', encoding="utf=8")
        soup = BeautifulSoup(f.read())

        els = soup.find_all("div", {"ng-repeat": "result in results.data"})

        for el in els:
            backer = {}
            backer["num backed"] = el.find(
                "div", {"class": "num_backed ng-binding"}).text.replace("Backed", "")
            backer["name"] = el.find(
                "h4", {"class": "media-heading backer-name"}).text
            backer["loc"] = el.find(
                "div", {"class": "backer-location ng-binding"}).text
            links = list(
                set([b["href"] for b in el.find_all("a") if "href" in b.attrs.keys()]))
            for l in links:
                host = (urlparse(l).netloc)
                backer[host] = l

            listBackers.append(backer)

# Store data in an Excel file
backXlsx = pd.DataFrame(listBackers).drop_duplicates(subset="name")
backXlsx.to_excel("backer.xlsx")
