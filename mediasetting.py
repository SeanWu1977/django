atenams_nginx.conf


    # Django media
    location /media  {
        alias /home/aten/atenams/media;
        # atenams_uwsgi.ini中設定
        # chdir = /home/aten/atenams
        # 因此media只能放在這個路徑下
        # your Django project's media files - amend as required
    }


setting.py

MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#templates
<a href="/media/xls/a.xls">下載模板</a>


# 檔案名稱加解密
from django.core import signing
# 加密
value = signing.dumps(filename)
# 解密
org = signing.loads(value)


# 可以不限制在media下
from django.http import FileResponse  
def file_down(request):  
    from django.http import FileResponse
    from django.core import signing
    value = 'ImEueGxzIg:1gScoL:x4-KqHaxIUq7-zD6m0241g_pP8g'
    filename = signing.loads(value)
    dir = '<absolute path>'    
    full_name = '{}/{}'.format(dir,filename)
    file=open(full_name,'rb')
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="example.tar.gz"'  
    return response 
