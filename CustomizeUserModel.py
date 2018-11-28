# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
# Extending User Model Using a Custom Model Extending AbstractUser

# 要在還沒有db table時就要先執行，或是先把db table跟migration file刪除在執行 


# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    oid = models.CharField(db_column='O_ID', max_length=3, blank=True, null=True, verbose_name='Organization ID')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
# settings.py
AUTH_USER_MODEL = 'usblog.User'  # <<appname>>.User


# python manage.py makemigrations usblog
# python manage.py migrate usblog



#admin.py
from usblog.models import User as MyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            ('Customize', {'fields': ('oid',)}),
    )


admin.site.register(MyUser, MyUserAdmin)


