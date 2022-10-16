'''

@File:run.py.py
@Datetime:2022/10/17 0:05
@Author:wangt
@Desc:
'''
import unittest
from config.HTMLTestRunner import HTMLTestRunner
import time
import logging.config

CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

test_dir = 'test_case'
report_dir = './reports'

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+'test_report.html'

if __name__ == '__main__':
    with open(report_name, 'wb') as f:
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
        runner = HTMLTestRunner(title='API Test', description='practice', stream=f)
        logging.info('=============Start API Test=============')
        runner.run(discover)