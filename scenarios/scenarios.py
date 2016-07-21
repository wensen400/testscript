# !/usr/bin/env python
# -*- coding: utf8 -*-

import unittest

from appium import webdriver
from ddt import ddt, data, unpack
from time import  sleep
import  codecs

from library.GetData import get_csv_data

@ddt
class TestScenario(unittest.TestCase):
    """ inheriting the TestCase class"""


    @classmethod
    def setUpClass(cls):
        """test preparation"""
        cls.desired_caps={}
        cls.desired_caps['platformName']='Android'
        cls.desired_caps['platformVersion']='4.3'
        cls.desired_caps['deviceName']='192.168.56.101:5555'
        cls.desired_caps['appPackage']='com.example.zhangjian.minibrowser2'
        cls.desired_caps['appActivity']='com.example.zhangjian.minibrowser2.MainActivity'
        cls.desired_caps["unicodeKeyboard"] = "True"
        cls.desired_caps["resetKeyboard"] = "True"
        #self.desired_caps["automationName"] = "Selendroid"
        cls.driver=webdriver.Remote('http://localhost:4723/wd/hub',cls.desired_caps)

    def setUp(self):
        print "case start"

    '''def setUp(self):
        """test preparation"""
        self.desired_caps={}
        self.desired_caps['platformName']='Android'
        self.desired_caps['platformVersion']='4.3'
        self.desired_caps['deviceName']='192.168.56.101:5555'
        self.desired_caps['appPackage']='com.example.zhangjian.minibrowser2'
        self.desired_caps['appActivity']='com.example.zhangjian.minibrowser2.MainActivity'
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        #self.desired_caps["automationName"] = "Selendroid"
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)'''

    @data(*get_csv_data('./data/data.csv'))
    @unpack
    def test_search(cls, target_url, search_value):
        """test case for scenario a"""
        elem = cls.driver.find_element_by_id('url')
        search_value = search_value.decode('unicode_escape')
        print search_value
        elem.send_keys(search_value)
        sleep(2)
        btn = cls.driver.find_element_by_id('searchbutton')
        btn.click()
        cls.assertTrue(True)

    @data(0, 0)
    def testNumber(cls, value):
        cls.assertTrue(value == 0)

    '''def tearDown(self):
        """clean up"""
        self.driver.quit()'''

    def tearDown(self):
        print "case stop"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()