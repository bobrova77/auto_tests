import math, time
from selenium import webdriver

# Рассчитаю значение для переменной х
def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

# Вводим ответ в текстовое поле  
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

element1 = browser.find_element_by_css_selector('#answer')
element1.send_keys(y)

# Отметить checkbox "I'm the robot"
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()
option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
option2 = browser.find_element_by_css_selector("[type='submit']")
option2.click()

time.sleep(5)
browser.quit()

    


