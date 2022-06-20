from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime

chrome_driver_path = 'C:\\Users\\eiulser\\Downloads\\chromedriver_win32\\chromedriver'
driver = webdriver.Chrome(service = Service(chrome_driver_path))
driver.get("https://dashnet.org/orteil/cookieclicker/")


#event = driver.find_element(By.ID, 'bigCookie' )
# eveniment = True
# while eveniment:
#event.click()

 #if datetime.datetime.now().second %10 == 0:
    prod = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    # x = len(prod)
    # if (len(prod)) >= 1 and prod[x-1].get_attribute():
    #   prod[x-1].click()




#driver.close()



