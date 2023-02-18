```
pip3 install -r requirements.txt
uvicorn main:app --reload 
```

例
```
curl localhost:8000/?v={videoid}
>>{video:https://~~~~~,audio:https://~~~~~}
```
videoidは"https://youtube.com/watch?v={ここの部分}"

