from fastapi import FastAPI
from yt_dlp import YoutubeDL
import sys
import subprocess

app = FastAPI()


@app.get("/")
def read_item(v: str = None):
    videoid = v
    print(videoid)
    cmd = 'yt-dlp -g "https://www.youtube.com/watch?v="'+videoid
    process = (subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')
    return {"video": process.splitlines()[0],"audio":process.splitlines()[1]}
