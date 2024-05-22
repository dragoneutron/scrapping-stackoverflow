from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

file = open("europeans.json", "r", encoding="UTF8")
europeans = json.loads(file.read())

driver = webdriver.Chrome()

driver.get("https://github.com/")
time.sleep(30)

print("Start")

developerCount = 0

americanCount = len(europeans)

for index in range(0, americanCount):
    american = europeans[index]

    driver.get(american["url"])
    time.sleep(2)

    github = ""

    link_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".ps-relative.mb16 a")
    for element in link_elements:
        href = element.get_attribute("href")
        if href.find("github.com") != -1:
            github = href
            break
    
    if github == "":
        print(str(index + 1) + "/" + str(americanCount) + " " + str(developerCount))
        continue

    driver.get(github)
    time.sleep(2)

    email = ""

    link_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".js-profile-editable-area a")
    for element in link_elements:
        href = element.get_attribute("href")
        if href.startswith("mailto:"):
            email = href[7:]
            break
    
    if email != "":
        developerCount += 1

        username = american["username"].split()[0]

        file = open("european_developers.txt", "a", encoding="UTF8")
        file.write(email + " " + username + " " + american["url"] + "\n")

    print(str(index + 1) + "/" + str(americanCount) + " " + str(developerCount))