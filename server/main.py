from selenium import webdriver
result = {}
driver = webdriver.Chrome(
    '/Users/abhishek/Documents/Personal/Chatr/server/chromedriver')
driver.get("https://www.linkedin.com/")
assert "LinkedIn" in driver.title
username = driver.find_element_by_id('session_key')
username.send_keys('adixitiitian@gmail.com')
password = driver.find_element_by_id('session_password')
password.send_keys('india2794')
driver.find_element_by_class_name('sign-in-form__submit-button').click()
assert "LinkedIn" in driver.title
driver.get("https://www.linkedin.com/in/risasiegel")
result['name'] = driver.find_element_by_xpath("//ul[contains(@class, 'pv-top-card--list') and contains(@class, 'align-items-center')]/li[1]").text
result['headline'] = driver.find_element_by_xpath("//div[contains(@class, 'flex-1 mr5')]/h2").text
result['country/region'] = driver.find_element_by_xpath("//ul[contains(@class, 'pv-top-card--list') and contains(@class, 'pv-top-card--list-bullet mt1')]/li").text
see_more = driver.find_element_by_class_name('lt-line-clamp__more')
if see_more:
	see_more.click()
result['about'] = driver.find_element_by_xpath("//p[contains(@class, 'pv-about__summary-text')]").text

print(result)
driver.close()