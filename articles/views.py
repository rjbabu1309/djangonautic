#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

@login_required(login_url="/accounts/login/")
def article_delete(request, title):
    articles = Article.objects.all().order_by('date')
    try:
        article = Article.objects.get(title=title)
        article.delete()
    except article.DoesNotExist:
        return redirect('articles:list')
    #except Exception as e:
        #return HttpResponse("error")
        #return redirect('/')
    return render(request, 'articles/article_list.html', {'articles': articles})

def user_detail(request, author):
    art = Article.objects.filter(author=request.user)
    print(request.user.username)
    #a = Article.objects.all().get(author=request.user)
    return render(request, 'articles/text.html', {'err': art})
