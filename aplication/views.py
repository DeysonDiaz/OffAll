#importante cambiar con cada vista  (views)


from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello World")
    return render(
        request,
        './home.html',
        {'name':'Denilson'}#aplicacion de diccionrios
)
def regClie(request):
    return render(
        request,
        './regClie.html',
        #{'name':'Denilson'}#aplicacion de diccionrios
)
def regProf(request):
    return render(
        request,
        './regProf.html',
        
        #{'name':'Denilson'}#aplicacion de diccionrios
)  
    
""" def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    resp=val1+val2
    return render(
        request,
        './result.html',
        {'result':resp}
    )
     """

