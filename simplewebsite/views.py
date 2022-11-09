from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# add root directory pages

# add home page or message
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
   # return HttpResponse("<h1>Just Home Page</h1>") # string of HTML code
    return render(request, "../templates/homepage.html", {})
    
    


#add about page
def about_view(request, *args, **kwargs): # *args, **kwargs
    return render(request,'../templates/about.html')
    

#add terms page
def terms_view(request, *args, **kwargs): # *args, **kwargs
    return render(request,'../templates/terms.html')
    
#add contact page
def contact_view(request, *args, **kwargs): # *args, **kwargs
    return render(request,'../templates/contact.html')
  

    
    


