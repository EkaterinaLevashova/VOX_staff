from django import forms
from django.core import validators
from staffApp.models import MetaUser
from staffApp.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class NewParticipantForm(forms.ModelForm):
    """INDEX.HTML FORM"""
    class Meta:
        model = MetaUser
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "myField",
                'placeholder': "Enter your full name:"
            }),
            'email': forms.TextInput(attrs={
                'class': "myField",
                'placeholder': "Enter your email:"
            }),
        }


class FormName(forms.Form):
    """RELATIVE.HTML FORM"""
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "myField"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "myField"}))
    verify_email = forms.EmailField(widget=forms.TextInput(attrs={'class': "myField",
                                                                  'placeholder': "Enter your email again"}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': "myField"}))

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get('email')
        vmail = all_clean_data.get('verify_email')

        if email != vmail:
            print("Make SURE Emails MATCH")
            raise forms.ValidationError("Make SURE Emails MATCH")
