from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from subcat.models import Subcat
from news.models import News
from django.core.files.storage import FileSystemStorage #for import media file
import datetime
from cat.models import Cat
#create your views here

def add_contact(request):
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
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        if name == '' or email == '' or msg == '':
            msg = "All fields required"
            return render(request, 'front/msgbox.html', {'msg':msg})

        contact_details = ContactForm(
            name=name,
            email=email,
            message=msg,
            date=today,
            time=hours,
        )
        contact_details.save()    
        msg = "We got your message"
        return render(request, 'front/msgbox.html', {'msg':msg})

    return render(request, 'front/msgbox.html')

def contact_list(request):
    #login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end
    contact_list = ContactForm.objects.all()

    return render(request, 'back/contact_list.html', {'contacts':contact_list})

#contact delete action

def contact_delete(request, pk):
    #login check start
    if not request.user.is_authenticated :
        return redirect('admin_login')
    #login check end
    b = ContactForm.objects.filter(pk=pk)
    b.delete()
        
    return redirect('contact_list')