from time import sleep 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from datetime import datetime,timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import calendar 

path_of_driver='/usr/local/bin/chromedriver'
driver=webdriver.Chrome(path_of_driver)
path="https://www1.nseindia.com/ArchieveSearch?h_filetype=fobhav&date="
path1="&section=FO"


start_date_string = input("enter the start date in the format dd-mm-yyyy")
end_date_string=input("enter the end date in the format of dd-mm-yyyy")
format_string = "%d-%m-%Y"


x=datetime.strptime(start_date_string, format_string)
y=datetime.strptime(end_date_string, format_string)

while (x!=y):
    if (x.weekday()==6 or x.weekday()==5):
        x=x+timedelta(1)
        continue
    date=datetime.strftime(x,format_string)
    final_path=path+date+path1
    print(final_path)
    driver.get(final_path)
    sleep(0.5)
    try:
        result = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr/td/a"))
        
    )
        result.click()
        
    except:
        x=x+timedelta(1)
        continue
   
    sleep(0.5)
    x=x+timedelta(1)
driver.close()