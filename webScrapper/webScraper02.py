from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="C:\\Users\\Raghavendra\\OneDrive\\Desktop\\CyberPresentation\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://www.msrit.edu/about-us.html#history')
file = open("C:\\Users\\Raghavendra\\OneDrive\\Desktop\\CyberPresentation\\scrappedData.txt", "a")

end = '/div/ul'

time.sleep(2)
for num in range(1, 6):
    a = 2
    if num == 2:
        a = 3
    headerXpath = f'//*[@id="evolution"]/div/ul/li[{num}]/div[2]/div[1]/h4'
    bodyXpath = f'//*[@id="evolution"]/div/ul/li[{num}]/div[2]/div[{a}]'

    if num == 1:
        data = driver.find_element(By.XPATH, bodyXpath).text
    else:
        data = driver.find_element(By.XPATH, bodyXpath + end).text

    header = driver.find_element(By.XPATH, headerXpath).text

    file.write(header + '\n')
    file.write(data + '\n\n')

print("Data written to the file")
