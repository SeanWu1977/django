import urllib.request
local_filename, headers = urllib.request.urlretrieve('http://python.org/') #filename是隨機產生
html = open(local_filename)
html.close()

urllib.request.urlcleanup() # 清除所有暫存檔

local_filename --> 本機端的暫存檔路徑





local_filename, headers = urllib.request.urlretrieve('http://python.org/','temp123') #filename指定為temp123

local_filename, headers = urllib.request.urlretrieve('http://python.org/','temp123',cbk) #filename指定為temp123
# cbk : reporthook (A chunk number, the maximum size chunks are read in, the total size of the download)
# 可顯示下載百分比
def cbk(a,b,c):
  per=100.0*a*b/c  
    if per>100:  
       per=100  
    print ('{:.2f}%'.format(per)) 
