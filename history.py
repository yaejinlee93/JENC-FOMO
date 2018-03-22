from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        id_list = request.session.get('id_list', [])
        try:
            id_list = request.session['id_list']
        except:
            id_list = []

        product_list = []
        if len(id_list) != 0:
            for pid in id_list:
                product_list.append(cmod.Product.objects.get(id = pid ))

        request.last_five = product_list
        print("hola")

        response = self.get_response(request)

        after_list = []
        print(request.last_five)
        for item in request.last_five:
            after_list.append(item.id)
            print(item.name)

        print('adios')
        request.session['id_list'] = after_list

        return response
