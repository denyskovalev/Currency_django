from time import time
from currency.models import ResponseLog
from currency.utils import get_client_ip


class ResponseLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Return original response, and fix time start/end
        start = time()
        response = self.get_response(request)
        end = time()

        # Get request execution time
        response_time = start - end

        # Get request method
        request_method = str(request.method)

        # Get request params
        request_params = str(request.GET)

        # Get client ip
        ip_client = get_client_ip(request)

        # Get path
        path = str(request.path)

        ResponseLog.objects.create(response_time=response_time,
                                   request_method=request_method,
                                   query_params=request_params,
                                   ip_client=ip_client,
                                   path=path)

        return response
