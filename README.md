# rbl_analyser

This is a **python3** script that will get IP Address to query in some RBL's and return relevant information if it is listed.

## Requirements (Setup) and Usage

### Setup

- Python3 (_2.7 may have errors_)

import json
import os
import requests
import colorama
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError
from dotenv import load_dotenv
from colorama import Fore, Back, Style
colorama.init()

### Usage:

In order to use the script you will need an API key which is used for query in rbl hetrix tools. To get an api key, you need to create an account at: https://hetrixtools.com/register/

With the token in hand, you need to create an .env file, follow the instructions at: https://es.stackoverflow.com/questions/529724/como-ocultar-tokens-en-un-script-python-en-github

To run this script:

```
python check_rbl.py
```
  
 <img src="[http://url/image.png](https://github.com/fagner-fmlo/rbl_analyser/blob/adbddcffa04ea9049a0d4b458aef445ebae9d4c9/check_rbl.jpg)" style=" width:60px ; height:60px ">
 
 <div style="width:60px ; height:60px">
![Employee data]([/repository/assets/employee.png?](https://github.com/fagner-fmlo/rbl_analyser/blob/adbddcffa04ea9049a0d4b458aef445ebae9d4c9/check_rbl.jpg)
<div>
