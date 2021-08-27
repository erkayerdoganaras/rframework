from appium import webdriver
from robot.api.deco import keyword
from robot.api.deco import library
from AppiumLibrary.keywords import *
import time

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                                      desired_capabilities={

                                          'platformName': 'iOS',
                                          'platformVersion': '12.5.4',
                                          'deviceName': 'iPhone',
                                          'udid': '8ec58a61ea3cb80aafb41abdfe84d4e52f6f8ffa'

                                      })

@keyword
def TC_10(numero):
    driver.find_element_by_accessibility_id("Telefon").click()
    driver.find_element_by_accessibility_id("Klavye").click()
    for i in range(0,11):
        driver.find_element_by_accessibility_id("{}".format(numero[i])).click()
    driver.find_element_by_accessibility_id("Ara").click()

@keyword
def open_vo():
    try:


        driver.find_element_by_accessibility_id("Ayarlar").click()
        driver.find_element_by_accessibility_id("Hücresel").click()
        driver.find_element_by_accessibility_id('Wi-Fi ile Arama').click()
        voWifi = driver.find_element_by_class_name('XCUIElementTypeCell')
        if voWifi.get_attribute('value') == '0':
            voWifi.click()
            driver.find_element_by_accessibility_id("Etkinleştir").click()
            print("VoWifi has opened")
            driver.background_app(-1)
        else:
            print("VoWifi has already been open")
            driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Hücresel']").click()
            driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Ayarlar']").click()
            driver.background_app(-1)
    except Exception as e:
        print("Error: {}".format(e))

@keyword
def TC_109():
    try:
        driver.find_element_by_accessibility_id("Ayarlar").click()
        driver.find_element_by_accessibility_id("Wi-Fi").click()
        wifi=driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='Wi‑Fi']")
        if wifi.get_attribute('value')=='1':
            wifi.click()
            print("Wifi has closed")
        else:
            print("Wifi has already been closed")
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Ayarlar']").click()
        driver.find_element_by_accessibility_id("Hücresel").click()
        hucresel=driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='Hücresel Veri']")
        if hucresel.get_attribute('value')=='0':
            hucresel.click()
            print("LTE has opened")
        else:
            print("LTE has already been open")
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Ayarlar']").click()
        driver.background_app(-1)
    except Exception as e:
        print("Error: {}".format(e))


@keyword
def denem1():
    driver.find_element_by_accessibility_id("Ayarlar").click()
@keyword
def denem2():
    driver.find_element_by_accessibility_id("Hücresel").click()
@keyword
def denem3():
    hucresel=driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='Hücresel Veri']")
    hucresel.click()
@keyword
def uygulamakapa():
    driver.background_app(-1)







@keyword
def TC_108():
    try:
        driver.find_element_by_accessibility_id("Ayarlar").click()
        driver.find_element_by_accessibility_id("Hücresel").click()
        hucresel=driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='Hücresel Veri']")
        if hucresel.get_attribute('value')=='1':
            hucresel.click()
            print("LTE has closed")
        else:
            print("LTE has already been closed")
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Ayarlar']").click()
        driver.find_element_by_accessibility_id("Wi-Fi").click()
        wifi=driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='Wi‑Fi']")
        if wifi.get_attribute('value')=='0':
            wifi.click()
            print("Wifi has opened")
        else:
            print("Wifi has already been open")
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Ayarlar']").click()
        driver.background_app(-1)
    except Exception as e:
        print("Error: {}".format(e))

@keyword
def TC_164():
    try:
        driver.find_element_by_accessibility_id("Telefon").click()
        driver.find_element_by_accessibility_id("Klavye").click()
        driver.find_element_by_accessibility_id("1").click()
        driver.find_element_by_accessibility_id("1").click()
        driver.find_element_by_accessibility_id("2").click()
        print("Calling 112")
        driver.find_element_by_accessibility_id("Ara").click()
    except Exception as e:
        print("Error: {}".format(e))

@keyword
def TC_164_1():
    driver.find_element_by_accessibility_id("Telefon").click()
@keyword
def TC_164_2():
    driver.find_element_by_accessibility_id("Klavye").click()
@keyword
def TC_164_3():
    driver.find_element_by_accessibility_id("1").click()
@keyword
def TC_164_4():
    driver.find_element_by_accessibility_id("1").click()
@keyword
def TC_164_5():
    driver.find_element_by_accessibility_id("2").click()
@keyword
def TC_164_6():
    driver.find_element_by_accessibility_id("Ara").click()






@keyword
def TC_110(who:str,message:str):
    try:
        driver.find_element_by_accessibility_id("Mesajlar").click()
        driver.find_element_by_accessibility_id(who).click()
        driver.find_element_by_accessibility_id("messageBodyField").click()
        driver.find_element_by_accessibility_id("messageBodyField").send_keys(message)
        driver.find_element_by_accessibility_id("sendButton").click()
        driver.find_element_by_xpath("//XCUIElementTypeNavigationBar[@name='CKChat']/XCUIElementTypeButton").click()
    except Exception as e:
        print("Error: {}".format(e))

@keyword
def TC_58(): #When compiled after call
    driver.find_element_by_accessibility_id("Reddet").click()

@keyword
def TC_50(numero):
    driver.find_element_by_accessibility_id("Telefon").click()
    driver.find_element_by_accessibility_id("Klavye").click()
    for i in range(0, 11):
        driver.find_element_by_accessibility_id("{}".format(numero[i])).click()
    driver.find_element_by_accessibility_id("Ara").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("Aramayı bitir").click()

@keyword
def TC_31():
    driver.find_element_by_accessibility_id("Aramayı bitir").click()


@keyword
def TC_155_for2phones(numero1,numero2):
    try:
        driver.find_element_by_accessibility_id("Telefon").click()
        driver.find_element_by_accessibility_id("Klavye").click()
        for i in range(0, 11):
            driver.find_element_by_accessibility_id("{}".format(numero1[i])).click()
        driver.find_element_by_accessibility_id("Ara").click()
        time.sleep(20)
        driver.find_element_by_accessibility_id("arama ekle").click()
        driver.find_element_by_accessibility_id("Klavye").click()
        for i in range(0, 11):
            driver.find_element_by_accessibility_id("{}".format(numero2[i])).click()
        driver.find_element_by_accessibility_id("Ara").click()
        time.sleep(20)
        driver.find_element_by_accessibility_id("konferans").click()
    except Exception as e:
        print("Error: {}".format(e))