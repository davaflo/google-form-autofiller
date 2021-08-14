from selenium import webdriver
from datetime import datetime




option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path = "D:\Descargas\chromedriver_win32/chromedriver.exe", options=option)

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSd2IcTMJFTa_Dc4bbCZGkMVvltfJ9h_u335qMMk-oQW_huvVg/viewform")

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")


textboxes[0].send_keys("NAME")

today = datetime.now()
textboxes[1].send_keys(today.strftime("%m/%d/%Y"))
textboxes[2].send_keys("000000")

radiobuttons[1].click()

textboxes[5].send_keys(today.strftime("%H"))
textboxes[6].send_keys(today.strftime("%M"))

radiobuttons[3].click()
radiobuttons[4].click()

checkboxes[4].click()

textboxes[7].send_keys("N/A")

