*** Settings ***
Library     OperatingSystem
Library     AppiumLibrary

*** Variables ***
${message}  merhabalar
${message2}  longer text message for test
${person}   Davut

*** Test Cases ***
TEST1
    OPEN APPLICATION  http://localhost:4723/wd/hub    platformName=iOS   platformVersion=12.5.4    deviceName=iPhone  udid=8ec58a61ea3cb80aafb41abdfe84d4e52f6f8ffa
    Log     This is the second test case



    click element   id=Telefon
    click element   id=Klavye
    click element   id=0
    click element   id=3
    click element   id=1
    click element  id= 2
    click element   id=3
    click element   id=4
    click element   id=7
    click element   id=2
    click element   id=9
    click element   id=0
    click element   id=8
    click element   id=Ara
    wait until page contains element   id=Aramayı bitir
    click element   id=Aramayı bitir



TEST3
    click element  id=Ayarlar
    click element  id=Hücresel
    click element  id=Wi-Fi ile Arama
    click element  class=XCUIElementTypeCell
    wait until page contains element  id=Etkinleştir
    click element  id=Etkinleştir

TEST4
    click element  id=Ayarlar
    click element  id=Hücresel
    click element  class=XCUIElementTypeCell
    click element  xpath=//XCUIElementTypeButton[@name='Ayarlar']
    click element  id= Wi-Fi
    click element  class=XCUIElementTypeCell
    click element  xpath=//XCUIElementTypeButton[@name='Ayarlar']

TEST5
    wait until page contains element  id=Reddet
    click element  id=Reddet


TEST8
    wait until page contains element  id=sesi kapat
    long press  id=sesi kapat  duration=5000
    wait until page contains element   id=TUT
    click element   id=TUT

TEST2
    click element  id=Mesajlar
    click element  id=${person}
    click element  id=messageBodyField
    input text     id=messageBodyField   text=${message2}
    click element  id=sendButton


