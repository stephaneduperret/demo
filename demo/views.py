from django.shortcuts import render

def demo(request):

    return render(request, 'page_demo.html')
