from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

@view_function
def fix_html(x):
    x = x.replace("&","&amp;")
    x = x.replace("<","&lt;")
    x = x.replace(">","&gt;")
    return x

@view_function
def process_request(request, prod:cmod.Product=None):

    product_id = prod.id
    product_name = fix_html(prod.name)

    request.new_product = prod
    if prod in request.last_five:
        request.last_five.remove(prod)
    request.last_five.insert(0, prod)

    if len(request.last_five) > 6:
        # request.last_five.remove(request.last_five[:-1])
        request.last_five = request.last_five[0:6]

    context = {
        'product':prod,
        'product_id':product_id,
        'product_name':product_name,
    }
    return request.dmp.render('detail.html', context)
