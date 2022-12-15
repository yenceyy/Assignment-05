from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://seleniumpractice.arisdelareapup.repl.co/")

a1 = driver.find_element("id", "fname").send_keys("Jett")
a2 = driver.find_element("id", "activity").send_keys("bonefire")
a3 = driver.find_element("id", "fee").send_keys("₱100.00")
a4 = driver.find_element("id", "bdate").send_keys("01/01/1999")
dropdown = Select(driver.find_element(By.XPATH,'(//select)[1]'))
dropdown.select_by_index(5)

b1 = driver.find_element("name", "fname2").send_keys("Yoru")
b2 = driver.find_element('xpath', "(//input[@name='activity'])[2]").send_keys("nagsisilab")
b3 = driver.find_element("id", "fee1").send_keys("₱300.00")
b4 = driver.find_element('xpath',"(//input[@name='bdate'])[2]").send_keys("12/12/1999")
dropdown2 = Select(driver.find_element(By.XPATH,'(//select)[2]'))
dropdown2.select_by_index(3)

c1 = driver.find_element('xpath',"(//input[@name='fname'])[2]").send_keys("Raze")
c2 = driver.find_element('xpath', "(//input[@name='activity'])[3]").send_keys("nag-iihaw")
c3 = driver.find_element('xpath', "//input[@id='fee2']").send_keys("50,000")
button1 = driver.find_element('xpath', "//span[normalize-space()='Yes - I am a city resident']").click()

d1 = driver.find_element('xpath',"(//input[@id='fname'])[3]").send_keys("Kay Nino")
d2 = driver.find_element("id", "lname").send_keys("Kalang")
add1 = driver.find_element("id", "address1").send_keys("Brgy.Takoyaki")
add2 = driver.find_element("id", "address2").send_keys("Brgy.Brownies")
ct = driver.find_element("id", "city").send_keys("City of Santotomels")
st = driver.find_element("id", "state").send_keys("Batangas")
email = driver.find_element("id", "eaddress").send_keys("gmail@yahoo.com")
pnumber = driver.find_element("id", "phone").send_keys("091234567890")
zip = driver.find_element("id", "zip").send_keys("6969")
button2 = driver.find_element('xpath',"//span[normalize-space()='Guardian']").click()
input = driver.find_element('xpath',"(//input[@type='text'])[15]").send_keys("Pinsan")