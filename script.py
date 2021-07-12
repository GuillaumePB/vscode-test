import math
import os
import sys
import tkinter as tk

import requests

print(sys.version)
print(sys.executable)


def greet(who):
    test = "test"
    greeting = "hey"
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
