from django.shortcuts import render

# Create your views here.
def html_form(request):
    return render(request,'html_form.html')

def html_form1(request):
    return render(request,'html_form1.html')