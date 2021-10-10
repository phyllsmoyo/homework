import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


###

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://oxylabs.io/blog')

results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features='lxml')

driver.quit()

###

for a in soup.findAll(attrs='blog-card__content-wrapper'):
    name = a.find('h2')

    if name not in results:
        results.append(name.text)


for b in soup.findAll(attrs='blog-card__date-wrapper'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

if len(results) == len(other_results):
    df = pd.DataFrame({'Names': results, 'Dates': other_results})

else:
    results = results[:(min(len(results), len(other_results)))]
    other_results = results[:(min(len(results), len(other_results)))]
    df = pd.DataFrame({'Names': results, 'Dates': other_results})

df.to_csv('names.csv', index=False, encoding='utf-8')
