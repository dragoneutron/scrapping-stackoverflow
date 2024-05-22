from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()

for page in range(2001, 3001):
    driver.get("https://stackoverflow.com/users?page=" + str(page) + "&tab=reputation&filter=all")
    time.sleep(1)

    url_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".user-gravatar48 > a")
    avatar_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".gravatar-wrapper-48 > img")
    username_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".user-details > a")
    topskill_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".user-tags")
    location_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".user-location")

    users = []

    for index in range(36):
        url = url_elements[index].get_attribute("href")
        avatar = avatar_elements[index].get_attribute("src")
        username = username_elements[index].text
        topskill = topskill_elements[index].text
        location = location_elements[index].text
        
        user = {
            "url": url,
            "avatar": avatar,
            "username": username,
            "topskill": topskill,
            "location": location
        }

        users.append(user)

    file = open("dashboard/european/" + str(page) + ".json", "w")
    file.write(json.dumps(users, indent = 2))

    print(page)