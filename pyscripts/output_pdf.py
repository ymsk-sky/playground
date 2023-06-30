# -*- coding: utf-8 -*-
"""
mdからpdf作成
"""

# from datetime import datetime
# import os

# import markdown


data = {
    "NAME": "ymsksky",
    "COLOR": "green",
    "GENDER": "man",
    "LOCAL": "Japan",
    "PROGRAM": "python"
}

with open("./template.md", "r", encoding="utf-8") as f:
    template = f.read()

for key in data:
    template = template.replace(f"%{key}%", data[key])

with open("./out.md", "w", encoding="utf-8") as f:
    f.write(template)
