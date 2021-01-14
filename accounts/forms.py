from django import forms


class RegistrationForm(forms.Form):
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)
	user_name = forms.CharField(max_length=255)
	email = forms.EmailField()
	password = forms.PasswordInput()
	confirm_password = forms.CharField(max_length=255)
