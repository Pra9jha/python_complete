from django.shortcuts import render
from product.models import product as pd
from django.http import HttpResponse

obj=pd.objects.get(id=1)
title=(obj.title)
des=obj.description
content={'name':title,'description':des}

def reflect_data(request):
   return render(request,'product/show.html',content)

