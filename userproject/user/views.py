from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

def index(request):
	data = {}
	user_id = request.session.get('user')
	if user_id:
		myinfo = User.objects.get(pk=user_id)
		#return HttpResponse(myinfo.username)
		#user = request.session.get('user')
		data['session'] = myinfo.username
	else:
		data['session'] = '로그인해주세요'
		
	return render(request, 'user/index.html', data)
	#return HttpResponse('로그인해주세요')
	#data = {}
	#if request.session:
	#	user = request.session.get('user')
	#	data['session'] = user
	#else:
	#	data['session'] = '로그인해주세요.'
	#return render(request, 'user/index.html', data)
	
def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "POST":
        username = request.POST.get('username')   #딕셔너리형태
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        data = {} 
        if not (username and password and re_password) :
            data['error'] = "모든 값을 입력해야 합니다."
            # return redirect('./')
        else :
            if password != re_password :
                # return HttpResponse('비밀번호가 다릅니다.')
                data['error'] = '비밀번호가 다릅니다.'
            else :
                user = User(username=username, password=password)
                #make_password는 괄호 안에 들어온 문자열 암호화
                user.save()
                return redirect('../')
        return render(request, 'user/register.html', data)
    else:
        return render(request, 'user/register.html')
		
def login(request):
	data = {}
	
	if request.method == "POST":
		loginuser = request.POST.get('username')
		loginpw = request.POST.get('password')
		
		if not (loginuser and loginpw):
			data['error'] = "아이디와 비밀번호를 모두 입력해주세요."
		else :
			user = User.objects.get(username=loginuser)
			if check_password(loginpw, user.password):
				request.session['user'] = user.id
				return redirect('../')
			else:
				data['error'] = '비밀번호를 틀렸습니다.'
		return render(request, 'user/login.html', data)
	else:
		return render(request, 'user/login.html')
		
def check_password( loginpw, pw ):
	if loginpw==pw:
		return True
	else:
		return False
		
def logout(request):
	request.session.pop('user')
	return redirect('../')


def form(request):
	if request.method == "POST":
		post = request.POST
		data = {
			'name': post.get('name'),
			'gender':post.get('gender'),
			'birth_year':post.get('birth_year'),
			'birth_month':post.get('birth_month'),
			'birth_date':post.get('birth_date')
		}
		return render(request, 'user/receive.html', data)
	else:
		data = {
			'year' : range(1990,2020)
		}
		return render(request, 'user/form.html',data)

# Create your views here.

