from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index_defined_in_view(request):
    articles = Article.objects.all()
    
    articles_len_over_10 = []
    for a in articles : 
        if a.len() > 10:
            articles_len_over_10.append(a)

    return render(request, 'index.html', {'articles_i_will_use_in_html':articles_len_over_10})


def detail_defined_in_view(request, pk_of_the_article_that_i_clicked):
    article = Article.objects.get(pk=pk_of_the_article_that_i_clicked)
    return render(request, 'detail.html', {'a_article_i_will_use_in_html' : article})
    
def new_defined_in_view(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail_i_will_use_in_html', pk_of_the_article_that_i_clicked=new_article.pk)
    else:
        return render(request, 'new.html')