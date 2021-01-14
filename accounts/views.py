from django.shortcuts import render, redirect
from django.contrib import messages
#from . import forms
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request, 'invalid credential')
			return redirect('login')
	else:
#		messages.info(request, '')
		return render(request, 'accounts/login.html')

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		if password == confirm_password:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'User Name Already exists')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'Email Already exists')
				return redirect('register')
			else:
				user = User.objects.create_user(first_name=first_name,last_name=last_name, username=username,email=email, password=password)
				user.save();
				print('User created')
				return redirect('login')
		else:
			messages.info(request, 'Password does not match')
			return redirect('register')
		return redirect('/')
	else:
		return render(request, 'accounts/register.html')

def logout(request):
	auth.logout(request)
	return redirect('/')
def profile(request):
	return render(request, 'accounts/profile.html')





'''	form = forms.RegistrationForm()
	if request.method == 'POST':
		form = forms.RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['user_name'],email=form.cleaned_data['email'])
			user.save();
			print('User created')
		else:
			print('user not created')
			return redirect('')
	return render(request, 'accounts/register.html', {'form':form})'''
