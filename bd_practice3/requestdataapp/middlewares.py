from datetime import timedelta, datetime

from django.http import HttpResponse


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


# class Anti_spam:
#     def __init__(self, get_response):
#         self.users_dict = dict()  # {"127.0.0.1": {"first_request": time, "request_counter": 1}}
#         self.get_response = get_response
#         self.time_threshold = timedelta(seconds=10)
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         user_ip = request.META.get('REMOTE_ADDR')
#
#         if user_ip in self.users_dict:
#             last_request_time = self.users_dict[user_ip]
#             time_passed = datetime.now() - last_request_time
#
#             if time_passed < self.time_threshold:
#                 return HttpResponse("Слишком много запросов. Попробуйте позже.", status=429)
#         else:
#             self.users_dict[user_ip] = datetime.now()
#
#         return response


class Anti_spam:
    def __init__(self, get_response):
        self.users_dict = dict()  # {"127.0.0.1": {"first_request": time, "request_counter": 1}}
        self.get_response = get_response
        self.time_threshold = timedelta(seconds=10)

    def __call__(self, request):
        response = self.get_response(request)
        user_ip = request.META.get("REMOTE_ADDR")

        if user_ip in self.users_dict:
            self.users_dict[user_ip]["request_counter"] += 1
            first_request_time = self.users_dict[user_ip]["first_request"]
            time_passed = datetime.now() - first_request_time
            print(time_passed)

            if time_passed > self.time_threshold:
                self.users_dict[user_ip]["first_request"] = datetime.now()
                self.users_dict[user_ip]["request_counter"] = 1

            if self.users_dict[user_ip]["request_counter"] >= 5:
                return HttpResponse("Слишком много запросов. Попробуйте позже.", status=429)

        else:
            self.users_dict[user_ip] = dict()
            self.users_dict[user_ip]["first_request"] = datetime.now()
            self.users_dict[user_ip]["request_counter"] = 1

        return response
