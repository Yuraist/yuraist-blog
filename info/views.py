from django.shortcuts import render

def about_page(request):
    return render(request, 'info/about.html')


def contact_page(request):
    return render(request, 'info/contact.html')