#!/usr/bin/python
import datetime, requests, json, time, os
output=open(os.path.join(os.path.expanduser('~'), "Desktop/TodaySCUT.txt"), "w+")
output.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ "\n")
headers={'Host':'jw.scut.edu.cn', 'Origin':'http://jw.scut.edu.cn', 'Referer':'http://jw.scut.edu.cn/dist/', 'content-type':'application/json, text/plain, */*', 'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4389.82 Safari/537.36'}
data=json.dumps({'pageNo':'1', 'pageSize': '10', 'tag':'0', 'category':'0'})
file=requests.post(url="http://jw.scut.edu.cn/zhinan/jw/api/v2/findInformNotice.do", data=data, headers=headers).json()
time.sleep(2)
for i in range(len(file["data"]["list"])):
    output.write(file["data"]["list"][i]["createDate"])
    output.write("  ")
    output.write(file["data"]["list"][i]["title"])
    output.write('\n')
output.close()
print("OK!")