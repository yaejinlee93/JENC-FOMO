from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #one-time configuration and initialization

    def __call__(self, request):
        #GET FROM DATABASE
        product_ids = []
        request.last_five = []
        if request.session.get('something') is not None:
            product_ids = request.session.get('something')

        for item in product_ids:
            request.last_five.append(cmod.Product.objects.get(id = item))

        request.new_product = None;

        #GO TO THE VIEW
        response = self.get_response(request)

        if request.new_product in request.last_five:
            request.last_five.remove(request.new_product)
        request.last_five.insert(0,request.new_product)

        if len(request.last_five) > 6:
            request.last_five = request.last_five[0:6]

        updated_list = []
        #SAVE TO DATABASE
        for item in request.last_five:
            if item is not None:
                updated_list.append(item.id)

        request.session['something'] = updated_list

        return response
