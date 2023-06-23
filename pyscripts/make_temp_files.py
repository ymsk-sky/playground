# -*- coding: utf-8 -*-
"""
タイムスタンプ付きファイルを作成
"""

import os

import cv2
import numpy as np

csv_path = "./tmp_csv/"
if not os.path.exists(csv_path):
    os.makedirs(csv_path, exist_ok=True)
img_path = "./tmp_img/"
if not os.path.exists(img_path):
    os.makedirs(img_path, exist_ok=True)

img = np.ones((100, 100), np.uint8) * 255

for month in range(1, 13):
    for day in range(1, 31):
        for hour in range(0, 24):
            for minute in range(0, 60, 10):
                ts = f"2023{month:02}{day:02}{hour:02}{minute:02}01"
                file_name = f"A-AAA_B-BBB01_{ts}.csv"
                _file = os.path.join(csv_path, file_name)
                with open(_file, "w", encoding="shift-jis") as f:
                    f.write("test1")
                    f.write("test2")
                _file = os.path.join(img_path, file_name.replace(".csv", ".jpg"))
                cv2.imwrite(_file, img)
