from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from django.contrib.auth.models import User


# posts = Post.objects.all()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # template_name = 'post_form.html'
    # success_url = reverse_lazy('blog:blog_home_page')   using "get_absolute_url" in models.py instead

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # template_name = 'post_form.html'  will use the same template as the create view!
    success_url = reverse_lazy('blog:blog_home_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    ordering = ['-date_created']
    paginate_by = 2  # change to higher number as needed


class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_posts.html'
    paginate_by = 2  # change to higher number as needed

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog_home_page')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about_page(request):
    context = {'title': 'About page'}
    template = 'blog/about.html'
    return render(request, template, context)