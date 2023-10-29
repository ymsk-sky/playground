import os

from yt_dlp import YoutubeDL

OUT_PATH = "out"
os.makedirs(OUT_PATH, exist_ok=True)

options = {
    "outtmpl": OUT_PATH,
    "format": "bestvideo+bestauido/best",
}
ydl = YoutubeDL(options)

with open("urls") as f:
    lines = f.readlines()

ydl.download(lines)
