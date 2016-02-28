# I hate how it requires me to learn stuff again and again, but well, let's do this
from django import forms


class FileForm(forms.Form):
    file = forms.FileField(label="File: ")
    # extremely long file lol
