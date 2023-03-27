from django.shortcuts import render
from .models import *

# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    about = About.objects.first()
    context = {
        'about': about
    }
    return render(request, 'about.html', context)



def class_page(request):
    classes = Classes.objects.all()
    parents = Parents.objects.all()
    context = {
        'classes': classes,
        'parents': parents,
    }
    return render(request, 'class.html', context)

def teachers_page(request):
    teacher = Teachers.objects.all()
    context={
        'teacher': teacher
    }
    return render(request, 'teachers.html',context)

def gallery_page(request):
    gallery = Gallery.objects.all()
    context={
        'gallery': gallery
    }
    return render(request, 'gallery.html', context)


def blog_page(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'blog.html', context)

def blog_detail_page(request, slug):
    detail = Blog.objects.get(slug=slug)
    context={
        'detail': detail
    }

    return render(request, 'blog_detail.html', context)

def contact_page(request):
    contact = Contact.objects.first()
    

    context={
        'contact': contact
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)
    return render(request, 'contact.html', context)