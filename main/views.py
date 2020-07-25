from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from contactform.models import ContactForm
from news.models import TrendingNews
from news.models import News
from cat.models import Cat
from subcat.models import Subcat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage #for import media file


# Create your views here.
#create function to send data
def home(request):
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcat = Subcat.objects.all()
    latestnews = News.objects.all().order_by('-pk')[:3]
    #popular news sorting by news count
    popnews = News.objects.all().order_by('-show')[:3]
    trending = TrendingNews.objects.all()

    return render(request, 'front/home.html',{'site':site, 'news':news, 'cat':cats, 'subcat':subcat, 'latestnews':latestnews, 'popularnews':popnews, 'trending':trending}) #ordering post by latest added

def about(request):
    site = Main.objects.get(pk=2)
    popnews = News.objects.all().order_by('-show')[:3]
    return render(request, 'front/about.html', {'site':site, 'popularnews':popnews})


def panel(request):
    #login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end
    return render(request, 'back/home.html')
#custom admin login area
def admin_login(request):
    if request.method == 'POST' :
        u_name = request.POST.get('username')
        u_pass = request.POST.get('password')

        if u_name != '' and u_pass != '' :
            user = authenticate(username=u_name, password=u_pass)

            if user != None :
                login(request, user)
                return redirect('panel')


    return render(request, 'front/login.html')
#logout function
def admin_logout(request):        
    logout(request)
    return render(request, 'front/login.html')

#site settings

def site_settings(request):
    #login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end

    if request.method == 'POST':
        title = request.POST.get('title')
        tel = request.POST.get('contact')
        fb = request.POST.get('facebook')
        tw = request.POST.get('twitter')
        yt = request.POST.get('youtube')
        about = request.POST.get('about_site')
        link = request.POST.get('footer-link')
        
        if fb == "" : fb == "#"
        if tw == "" : tw == "#"
        if yt == "" : yt == "#"
        if link == "" : link == "#"

        if title == "" or tel == "" or about == "":
            error = 'All fields are required'
            return render(request, 'back/error.html', {'error':error})

        try:
            logo = request.FILES['sitepic']
            fs = FileSystemStorage()
            filename = fs.save(logo.name, logo)
            url = fs.url(filename)
        except :
            filename = '-'
            url = '-' 

        try:
            logo2 = request.FILES['sitepic2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(logo2.name, logo2)
            url2 = fs2.url(filename2)
        except :
            filename2 = '-'
            url2 = '-' 

        b = Main.objects.get(pk=2)
        b.name = title
        b.tel = tel
        b.facebook = fb
        b.twitter = tw
        b.youtube = yt
        b.about = about
        b.footer_link = link
        if filename != "-" : b.picname = filename
        if url != "-" : b.picurl = url
        if filename2 != '-' : b.picname2 = filename2
        if url2 != "-" : b.picurl2 = url2

        b.save()


    site = Main.objects.get(pk=2)
    return render(request, 'back/settings.html', {'site':site})

#about page settings

def about_settings(request):
    #login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end
    if request.method == 'POST' :
        txt = request.POST.get('about-txt')
        if txt == "" :
            error = "All the fields required"

        b = Main.objects.get(pk=2)
        b.abouttxt = txt
        b.save()
    site = Main.objects.get(pk=2)
    return render(request, 'back/about_settings.html',{'about':site})

#contact page

def contact(request):
    site = Main.objects.get(pk=2)
    popnews = News.objects.all().order_by('-show')[:3]

    return render(request, 'front/contact.html', {'site':site, 'popnews':popnews})    

