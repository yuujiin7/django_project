from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
	# return HttpResponse("<h1>Hello, world. You're at the blog home.</h1>")
	context = {
		'posts': Post.objects.all()


	}
 
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html' , {'title': 'About'})