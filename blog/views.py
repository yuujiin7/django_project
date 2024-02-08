from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
@login_required
def home(request):
	# return HttpResponse("<h1>Hello, world. You're at the blog home.</h1>")
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)



class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(UpdateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_confirm_delete.html'
	success_url = '/'
	# success_url = reverse_lazy('blog-home')
 
 
	
def about(request):
	return render(request, 'blog/about.html' , {'title': 'About'})


