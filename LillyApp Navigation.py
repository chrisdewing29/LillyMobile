from selenium import webdriver
from applitools.eyes import Eyes
from appium.webdriver.common.touch_action import TouchAction
import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

'''

This program will open the Lilly Mobile app and navigate through the app testing the functionality of all the buttons.
In addition, screen shots of the app will be taken using the Appitools eyes app

'''


class lillyApp():
    # gloabal variables for the methods
    desired_caps = dict(
        platformName='Android',
        deviceName='Galaxy S8',
        platformVersion='8.0.0',
        app='C:\\Users\\chris.dewing\\Desktop\\lillydevicetestapp-1.6-release (1).apk'
        # app_package = "com.lilly.ddcs.lillydevicetestapp",
        # app_activity = 'com.lilly.ddcs.lillydevicetestapp.TestActivity'
    )
    # Open the app.
    wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    wd.implicitly_wait(10)

    # Initialize the eyes SDK and set your private API key.
    eyes = Eyes()
    eyes.api_key = 'lDFzChp3PyMmFF1KVoNlgU2NMG108tWfUHBlItYgC0njA110'

    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def num2buttonclick(self):
        self.wd.find_element_by_xpath("xpath=//*[@text='NUM 2']").click()
        self.wd.find_element_by_xpath("xpath=//*[@text='NUM 1']").click()

    # This method connects to bluetooth device and enables the greyed out buttons
    def enable_grey_buttons(self):
        self.wd.swipe(603, 546, 603, -53, 1349)
        self.wd.swipe(603, 1146, 610, 5978, 3738)
        self.wd.find_element_by_xpath("xpath=//*[@text='START SCAN']").click()
        self.wd.find_element_by_xpath("xpath=//*[@text='Contour7830H5779094 (B0:91:22:FF:53:ED)']").click()
        self.wd.find_element_by_xpath("xpath=//*[@text='CONNECT']").click()

    # This method tests random buttons on the app
    def buttontest(self):
        self.wd.find_element_by_xpath("xpath=//*[@text='TEST CACHE']").click()
        self.wd.swipe(332, 1032, 332, 582, 682)
        self.wd.swipe(499, 1046, 496, 146, 680)
        self.wd.swipe(467, 1660, 467, 2260, 636)
        self.wd.find_element_by_xpath("xpath=//*[@text='RETRIEVE NEW']").click()
        self.wd.swipe(239, 1946, 239, 2846, 791)
        self.wd.find_element_by_xpath("xpath=//*[@text='RETRIEVE NEWEST']").click()
        self.wd.swipe(228, 2214, 224, 3110, 831)
        self.wd.find_element_by_xpath("xpath=//*[@text='RETRIEVE FROM SEQ. #']").click()
        self.wd.swipe(264, 2253, 264, 3153, 675)
        WebDriverWait(self.wd, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@text="CLEAR CACHE"]')))
        self.wd.find_element_by_xpath("xpath=//*[@text='CLEAR CACHE']").click()
        self.wd.swipe(696, 1967, 696, 2867, 709)
        self.wd.find_element_by_xpath("xpath=//*[@text='RETRIEVE ALL']").click()
        self.wd.swipe(782, 2053, 782, 2949, 678)
        self.wd.find_element_by_xpath("xpath=//*[@text='RETRIEVE OLDEST']").click()
        self.wd.swipe(814, 2121, 814, 3021, 720)
        self.wd.find_element_by_xpath("xpath=//*[@text='RETRIEVE SEQ. #']").click()
        self.wd.swipe(578, 1778, 578, 2678, 720)
        self.wd.swipe(578, 1778, 578, 1928, 582)
        self.wd.swipe(578, 1778, 578, 2528, 762)
        self.wd.swipe(578, 1178, 578, 578, 650)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET FEATURES']").click()
        self.wd.swipe(710, 1732, 703, 2474, 689)
        self.wd.find_element_by_xpath("xpath=//*[@text='SHOW DEVICE INFO']").click()
        self.wd.swipe(496, 1646, 496, 1796, 586)
        self.wd.swipe(235, 996, 235, 696, 801)

    # This mehthod crashes the app
    def lilly_app_crash(self):
        self.wd.find_element_by_xpath("xpath=//*[@text='INIT WITH MAC']").click()

    def enter_sequence_number(self):
        self.wd.swipe(332, 514, 332, -85, 669)
        self.wd.swipe(332, 514, 332, 214, 617)
        self.wd.swipe(457, 1282, 457, 982, 627)
        self.wd.find_element_by_xpath("xpath=//*[@id='sequence_number_edit_text']").click()
        self.wd.find_element_by_xpath(
            "xpath=//*[@class='android.widget.LinearLayout' and ./*[@class='android.widget.FrameLayout' and ./*[@id='decor_content_parent']]]").click()
        self.wd.find_element_by_xpath("xpath=//*[@id='keyboardView']").click()
        self.wd.find_element_by_xpath("xpath=//*[@id='keyboardView']").click()

    def nav1(self):
        self.wd.swipe(803, 849, 799, 285, 737)
        self.wd.find_element_by_xpath("xpath=//*[@text='SAVE STATE']").click()
        self.wd.find_element_by_xpath("xpath=//*[@text='RESTORE STATE']").click()
        self.wd.find_element_by_xpath("xpath=//*[@text='GET CURRENT TIME']").click()
        self.wd.swipe(328, 1682, 328, 2432, 620)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET BATTERY LEVEL']").click()
        self.wd.swipe(785, 1685, 785, 2585, 674)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET LOCAL TIME INFO']").click()
        self.wd.swipe(407, 1835, 403, 2882, 706)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET REF TIME INFO']").click()
        self.wd.swipe(807, 2446, 803, 2896, 626)

    def nav2(self):
        self.wd.swipe(746, 874, 746, 132, 677)
        self.wd.swipe(746, 899, 746, 299, 771)
        self.wd.swipe(746, 899, 746, 0, 663)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET MODEL #']").click()
        self.wd.swipe(289, 1242, 289, 492, 670)
        self.wd.swipe(296, 1835, 299, 2882, 725)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET MAN. NAME']").click()
        self.wd.swipe(842, 1824, 842, 2871, 766)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET SERIAL #']").click()
        self.wd.swipe(485, 1907, 489, 2807, 693)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET HW REV']").click()
        self.wd.swipe(846, 1935, 849, 2835, 701)

    def nav3(self):

        self.wd.swipe(921, 1332, 921, 2225, 783)
        self.wd.swipe(921, 717, 921, -32, 673)
        self.wd.swipe(928, 721, 928, -478, 729)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET FW REV']").click()
        self.wd.swipe(603, 1064, 603, 21, 736)
        self.wd.swipe(603, 1689, 603, 2589, 694)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET SW REV']").click()
        self.wd.swipe(864, 1521, 864, 2571, 1102)

    def nav4(self):
        self.wd.swipe(753, 610, 753, -435, 728)
        self.wd.swipe(721, 1100, 721, 1999, 635)
        self.wd.swipe(742, 1021, 742, 1621, 644)
        self.wd.swipe(728, 535, 728, -210, 643)
        self.wd.swipe(728, 539, 728, -1410, 1037)
        self.wd.swipe(728, 542, 728, -657, 709)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET SYS ID']").click()
        self.wd.swipe(396, 2024, 396, 3074, 680)
        self.wd.find_element_by_xpath("xpath=//*[@text='GET PNP ID']").click()
        self.wd.swipe(671, 1917, 671, 2967, 709)


# Call Functions To instantiate class methods
s = lillyApp()

s.num2buttonclick()
s.enable_grey_buttons()
s.buttontest()
# s.lilly_app_crash()
# s.enter_sequence_number()
# s.nav1()
# s.nav2()
# s.nav3()
# s.nav4()
