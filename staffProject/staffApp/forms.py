from django import forms
from django.core import validators
from staffApp.models import MetaUser


class NewParticipantForm(forms.ModelForm):
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


# def check_for_z(value):
#    if value[0].lower() == "z":
#        raise forms.ValidationError("!!!KAZAP DETECTED!!!")
# class FormName(forms.Form):
#    name = forms.CharField(validators=[check_for_z])

class FormName(forms.Form):
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

#    def clean_botcatcher(self):
#        botcatcher = self.cleaned_data['botcatcher']
#        if len(botcatcher):
#           raise forms.ValidationError("GOTCHA BOT!")
#        return botcatcher
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   validators=[validators.MaxLengthValidator(0)]
