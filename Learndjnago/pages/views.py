from django.shortcuts import render
from django.http import HttpResponse

context={"name":"Prashant","company":"Engagedly pvt ltd","Location":"Bangalore","mynum":[12,23,34,45,56]}

def home_page(request , *args,**kwargs):
    # print(request.user)
    # return HttpResponse("<h1>Blank Page </h1>")
    return render(request, 'pages/home.html',context)
def to_do(request):
    return render(request,'pages/todo.html')
def inforamation(*args ,**kwargs):
     print(*args )
     print("________________________")
     print(**kwargs)
     print("________________________")
     return HttpResponse("nothing to return ")
