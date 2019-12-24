from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .forms import BlogForm

from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib import messages


from django.urls import reverse_lazy


# Create your views here.
class BlogListView(ListView):
    model=Blog
    context_object_name="blogs"  #テンプレートに渡すオブジェクト名を変更

    paginate_by=6  #ページネーションの表示数を指定

class BlogDetailView(DetailView):
    model=Blog
    context_object_name="blog"
    
class BlogCreateView(LoginRequiredMixin,CreateView):
    model=Blog
    form_class=BlogForm
    template_name="blog/blog_create_form.html"

    success_url=reverse_lazy("index")
    login_url="/login"

    def form_valid(self,form):  #保存に成功した時にメッセージを表示する
        messages.success(self.request,"保存しました")
        return super().form_valid(form)
    
    def form_invalid(self,form): #保存に失敗した時にメッセージを表示する
        messages.error(self.request,"保存に失敗しました")
        return super().form_invalid(form)



class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model=Blog
    form_class=BlogForm

    login_url="/login"

    template_name="blog/blog_update_form.html"


    def form_valid(self,form):  #保存に成功した時にメッセージを表示する
        messages.success(self.request,"更新しました")
        return super().form_valid(form)
    
    def form_invalid(self,form): #保存に失敗した時にメッセージを表示する
        messages.error(self.request,"更新に失敗しました")
        return super().form_invalid(form)


    def get_success_url(self):
        blog_pk=self.kwargs['pk']
        url=reverse_lazy("detail",kwargs={'pk':blog_pk})

        return url



class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model=Blog
    success_url=reverse_lazy("index")

    login_url="/login"

    def delete(self,request,*args ,**kwargs):
        messages.success(self.request,"削除しました")

        return super().delete(request,*args,**kwargs)

