from django import forms
from django.core.files.uploadhandler import InMemoryUploadedFile
from django.core.exceptions import ValidationError


class UserBIOform(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    age = forms.IntegerField(label="Your age", min_value=1, max_value=100)
    about = forms.CharField(label="Biography", widget=forms.Textarea, max_length=500)


def validate_file_name(file):
    if file.name and "virus" in file.name:
        raise ValidationError("File name inccorect")


class UploadForm(forms.Form):
    file = forms.FileField(validators=[validate_file_name])
