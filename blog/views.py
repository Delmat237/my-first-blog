from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def article(request,numero_article):
    if numero_article in ["1","1","2"]:
        return render(request, f'blog/article_0{numero_article}.html')
    
    return render(request, 'blog/article_not_found.html')
