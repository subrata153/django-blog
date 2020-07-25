from django.shortcuts import render, get_object_or_404, redirect
from .models import Subcat
from cat.models import Cat
# Create your views here.

def subcat_list(request):
    subcat = Subcat.objects.all()

    return render(request, 'back/subcat_list.html', {'subcat':subcat})

def subcat_add(request):
    cat = Cat.objects.all()
    if request.method == 'POST':
        title = request.POST.get('name')
        # catname = request.POST.get('catname')
        description = request.POST.get('desc')
        catid = request.POST.get('catid')
        catname = Cat.objects.get(pk=catid).name

        if title == '':
            error = 'Title field is required'
            return render(request, 'back/error.html', {'error':error})
            
        if len(Subcat.objects.filter(name=title)) != 0:
            error = 'Aha! This category already exist'
            return render(request, 'back/error.html')

        else:
            save_subcat = Subcat(name=title,catname=catname,catid=catid,description=description)
            save_subcat.save()
            return redirect('subcat_list')    

    return render(request, 'back/subcat_add.html', {'cat':cat})    