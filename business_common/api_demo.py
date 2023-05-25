import requests
from common.custom_logs import info_log,error_log,warning_log

class ApiDemo:
    def get_api(self,url,re_body,headers):
        info_log(f"request body:{re_body}")
        info_log(f"request headers:{headers}")
        res = requests.get(url=url, params=re_body, headers=headers,timeout=10)
        info_log(f"response status_code:{res.status_code}")
        info_log(f"response res body:{res.text}")
        return res
