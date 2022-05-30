
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get("http://127.0.0.1:5000/")

value = driver.find_element_by_id("score").text
print(value)
driver.quit()


