from .models import New
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger        

COUNT_BLOCKS_ON_PAGE = 10

def item(request, title):         
    current_new = New.objects.filter(url_name=title).first()
    return render(request, 'onesnews.html', {
        "current_new": current_new,
    })  
    
def main(request):      
    pub_date = ""    
    if request.GET:
        try:
            pub_date = request.GET["pub_date"]                
        except:
            pub_date = ""
    snews = New.objects.all()    
    if pub_date:
        snews = snews.filter(pub_date__icontains=pub_date)    
        
    paginator = Paginator(snews, COUNT_BLOCKS_ON_PAGE)     
    page = request.GET.get('page')        
    try:
        page = int(page)
    except:
        page = 1
    a = ""
    snews = ""
    pages=[]
    if page:
        try:
            snews = paginator.page(page)
        except EmptyPage:
            snews = paginator.page(paginator.num_pages)
            page = paginator.num_pages

        for i in range(page-2, page+3):
            try:
                a = paginator.page(i)
                pages.append(i)
            except:
                continue        
        if pages[-1] != paginator.num_pages:
            pages.append(paginator.num_pages)

        if pages[0] != 1:
            pages.insert(0, 1)
    else:
        pages = [1,2,3,4,5,paginator.num_pages]
        snews = paginator.page(1)

    return render(request, 'news.html', {
        'snews': snews,
        'pub_date': pub_date,       
        "pages": pages,
    })  


      

