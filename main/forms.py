from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'birthday', 'gender', 'email', 'phone_number', 'faculty', 'course', 'image', 'i_va_ii',
                  'temir_daftar', 'yetim']
