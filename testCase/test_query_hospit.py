import unittest
from business_common.api_demo import ApiDemo
from common.read_yml import ReadYaml
from copy import deepcopy
from common.custom_logs import info_log,log_method_call,log_class_methods
from parameterized import parameterized

@log_class_methods
class QueryHospitalApi(unittest.TestCase):
    """查询医院接口"""
    env_config = ReadYaml().env_yaml("config.yml")
    api_config = ReadYaml().api_yaml("QueryHosptitalApi/api_data.yml")
    hosts = env_config["hosts"]
    token = env_config["token"]
    # print(token)
    user2_token = env_config["token1"]
    # print(token)
    path = "/apis/diagnosis/reverse_prescription/ih_hospital"
    re_body_base = {
        "pageNum": 1,
        "pageSize": 10
    }
    url = hosts + path


    def testCase01_Queryhospital(self):
        """查询医院 主流程"""
        re_body = deepcopy(self.re_body_base)
        headers = {"token": self.token}
        res = ApiDemo().get_api(self.url,re_body,headers)
        self.assertTrue(res.status_code == 200)

    @parameterized.expand(api_config["option_key"])
    def testCase02_option_key(self,dic):
        """查询医院 选填项检验"""
        re_body = deepcopy(self.re_body_base)
        re_body.pop(dic["key"])
        headers = {"token": self.token}
        res = ApiDemo().get_api(self.url,re_body,headers)
        self.assertTrue(res.status_code == dic["code"])


    def testCase03_token_failure(self):
        """查询医院 登录token失效"""
        re_body = {
            "pageNum": 1,
            "pageSize": 10
        }
        headers = {"token": self.user2_token}
        res = ApiDemo().get_api(self.url,re_body,headers)
        self.assertTrue(res.status_code == 401,msg="token失效，请重新登录")