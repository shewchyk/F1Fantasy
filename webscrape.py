from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from races import race_name
service = Service()

#region list paceholders
Verstappen = []
Bottas = []
Hamilton = []
Stroll = []
Alonso = []
Russell = []
Sainz = []
Leclerc = []
Norris = []
Gasly = []
Perez = []
Magnussen = []
Tsunoda = []
Albon = []
Zhou = []
Ocon = []
Piastri = []
Hulkenberg = []
De_vries = []
Sargeant = []
Ricciardo = []
#endregion

def get_webdriver(race_name): 
    options = webdriver.ChromeOptions()
    #region selenium options
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    #endregion
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(race_name)
    return driver

#Adds web elements to drivers' list 
def list_ext(name_web, pos_web):
    #region case function
    match name_web.text:
        case "Bottas":
            Bottas.append(pos_web)
        case "Hamilton":
            Hamilton.append(pos_web)
        case "Verstappen":
            Verstappen.append(pos_web)
        case "Stroll":
            Stroll.append(pos_web)
        case "Alonso":
            Alonso.append(pos_web)
        case "Russell":
            Russell.append(pos_web)
        case "Sainz":
            Sainz.append(pos_web)
        case "Leclerc":
            Leclerc.append(pos_web)
        case "Norris":
            Norris.append(pos_web)
        case "Gasly":
            Gasly.append(pos_web)
        case "Perez":
            Perez.append(pos_web)
        case "Magnussen":
            Magnussen.append(pos_web)
        case "Tsunoda":
            Tsunoda.append(pos_web)
        case "Albon":
            Albon.append(pos_web)
        case "Guanyu":
            Zhou.append(pos_web)
        case "Ocon":
            Ocon.append(pos_web)
        case "Piastri":
            Piastri.append(pos_web)
        case "Hulkenberg":
            Hulkenberg.append(pos_web)
        case "De Vries":
            De_vries.append(pos_web)
        case "Sargeant":
            Sargeant.append(pos_web)
        case "Ricciardo":
             Ricciardo.append(pos_web)
    #endregion

#Converts list contents from web elements (text) to int
#If statement averages sessions results for drivers who missed an FP session(s) (replaced by reserve drivers / mechanical issues / etc.)
def pos_int(list, surname):
    list = [int(x) for x in list]
    if len(list) <= 2:
        a = sum(list) / len(list)
        total = int(round(sum(list) + a, 0))
    else: total = int(round(sum(list), 0))
    print(total, surname, list)

def webscrape():
    a = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    x = 0
    while x < len(race_name):
       webdriver = get_webdriver(race_name[x])
       time.sleep(3)
       #region clears cookie popup
       cookie = webdriver.find_element(by=By.CLASS_NAME, value="trustarc-agree-btn")
       cookie.click()
       #endregion
       y = 0
       while y < len(a):
           try:
            name_web = webdriver.find_element(by="xpath", value="/html/body/div[2]/main/article/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[" + a[y] + "]/td[4]/span[2]")
           except NoSuchElementException:
               break
           try:
            pos_web = webdriver.find_element(by="xpath", value="/html/body/div[2]/main/article/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[" + a[y] + "]/td[2]")
           except NoSuchElementException:
               break
           list_ext(name_web, pos_web.text)
           y += 1
       x += 1

webscrape()
pos_int(Bottas, "Bottas:")
pos_int(Stroll, "Stroll")
pos_int(Alonso, "Alonso")
pos_int(Verstappen, "Verstappen")
pos_int(Hamilton, "Hamilton")
pos_int(Russell, "Russell")
pos_int(Sainz, "Sainz")
pos_int(Leclerc, "Leclerc")
pos_int(Norris, "Norris") 
pos_int(Gasly, "Gasly") 
pos_int(Perez, "Perez") 
pos_int(Magnussen, "Magnussen") 
pos_int(Tsunoda, "Tsunoda")
pos_int(Albon, "Albon") 
pos_int(Zhou, "Zhou")
pos_int(Ocon, "Ocon")
pos_int(Piastri, "Piastri") 
pos_int(Hulkenberg, "Hulkenberg") 
#pos_int(De_vries, "De_vries") 
pos_int(Sargeant, "Sargeant") 
pos_int(Ricciardo, "Ricciardo")
