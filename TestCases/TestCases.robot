*** Settings ***
Documentation       This is the first test case
Library     AppiumLibrary
Library     OperatingSystem
Library     ../ExternalKeywords/UserKeywords.py

*** Keywords ***
vowifi
    open vo

CLose wifi open LTE
    TC 109

Open wifi close LTE
    TC 108

Call 112
    TC 164

Send Message
    TC 110

End Active Call
    TC 31

Reject Incoming Call
    TC 58

Conference Call
    TC 155 for2phones

Make Call
    TC 10

CLose Uygulamaa
    uygulamakapa

Deneme1
    TC 164 1
Deneme2
    TC 164 2
Deneme3
    TC 164 3
Deneme4
    TC 164 4
Deneme5
    TC 164 5
Deneme6
    TC 164 6
*** Test Cases ***
TEST
    DENEME1
TEST2
    DENEME2
TEST3
    DENEME3
TEST4
    DENEME4
TEST5
    DENEME5
TEST6
    Deneme6
