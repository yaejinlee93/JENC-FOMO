from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # get the list of id's from the sessions
        prods = request.session.get('lastFive', [])
        request.last_five = []


        #convert product id's to list of product objects
        for item in prods:
            request.last_five.append(cmod.Product.objects.get(id=item))

        response = self.get_response(request)

        # save id's back to the session
        #convert request.last_five into a list of id's
        request.session['lastFive'] = []

        for item in request.last_five:
            request.session['lastFive'].append(item.id)

        return response
