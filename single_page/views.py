from django.shortcuts import render

def single_page(request):
    return render(request, 'single_page/read_me.html')
