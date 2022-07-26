class Handler:
    def __init__(self, methods):
        self.methods = methods
        self.default_methods = ('GET', 'POST')
    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if request.get('method', 'GET') in self.methods and request.get('method', 'GET') == 'POST':
                return self.post(func, request)
            elif request.get('method', 'GET') in self.methods and request.get('method', 'GET') == 'GET':
                return self.get(func, request)
        return wrapper
    def get(self,func, request):
        result = func(request)
        return f'{request.get("method", "GET")}: {result}' 
    def post(self,func, request):
        result = func(request)
        return f'POST: {result}' 
@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Dzhan"
