from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.kent.edu/")
element = driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/article/div/div/div/div/section/div[1]/div/div/div/a[5]/div/span[1]")
element.click()