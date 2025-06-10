"""
マイクラで半自動的にハードコア用ワールドを建て直す
"""

import argparse
import shutil
import subprocess
import time
from pathlib import Path


eula_file = "eula.txt"
exe_file = "server.jar"
prop_file = "server.properties"

parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="サーバーパス")
args = parser.parse_args()

# ディレクトリ確認
dir = args.dir
cnt = 0
for obj in Path(dir).glob("*"):
    if obj.name == eula_file:
        cnt += 1
    elif obj.name == exe_file:
        cnt += 1
    elif obj.name == prop_file:
        cnt += 1
if cnt != 3:
    print("DANGER: PROBABLY NOT MINECRAFT SERVER DIRECTORY")
    exit()

# サーバファイル群削除
for obj in Path(dir).glob("*"):
    if obj.name == exe_file:
        continue
    if obj.is_dir():
        shutil.rmtree(str(obj))
    else:
        obj.unlink()

# サーバ準備
server = Path(dir) / Path(exe_file)
res = subprocess.run(str(server), shell=True, cwd=dir)
time.sleep(0.3)

# 同意書ファイル書き換え
with (Path(dir) / Path(eula_file)).open(mode="r") as f:
    contents = f.readlines()
contents[-1] = "eula=true\n"  # 同意する
with (Path(dir) / Path(eula_file)).open(mode="w") as f:
    f.writelines(contents)

# サーバ設定ファイル書き換え
with (Path(dir) / Path(prop_file)).open(mode="r") as f:
    contents = f.readlines()
for i, cont in enumerate(contents):
    if "hardcore" in cont:
        contents[i] = "hardcore=true\n"  # ハードコア設定
        break
with (Path(dir) / Path(prop_file)).open(mode="w") as f:
    f.writelines(contents)
