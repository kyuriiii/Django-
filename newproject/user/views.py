from django.shortcuts import render,redirect
from .models import User

# Create your views here.	
def register(request):
	if request.method == "POST" :
		userid = request.POST.get('userid')   
		username = request.POST.get('username')
		password = request.POST.get('password')
		gender = request.POST.get('gender')
		data = {}
		if not ( userid and username and password and gender):
			data['error'] = '빈칸입니다.'
			return render(request, 'user/register.html', data )
		else:
			user = User( userid=userid, username=username, password=password, gender=gender)
			user.save()
			return redirect('../main')
	else:
		return render(request, 'user/register.html')
		
def login(request):
	if request.method == "POST" :
		userid = request.POST.get('userid')
		password = request.POST.get('password')
		data = {}
		if not ( userid and password ):
			data['error'] = '빈칸입니다.'
			return render(request, 'user/login.html', data)
		else:
			user = User.objects.get(userid=userid)
			if user.password == password:
				request.session['user'] = userid
				return redirect('../main')
			else:
				data['error'] = '로그인실패.'
				return render(request, 'user/login.html', data)
	else:
		return render(request, 'user/login.html')

def logout(request):
	request.session.pop('user')
	return redirect('../main')
		
def main(request):
	data = {}
	user_id = request.session.get('user')
	if user_id:
		myinfo = User.objects.get(pk=user_id)
		data['session'] = myinfo.username
	else:
		data['session'] = '로그인해주세요'

	return render(request, 'user/main.html', data)