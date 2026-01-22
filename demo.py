from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://eaton-sc-web.houyuzhu.com.cn:81/#/login")
print(driver.current_url)