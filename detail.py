from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
import math

@view_function
def fix_html(x):
    x = x.replace("&","&amp;")
    x = x.replace("<","&lt;")
    x = x.replace(">","&gt;")
    return x

@view_function
def process_request(request, product: cmod.Product=None):

    p_id = product.id
    p_name = fix_html(product.name)

    #don't add a second time
    for p in request.last_five:
        if product == p:
            request.last_five.remove(p)

    #remove if already in the list
    request.last_five.insert(0, product)

    #if leng > 6, remove last item
    if len(request.last_five) > 6:
        request.last_five.pop()

    context = {

    'product': product,
    'mainimg': product.image_url(),
    'listimgs': product.image_urls()

    }
    return request.dmp.render('detail.html', context)
