from django import forms
from Authority.models import otherDetails,problem
from django.contrib.auth.models import User

class Registerdetail(forms.ModelForm):
    class Meta:
        model=otherDetails
        fields = "__all__"
        exclude = ('user','choice')

class Food(forms.ModelForm):
    class Meta:
        date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
        model=problem
        fields = "__all__"
        exclude = ('user','otherDetails','city','created_on','images',)