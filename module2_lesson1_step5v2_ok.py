from selenium import webdriver
import math
 
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
 
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
 
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(int(x))
 
 
button = browser.find_element_by_tag_name("button")
browser.execute_script('return arguments[0].scrollIntoView(true);', button)
 
 
input = browser.find_element_by_id("answer")
input.send_keys(y)
 
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
 
radioB = browser.find_element_by_css_selector("[for = 'robotsRule']")
radioB.click()
 
button = browser.find_element_by_css_selector("button.btn")
button.click()

    


