import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
dirtyadr=pd.read_excel("fingertips.xlsx")
driver = webdriver.Chrome(ChromeDriverManager().install())
def address():
 search_string="Chop Shop Kochi"
 search_string = search_string.replace(' ','+')
 matched_elements = driver.get("https://www.google.co.in/search?q=" + search_string)
 driver.maximize_window() 
 driver.refresh()
 sleep(1)
 try:
  address=driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[5]/div/div/div/span[2]').text #happycup
 except:
  try:    
   address=driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[4]/div/div/div').text #cera
  except:
   try:
    address=driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[6]/div/div/div/span[2]').text #xilli
   except:
    try:
     address=driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[7]/div/div/div/span[2]').text   
    except:
     address=driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[4]/div/div/div/span[2]').text   
 print(address)
 return address
address()
