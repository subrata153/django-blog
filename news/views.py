from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .models import TrendingNews
from subcat.models import Subcat
from main.models import Main
from django.core.files.storage import FileSystemStorage #for import media file
import datetime
from cat.models import Cat

# Create your views here.

def news_details(request,word):
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cats = Cat.objects.all()
    subcat = Subcat.objects.all()
    latestnews = News.objects.all().order_by('-pk')[:3]
    tagname = News.objects.get(name=word).tag
    tag = tagname.split(',')


    shownews = News.objects.filter(name=word)
    popularnews = News.objects.all().order_by('-show')[:3]


	#count post views
    try :
        mynews = News.objects.get(name=word)
        mynews.show = mynews.show + 1
        mynews.save()
    except :
        print('Error')
    return render(request, 'front/news_details.html', {'site':site, 'news':news, 'cat':cats, 'subcat':subcat, 'latestnews':latestnews, 'shownews':shownews, 'popularnews':popularnews,'tag':tag})

def news_list(request):
	#login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end

    news = News.objects.all()
    cat = Subcat.objects.all()
    return render(request, 'back/news_list.html', {'news':news, 'cat':cat}) 

def news_add(request):
	#login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end

	#get form data using post method
    cat = Subcat.objects.all()

	#add current date 

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    if len(str(day)) == 1 :
	    day = '0' + str(month)
    if len(str(month)) == 1 :
	    month = '0' + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)

    hours = str(hour) + ':' + str(minute) + ':' + str(second)

    if request.method == 'POST':
	    newstitle = request.POST.get('newstitle')
	    newscat = request.POST.get('newscat')
	    newstxtshort = request.POST.get('newstxtshort')
	    newstxt = request.POST.get('newstxt')
	    catid = request.POST.get('newscat')
	    tag = request.POST.get('newstag')
		# catid =  Subcat.objects.filter(pk=newscat)
	    # newstxtshort = request.POST.get('newstxtshort')
	    if newstitle == '' or newscat == '' or newstxt == '':
			#custom error page
		    error = 'All fields are required'
		    return render(request, 'back/error.html', {'error': error})
		#check if image file is choosen
	    try :
		    newsimg = request.FILES['newsimg']
			
		    fs = FileSystemStorage()
		    filename = fs.save(newsimg.name, newsimg)
		    url = fs.url(filename)
			# print(url)
			#check file type
		    if str(newsimg.content_type).startswith('image'):
					#check file size
				    if newsimg.size < 5000000 :
					    catname = Subcat.objects.get(pk=catid).name
					    ocatid = Subcat.objects.get(pk=catid).catid
					    news_save = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, time=hours, picname=filename, picurl=url, author='admin', catname=catname, catid=catid, show=0, ocatid=ocatid, tag=tag)		
					    news_save.save()
						#count news in category
					    count = len(News.objects.filter(ocatid=ocatid))

					    cat_save = Cat.objects.get(pk=ocatid)
					    cat_save.count = count
					    cat_save.save()

					    return redirect('news_list')
				    else :
					    error = 'File size moren than 5 MB please upload lower size'
					    return render(request, 'back/error.html', {'error': error})
		    else:
			    fs.delete(filename)
			    error = 'Please choose a valid file format'
			    return render(request, 'back/error.html', {'error': error}) 
			
	    except :
		    error = 'Please choose a image file'
		    return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/news_add.html', {'cat':cat})

#delete news
def news_delete(request,pk):
	#login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end

    try :
	    news = News.objects.get(pk=pk)
	    fs = FileSystemStorage()
	    fs.delete(news.picname)
	    ocatid = News.objects.get(pk=pk).ocatid
	    news.delete()
		
		#delete count when deleting news
	    count = len(News.objects.filter(ocatid=ocatid))
	    cat_del = Cat.objects.get(pk=ocatid)
	    cat_del.count = count
	    cat_del.save()

    except :
	    error = 'Something wrong'
	    return render(request, 'back/error.html', {'error': error})

    return redirect('news_list')

#edit news function

def news_edit(request,pk):
	#login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end

	#check if news clicked news exist or not
    if len(News.objects.filter(pk=pk)) == 0:
	    error = 'No news found'
	    return render(request, 'back/error.html', {'error': error})
    news = News.objects.get(pk=pk)
    cat = Subcat.objects.all()

    if request.method == 'POST':
	    newstitle = request.POST.get('newstitle')
	    newstxtshort = request.POST.get('newstxtshort')
	    newstxt = request.POST.get('newstxt')
	    catid = request.POST.get('newscat')
	    tag = request.POST.get('newstag')
		# newscat = Subcat.objects.filter(pk=catid).name


	    if newstitle == '' or newstxtshort == '' or newstxt == '':
			#custom error page
		    error = 'All fields are required'
		    return render(request, 'back/error.html', {'error': error})
		#check if image file is choosen
	    try :
		    newsimg = request.FILES['newsimg']
		    fs = FileSystemStorage()
		    filename = fs.save(newsimg.name, newsimg)
		    url = fs.url(filename)

			#check file type
		    if str(newsimg.content_type).startswith('image'):
				#check file size
			    if newsimg.size < 5000000 :
				    catname = Subcat.objects.get(pk=catid).name
				    news_save = News.objects.get(pk=pk)

					#delete existing image while add new image
				    fss = FileSystemStorage()
				    fss.delete(news_save.picname)

				    news_save.name = newstitle
				    news_save.short_txt = newstxtshort
				    news_save.body_txt = newstxt
				    news_save.picname = filename
				    news_save.picurl = url
				    news_save.author = "-"
				    news_save.catname = catname
				    news_save.catid = catid
				    news_save.tag = tag

				    news_save.save()
				    return redirect('news_list')
			    else :
				    fs = FileSystemStorage()
				    fs.delete(newsimg)
				    error = 'File size moren than 5 MB please upload lower size'
				    return render(request, 'back/error.html', {'error': error})
		    else:
			    fs = FileSystemStorage()
			    fs.delete(filename)
			    error = 'Please choose a valid file format'
			    return render(request, 'back/error.html', {'error': error}) 
			
	    except :
		    catname = Subcat.objects.get(pk=catid).name
		    news_save = News.objects.get(pk=pk)

		    news_save.name = newstitle
		    news_save.short_txt = newstxtshort
		    news_save.body_txt = newstxt
			# news_save.picurl = url
		    news_save.catname = catname
		    news_save.catid = catid
		    news_save.tag = tag

		    news_save.save()
		    return redirect('news_list')

    return render(request, 'back/news_edit.html', {'pk':pk, 'news':news, 'cat': cat})


#tending news add

def trending_add(request):
    trending = TrendingNews.objects.all()
	#login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end
    if request.method == 'POST':
        tnews = request.POST.get('tnews')

        if tnews == '':
            msg = 'Field can not be empty'

            return render(request, 'front/msgbox.html', {'msg':msg})

        trending = TrendingNews( tnews=tnews )
        trending.save()

        msg = "Inserted successfully"
        return render(request, 'front/msgbox.html', {'msg':msg})

    return render(request, 'back/trending_add.html', {'trending':trending})

def del_tredning(request, pk):
	#login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end
    trending = TrendingNews.objects.filter(pk=pk)
    trending.delete()
		
    return redirect('trending_add') 

def edit_trending(request, pk):
	#login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end
    trending = TrendingNews.objects.get(pk=pk).tnews
    if request.method == 'POST':
	    gtnews = request.POST.get('tnews')

	    if gtnews == '':
		    msg = 'Field can not be empty'
		    return render(request, 'front/msgbox.html', {'msg':msg})
	    b = TrendingNews.objects.get(pk=pk)	
	    b.tnews = gtnews
	    b.save()
	    return redirect('trending_add') 
    return render(request, 'back/trending_edit.html', {'trending':trending,'pk':pk})
