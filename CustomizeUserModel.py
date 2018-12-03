# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
# Extending User Model Using a Custom Model Extending AbstractUser

# 要在還沒有db table時就要先執行，或是先把db table跟migration file刪除在執行 
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser


# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
class ATENUser(AbstractUser):
    oid = models.CharField(db_column='O_ID', max_length=3, blank=True, null=True,verbose_name='Organization ID')
    REQUIRED_FIELDS = ['oid','email']
    def __str__(self):
        return '{}({})'.format(self.username, self.email)
    
class ATENORG(models.Model):
    oid = models.CharField(db_column='O_ID', primary_key=True, max_length=3,verbose_name='Organization ID')  # Field name made lowercase.
    odesc = models.CharField(db_column='O_DESC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'ORGTABLE'
    def __str__(self):
        return self.oid # admin page 存檔時會用此回傳值    
    
# settings.py
AUTH_USER_MODEL = 'user.ATENUser'  # <<appname>>.User


# python manage.py makemigrations usblog
# python manage.py migrate usblog



#admin.py (org 下拉選單)
from django.contrib import admin
from user.models import ATENUser, ATENORG
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.forms import ModelChoiceField

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return '({}){}'.format(obj.oid , obj.odesc)

class ATENUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = ATENUser
    oid = MyModelChoiceField(queryset=ATENORG.objects.all(), label='Organization ID')


class ATENUserAdmin(UserAdmin):
    form = ATENUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            ('Customize', {'fields': ('oid',)}),
    )

class ORGAdmin(admin.ModelAdmin):
    pass

admin.site.register(ATENUser, ATENUserAdmin)
admin.site.register(ATENORG, ORGAdmin)



