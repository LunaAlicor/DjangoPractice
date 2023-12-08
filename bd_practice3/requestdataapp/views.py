from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .forms import UserBIOform, UploadForm


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


def formstest(request):
    context = {
        "form": UserBIOform(),
    }
    return render(request, "requestdataapp/formstest.html", context=context)


def upload_tes(request):

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            my_file = form.cleaned_data["file"]

            # print(size)
            fs = FileSystemStorage()
            filename = fs.save(my_file.name, my_file)
            print(f"saved file {filename}")
        else:
            context = {"form": form}
            return render(request, "requestdataapp/upload.html", context=context)
    else:
        form = UploadForm()

    context = {
        "form": UploadForm()
    }
    return render(request, "requestdataapp/upload.html", context=context)
