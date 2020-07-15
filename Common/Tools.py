#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/6/24 15:03
# @Author: zhc

import os
import yaml

class ReadYaml:
    def __init__(self,filename):
        path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        self.filepath = path_ya+"/data/"+filename

    def get_yaml_data(self):
        with open(self.filepath, "r", encoding="utf-8")as f:

            return yaml.load(f)

if __name__ == '__main__':
    data = ReadYaml("login_data.yml").get_yaml_data()
    print(data)
