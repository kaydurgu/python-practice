class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods
    def get(self, request):
        if not type(request) is dict and not 'url' in request:
            raise TypeError('request не является словарем')
        return f'url: {request["url"]}'
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass

class DetailView(GenericView):
    def render_request(self, request, method):
        if not method in self.methods or 'url' not in request:
            raise TypeError('данный запрос не может быть выполнен')
        return self.__getattribute__(method.lower())(request)

# getattr -- when there is no attribute with this name 
# getattribute when there is a attribute with this name 

    