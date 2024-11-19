from django import forms
# from naija_kitchen.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username or password.")
        self.cleaned_data['user'] = user
        return cleaned_data
