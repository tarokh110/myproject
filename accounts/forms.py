from django import forms
from django.db import models
from django.core import validators
from accounts.models import user , books




class Newuser(forms.ModelForm):
    class Meta():
        model = user

        fields = ('last_name','password')




















#
# def Check_name(value):
#     if value[0].lower != 'z':
#         raise forms.ValidationError('Name mustr start with z')
#
#
# class fromname(forms.Form):
#     name = forms.CharField(validators=[Check_name])
#     email = forms.EmailField()
#     password = forms.PasswordInput()
#
#     #baraye Bot ke gir bendazim
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators= [validators.MaxLengthValidator(0)])
#
#     def clean(self):
#         all_clean_data = super().clean()
#         password = all_clean_data['password']
#         password2 = all_clean_data['password2']
#         if password != password2 :
#             raise forms.ValidationError('NOT verify passwords')