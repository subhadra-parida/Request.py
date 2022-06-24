import requests
import os
import json
from requests.api import options,request
x=requests.get("http://saral.navgurukul.org/api/courses")
y=x.json()
print(y)

