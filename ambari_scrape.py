from selenium import webdriver
browser = webdriver.Chrome("/Users/rraman/PycharmProjects/WebScraping/webdrivers/chromedriver")

login_url = "http://c249-node1.coelab.cloudera.com:8080/"
browser.get(login_url)

login_user_element = browser.find_element_by_class_name('login-user-name')
login_user_element.send_keys("admin")

login_user_password_element = browser.find_element_by_class_name('login-user-password')
login_user_password_element.send_keys("admin")

login_btn = browser.find_element_by_class_name("login-btn")
login_btn.click()

#After login
url = login_url + "#/main/dashboard/metrics"
browser.get(url)

#Installed services
browser.implicitly_wait(30)  #Wait for max upto 30 seconds for the page to load
services_element = browser.find_element_by_class_name("services-menu")
service_dict = dict.fromkeys((services_element.text).split("\n"))

#Cleaning up dict items
#service_dict.pop("1")
service_dict.pop("Actions")
service_dict = {k.strip(): v for(k,v) in service_dict.items()}

#convert dict to list
service_list = list(service_dict.keys())
print(service_list)
