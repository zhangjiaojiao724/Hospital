import os
import sys
import yaml
from main import DIR, Environ


class ReadYaml(object):
    """读取环境层的配置"""
    @staticmethod
    def env_yaml(filename):
        with open((DIR + Environ)+"/"+filename, "r", encoding="utf-8")as f:
            # 调用load方法加载文件流
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def api_yaml(filename):
        with open((DIR + r"/data")+"/"+filename, "r", encoding="utf-8")as f:
            # 调用load方法加载文件流
            return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    main_data = ReadYaml().env_yaml("env.yml")  # 读取数据
    host = main_data['note_host']
    print(host)


