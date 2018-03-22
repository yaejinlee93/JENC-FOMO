from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod

def fix_html(x):
    x = x.replace("&","&amp;")
    x = x.replace("<","&lt;")
    x = x.replace(">","&gt;")
    return x

@view_function
def process_request(request,prod:cmod.Product=None):
    #utc_time = datetime.utcnow()
    product_name = fix_html(prod.name)

    #add the current product to the last_five list
    #request.last_five.append(prod)
    request.new_product = prod

    context = {
        # list of categories
        'product_name' : product_name,
        'product' : prod,
        'category_id' : prod.category.id,
    }
    return request.dmp.render('detail.html', context)
