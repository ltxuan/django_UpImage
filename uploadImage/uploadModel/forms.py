from django import forms

class UploadFileForm(forms.Form):
    image1 = forms.FileField()