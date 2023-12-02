def set_useragent_on_request_middleware(get_response):

    print("initial call")

    def middleware(request):
        print("before get_response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get_response")
        return response
    return middleware


class CountRequestmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exception_count = 0

    def __call__(self, request):
        self.requests_count += 1
        print(f"Request count: {self.requests_count}")
        response = self.get_response(request)
        self.responses_count += 1
        print(f"Responsens count: {self.responses_count}")
        return response

    def process_exception(self, request, exception: Exception):
        self.exception_count += 1
        print(f"Total exceptions: {self.exception_count}\nGot new exception: {exception}")
