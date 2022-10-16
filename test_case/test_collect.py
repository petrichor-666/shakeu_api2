'''

@File:test_collect.py
@Datetime:2022/10/16 16:42
@Author:wangt
@Desc:登录接口
'''

import requests
import unittest
import warnings
import logging
# 1. 注册
# data = {
#     'username': 'testwt111',
#     'password': '123456',
#     'repassword': '123456'
# }
# res = requests.post(host_url+'/user/register',data=data)
# print(res.text)
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.host_url = 'https://www.wanandroid.com'    # host_url
        self.session = requests.session()
        # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)

    def test01_login(self):
        """登录接口"""
        logging.info('test01_login')
        url = self.host_url+'/user/login'
        data = {
            'username': 'testwt111',
            'password': '123456'
        }
        res = self.session.post(url,data=data)
        self.dict_cookies = dict(res.cookies)       # 将cookiejar转为字典格式
        global cookies      # 将登录接口返回的cookies设为全局变量
        cookies={
            'loginUserName_wanandroid_com':self.dict_cookies['loginUserName_wanandroid_com'],
            'token_pass_wanandroid_com':self.dict_cookies['token_pass_wanandroid_com'],
            'JSESSIONID':self.dict_cookies['JSESSIONID'],
            'loginUserName':self.dict_cookies['loginUserName'],
            'token_pass':self.dict_cookies['token_pass']
        }
        # print(dict_cookies)
        json_data = res.json()
        self.assertEqual(json_data['data']['username'],'testwt111')

    def test02_collect_list(self):
        """收藏列表接口"""
        logging.info('test02_collect_list')
        # self.test01_login()     # 使用login用例中的方法
        url = self.host_url+'/lg/collect/list/0/json'
        res = self.session.get(url,cookies=cookies)
        json_data = res.json()
        self.assertEqual(json_data['data']['curPage'],1)
        # print(res.text)

    def test03_collect_article(self):
        """收藏文章接口"""
        logging.info('test03_collect_article')
        url = self.host_url+'/lg/collect/2804/json'
        res = self.session.post(url,cookies=cookies)
        json_data = res.json()
        self.assertEqual(json_data['errorCode'],0)
        # print(res.text)


if __name__ == '__main__':
    unittest.main()