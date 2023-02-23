from fastapi import FastAPI
from fastapi.responses import JSONResponse
from yt_dlp import YoutubeDL
import sys
import subprocess

app = FastAPI()


@app.get("/")
def read_item(v: str = None):
    try:
        videoid = v
        cmd = 'yt-dlp -g "https://www.youtube.com/watch?v="'+videoid
        process = (subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')
        content = {"status":"Success","video": process.splitlines()[0],"audio":process.splitlines()[1]}
        headers = {"Access-Control-Allow-Origin": "*"}
        return JSONResponse(content=content, headers=headers)
    except:
        return {"status":"Failed"}