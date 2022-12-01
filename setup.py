#!/usr/python


import os
from aocd import get_data
import urllib3
urllib3.disable_warnings()

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

day = "1"
os.makedirs(day,exist_ok= True)

aa = get_data(session="53616c7465645f5f62fd893352d8b9c786c3cfb8c55e2f767fae44016b1274b91a2422a4bcf035087f4b503889f3c43df2354f5995b697fc8684faae7379b23e",day=1,year=2022)

print(aa)



