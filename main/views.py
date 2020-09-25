from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from contactform.models import ContactForm
from news.models import TrendingNews
from news.models import News
from manager.models import Manager
from cat.models import Cat
from subcat.models import Subcat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage #for import media file
import random
from random import randint
from django.contrib.auth.models import User

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
    trending = TrendingNews.objects.all().order_by('-pk')[:5]
    #random data for random trending news using random library
    # random_objects = TrendingNews.objects.all()[randint(0, len(trending) -1)]
    # print(random_objects)
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

#user registration area
def myRegister(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        uname = request.POST.get('username')
        mail = request.POST.get('email')
        password = request.POST.get('password')
        ver_pass = request.POST.get('password-verify')
        if name == '':
            msg = "Your password didn't match"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if password != ver_pass :
            msg = "Your password didn't match"
            return render(request, 'front/msgbox.html', {'msg':msg})

        #checking password strength
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in password :

            if i > "0" and i < "9":
                count1 = 1
            if i > "A" and i < "Z":
                count2 = 1
            if i > 'a' and i < 'z':
                count3 = 1
            if i > "!" and i < "(":
                count4 = 1
        if count1 == 0 and count2 == 0 and count3 == 0 and count4 == 0 :
            msg = "Password has to be more strong"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(password) < 8 :
            msg = "Password has to be more than 8 character"
            return render(request, 'front/msgbox.html', {'msg':msg})    

        #check if user already exists
        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=mail)) == 0 :
            user = User.objects.create_user(username=uname,email=mail,password=password)   
            #save data to custom user table 
            b = Manager(name=name,utxt=uname,email=mail)
            b.save()

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
    #login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end
    site = Main.objects.get(pk=2)
    popnews = News.objects.all().order_by('-show')[:3]

    return render(request, 'front/contact.html', {'site':site, 'popnews':popnews})    

#change admin password functionality
def change_pass(request):
    #login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end

    if request.method == 'POST':
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        if oldpass == '' or newpass == '':
            error = "All fields required."
            return render(request, 'back/error.html', {'error':error})
        #checking user authentication
        user = authenticate(username=request.user, password=oldpass)
        #set new admin password
        if user != None :
            if len(newpass) < 8 :
                error = "Your password should me more than 8 char"
                return render(request, 'back/error.html', {'error':error})
            #checking password strength
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            for i in newpass :

                if i > "0" and i < "9":
                    count1 = 1
                if i > "A" and i < "Z":
                    count2 = 1
                if i > 'a' and i < 'z':
                    count3 = 1
                if i > "!" and i < "(":
                    count4 = 1
            if count1 == 1 and count2 == 1 and count3 == 1 and count4 ==1 :
                user = User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()
                return redirect('admin_logout')    
            else :
                error = "Password has to be more strong"
                return render(request, 'back/error.html', {'error':error})                  
        else:
            error = "Password is not correct"
            return render(request, 'back/error.html', {'error':error})  

    return render(request, 'back/changepass.html')