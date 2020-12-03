from selenium import webdriver
import time


# NOTE BLANTONS

driver = webdriver.Firefox(
    executable_path=r'C:\Users\sleba\AppData\Local\Programs\geckodriver-v0.28.0-win64\geckodriver.exe')
driver.get(
    'https://mixblendenjoy.com/product/?nabca=16850&query=16850')

age_verification_button = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/form[1]/input[2]")
age_verification_button.click()

time.sleep(2)

limited_availability_button = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[2]/a[1]/img[1]")
limited_availability_button.click()

time.sleep(2)

blantons_button = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[1]/ul[1]/li[6]/a[1]")
blantons_button.click()

time.sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[1])

check_availability_button = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[2]/div[1]/div[2]/main[1]/div[4]/a[1]")
check_availability_button.click()

time.sleep(2)

zipcode_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[2]/div[1]/div[2]/main[1]/div[3]/form[1]/input[1]")
zipcode_input.click()
zipcode_input.clear()
zipcode_input_string = "83616"
for char in zipcode_input_string:
    zipcode_input.send_keys(char)

time.sleep(2)

zipcode_input_button = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[2]/div[1]/div[2]/main[1]/div[3]/form[1]/input[4]")
zipcode_input_button.click()

time.sleep(2)

location_results = driver.find_elements_by_id("results")
location_search_string = location_results.find("Hailey")
if(location_search_string in location_results):
    print("yes")
else:
    print(location_results)
    print("no")

# all_results = driver.find_elements_by_xpath("//*[contains(text(),'Hailey')]")
# print len(all_results)

# NOTE create new tab instead of new window, export to notepad?

# NOTE EAGLE RARE

# driver = webdriver.Firefox(
#     executable_path=r'C:\Users\sleba\AppData\Local\Programs\geckodriver-v0.28.0-win64\geckodriver.exe')
# driver.get(
#     'https://mixblendenjoy.com/product/?nabca=16850&query=16850')

# age_verification_button = driver.find_element_by_xpath(
#     "/html[1]/body[1]/div[1]/form[1]/input[2]")
# age_verification_button.click()

# time.sleep(2)

# limited_availability_button = driver.find_element_by_xpath(
#     "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[2]/a[1]/img[1]")
# limited_availability_button.click()

# eagle_rare_button = driver.find_element_by_xpath(
#     "/html[1]/body[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[1]/ul[1]/li[14]/a[1]")
# eagle_rare_button.click()

# time.sleep(2)
