from django.core.paginator import Paginator
from django.shortcuts import render

from . models import *

# Create your views here.


def blog(request):
    category = Category.objects.all()  
    article = Article.objects.all()     
    instagram = Instagram.objects.all()
    tag = Tag.objects.all()
    newsletter = Newsletter.objects.all()  

    paginator = Paginator(article, 4) # Show 25 articles per page
    page = request.GET.get('page')
    article = paginator.get_page(page)

    context = { "category": category, "article": article, "instagram": instagram, "tag": tag, "newsletter": newsletter,}
    return render(request, 'pages/blog.html', context)

    # context = {
    #     'category': Category.objects.all(),
    #     'article': Article.objects.all(),
    #     'instagram': Instagram.objects.all(),
    #     'tag': Tag.objects.all(),
    #     'newsletter': Newsletter.objects.all(),
    # }
    


def singleblog(request, id):
    article = Article.objects.get(pk=id)    
    instagram = Instagram.objects.all()
    tag = Tag.objects.all()
    comment = Comment.objects.all()

    form = Comment()
    if request.method == "POST":
         form = Comment(request.POST)
         if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"],
                article=article,
            )
            comment.save()

    context = { "articles": article, "instagram": instagram, "tag": tag, "comment": comment, "form": form}
    return render(request, 'pages/single-blog.html', context)




