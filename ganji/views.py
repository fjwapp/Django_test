from django.shortcuts import render,redirect
from ganji.models import ArtiInfo,Content,Comment
from django.core.paginator import Paginator
from django import forms
# Create your views here.

class CommnetForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField()



def index(request):
    limit = 4
    arti = ArtiInfo.objects[:20]
    paginator = Paginator(arti,limit)
    page = request.GET.get('page',1)
    loaded = paginator.page(page)
    context = {
        'ArtiInfo':loaded
    }


    return render(request,'index.html',context)



def blog(request):
    return render(request,'blog.html')

def index_semantic(request):
    limit = 3
    arti = ArtiInfo.objects[:1]
    paginator = Paginator(arti, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    context = {
        'ArtiInfo': loaded
    }
    return render(request,'index_semantic.html',context)

def charts(request):
    limit = 3
    arti = ArtiInfo.objects[:1]
    paginator = Paginator(arti, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    context = {
        'ArtiInfo': loaded
    }
    return render(request,'charts.html',context)

def My_Blog(request):
    content_list = {}


    if request.method == 'POST':
        form_list = CommnetForm(request.POST)
        print(form_list)
        if form_list.is_valid():
            name = form_list.cleaned_data['name']
            comment = form_list.cleaned_data['comment']

            c = Comment(name=name,comment=comment,)
            c.save()
            return redirect(to='My_Blog')
    else:
        form_list = CommnetForm
    blog_list= Content.objects.all()
    comment_list = Comment.objects.all()
    content_list['blog_list'] = blog_list
    content_list['comment_list']= comment_list
    content_list['form_list'] = form_list
    blog_page = render(request, 'My_Blog.html', content_list)
    return blog_page