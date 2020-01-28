from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

firefox_binary = FirefoxBinary(r"C:\\Users\\de-jesus.n\\Applications\\FirefoxPortable\\App\\\Firefox64\\firefox.exe")
#cap = DesiredCapabilities().FIREFOX

#browser = webdriver.Firefox(firefox_binary=firefox_binary, capabilities=cap, executable_path=r"C:\Users\de-jesus.n\Documents\code\tdd\geckodriver.exe")
browser = webdriver.Firefox(firefox_binary=firefox_binary)
browser.get('http://localhost:8000')

assert 'Django' in browser.title