# 使用原有DB產生model
python manage.py inspectdb --database rmotelog > db1model.py
# 將新增的class copy 到原本的model.py
'''
model 中，managed = False表示只建管理用資料，不在default db建table
class Meta:
        managed = False
'''


# 產生migration script
python manage.py makemigrations
# 於admin package 中產生相對印的權限
python manage.py migrate  
