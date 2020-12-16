from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
import datetime

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts, 'user':request.user})
	
def post_create(request):
	if request.method == 'POST':
		post_data = request.POST
		login_user = request.user
		
		data = Post(author=login_user,title=post_data.get('title'),text=post_data.get('text'),published_date=datetime.datetime.now())
		data.save()
	return redirect('post')
	
def post_update(request,pk):
	if request.method == 'POST':
		post_data = request.POST
		login_user = request.user
		
		nowPost = Post.objects.get(id=pk)
		if nowPost.author != login_user:
			return redirect( 'post' )
		else:
			nowPost.title=post_data.get('title')
			nowPost.text=post_data.get('text')
			nowPost.save()
			return redirect( 'post' )
	else:
		nowPost = Post.objects.get(id=pk)
		return render( request, 'blog/post_update.html',{'post':nowPost})

def post_delete(request,pk):
	nowPost = Post.objects.get(id=pk)
	nowPost.delete()
	return redirect( 'post' )