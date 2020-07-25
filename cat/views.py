from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat

def cat_list(request):
    cat = Cat.objects.all()
    return render(request, 'back/cat_list.html', {'cat':cat})

def cat_add(request):

    if request.method == 'POST':
        cat_title = request.POST.get('cattitle')
        cat_description = request.POST.get('catdesc')

        if cat_title == '':
            error = 'Please add a category name'
            return render(request, 'back/error.html', {'error':error})
        #check if the category is already added
        if len(Cat.objects.filter(name=cat_title)) != 0:
            error = 'Oho! You have already added this category'
            return render(request, 'back/error.html', {'error':error})
        else:
            cat_save = Cat(name=cat_title,description=cat_description)
            cat_save.save()    
            return redirect('cat_list')

    return render(request, 'back/cat_add.html')




