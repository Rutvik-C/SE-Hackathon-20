from django import forms
from .models import rate
from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class Rate(forms.ModelForm):
    class Meta:
        model = rate
        fields = "__all__"
        widgets = {'ratings': forms.NumberInput(attrs={'class': 'Stars'})}
        labels = {'ratings': 'ratings /5'}
        exclude = ('user',)
