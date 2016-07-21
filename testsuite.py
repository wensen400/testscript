# !/usr/bin/env python
# -*- coding: utf8 -*-

import HTMLTestRunner
import time
import unittest

from library.SendReport import send_mail
from scenarios.scenarios import TestScenario

'''正常情况下'''
'''# load test cases 加载整个class
scenario = unittest.TestLoader().loadTestsFromTestCase(TestScenario)
# create test suite
test_suite = unittest.TestSuite([scenario])
# execute test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)

#加载一个class中一条具体的测试用例
test_suite.addTest(testPersonalCenter.MyTestCase('test_settingInMyCenter'))'''

'''生成测试报告'''
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# load test cases
scenario_a = unittest.TestLoader().loadTestsFromTestCase(TestScenario)
# create test suite
test_suite = unittest.TestSuite([scenario_a])
# declare report name
HtmlFile = "report/"+now + "HTMLtemplate.html"
#file handler
fp = file(HtmlFile, "wb")
#output report
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"搜狗测试报告", description=u"用例测试情况")
#run test
runner.run(test_suite)


'''发送测试报告'''
send_mail( ["zhangjian@sogou-inc.com"], "TestResult", HtmlFile)