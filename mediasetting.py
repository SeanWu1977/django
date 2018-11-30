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
