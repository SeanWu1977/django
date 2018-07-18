# The app should contain a templatetags directory, at the same level as models.py, views.py, etc. 
# If this doesn’t already exist, create it
# don’t forget the __init__.py file to ensure the directory is treated as a Python package.
  


  
# in directory "templatetags", create xxx.py

# xxx.py
from django import template

register = template.Library()

@register.filter
def price(value):
    return value/100



# in html 
{% load xxx %}
{% value|price%}
