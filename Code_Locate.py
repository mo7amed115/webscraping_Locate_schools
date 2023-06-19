import pandas as pd
import selenium
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from multiprocessing import Pool
from datetime import datetime

options = Options()

driver = webdriver.Chrome(options=options)
url = 'https://locate.cisce.org/result'
driver.get(url)
time.sleep(1)
driver.maximize_window()
time.sleep(5)

result = []
for i in range(2):
    print(f"Page : {i}")
    containers  = driver.find_elements('xpath','/html/body/div[3]/div/div/div/div/div/div[2]/div/table/tbody/tr/td[1]/ul')
    containers2 = driver.find_elements('xpath','/html/body/div[3]/div/div/div/div/div/div[2]/div/table/tbody/tr/td[2]/ul')
    containers3 = driver.find_elements('xpath','/html/body/div[3]/div/div/div/div/div/div[2]/div/table/tbody/tr/td[3]/ul')
    containers4 = driver.find_elements('xpath','/html/body/div[3]/div/div/div/div/div/div[2]/div/table/tbody/tr/td[4]/ul')
    containers5 = driver.find_elements('xpath','/html/body/div[3]/div/div/div/div/div/div[2]/div/table/tbody/tr/td[5]/ul')

    for c, x, category, course, manager in zip(containers, containers2, containers3, containers4, containers5):
        code = c.find_elements('xpath', ".//li[1]")
        Name = c.find_elements('xpath', ".//li[2]")
        adress = c.find_elements('xpath', ".//li")
        address = []
        for i in range(3, 8):
            address.append(adress[i].text)
        address = " / ".join(address)

        txt = x.find_elements('xpath', './/li')
        d2 = {}
        for i in txt:
            text = i.text
            if 'Phone' in text:
                d2['Phone'] = text.replace('Phone :\n', '').replace(',', ' / ')
            elif 'Fax' in text:
                d2['Fax'] = text.replace('Fax :\n', '')
            elif 'Email' in text:
                d2['Email'] = text.replace('Email:-\n', '').replace(',', ' / ')
            elif 'Website' in text:
                d2['Website'] = text.replace('Website:-', '').replace(',', ' / ').replace('Copy', '')

        category = category.text.replace('Co-ed.\n', '').replace('\n', ' / ')
        course = course.text.replace('\n', ' / ')
        head_manager = manager.text

        data_dict = {
            'Code': code[0].text,
            'Name': Name[0].text,
            'Address': address,
            'Phone': d2.get('Phone', ''),
            'Fax': d2.get('Fax', ''),
            'Email': d2.get('Email', ''),
            'Website': d2.get('Website', ''),
            'Category': category,
            'Course': course,
            'Manager_name': head_manager
        }

        result.append(data_dict)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    print('Done')
    time.sleep(1)
    try:
        m = driver.find_element('xpath','/html/body/div[3]/div/div/div/div/div/div[3]/div[2]/div/ul/li[9]/a')
        time.sleep(1)
        m.click()
    except:
        pass
    
# Create a DataFrame from the result list
df = pd.DataFrame(result)

# Define the desired order of columns
columns = ['Code', 'Name', 'Address', 'Phone', 'Fax', 'Email', 'Website', 'Category', 'Course', 'Manager_name']

# Reorder the columns in the DataFrame
df = df[columns]

# Save the DataFrame to an Excel file
df.to_excel('Locate_school.xlsx', index=False)
