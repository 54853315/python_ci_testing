#!/usr/bin/env python

import unittest,requests,sys,json
import function.common as common

# API域名
HOST = "https://domain/api/backend/"

## 类名的命名规则不限
class Test(unittest.TestCase):
    def setUp(self):
        # 版本检测
        python_version = sys.version_info[0]
        if(python_version !=3):
            print("本系统依赖于python3，您的版本过低，goodbye！")
            exit()

    def test_001_requirement(self):

        """需求提交"""
        
        # 拼写当前test请求的api地址
        api = HOST+'/requirement'
        # 拼装要提交的数据
        data = {'name':common.make_people_name(),'wechatid':'crazyphper','description':'不要问我叫什么,也不要问我是谁,我只是一个学生,正在虔诚的铺建自己的未来……我是一位建筑师,我打造自己的知识；我是一位画家,我描绘自己的未来；我是一位探险者,我追求一切的未知……我不愿留名于世,因为我只有一个名字——中国人.是的,我是中国人,我是祖国的栋梁,我承担着'}
        headers = {'Content-Type':'application/json'}
        data = json.dumps(data)
        r=requests.post(api,data = data,headers = headers)
        self.assertEqual(r.status_code,200)
        # print(r.text)

    def test_002_banner(self):
        """请求幻灯片"""
        
        api = HOST+'/banner'
        r=requests.get(api)
        self.assertEqual(r.status_code,200)

    def test_003_case(self):
        """请求案例列表"""

        api = HOST+'/case'
        data = {'page':1,'page_size':5}
        r=requests.get(api,data = data)
        self.assertEqual(r.status_code,200)


# 最后一定要有这一段代码
if __name__ == '__main__':
    unittest.main()