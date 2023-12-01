from django.shortcuts import render


def hello_request(request):
    b = request.GET.get("b", "")
    a = request.GET.get("a", "")
    result = a + b
    context = {
        "a": a,
        "b": b,
        "result": result
    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)
