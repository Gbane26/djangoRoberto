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
    
    email = request.POST.get('email')
    author = request.POST.get('author')
    emails = request.POST.get('email')
    website = request.POST.get('website')
    message = request.POST.get('message')
    
    if email is not None:
	    h = Newsletter(email=email)
	    h.save()

    if author is not None and emails is not None and website is not None and message is not None:
        me = Comment(author=author, email=emails, website=website, message=message, Article_id = article)
        me.save()

    

    context = { "articles": article, "instagram": instagram, "tag": tag, "comment": comment, "id":id}
    return render(request, 'pages/single-blog.html', context)




