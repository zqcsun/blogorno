from django.shortcuts import render
from .models import Post
# Create your views here.

def lists_page(request):
    items = Post.objeck.all()
    context = {'items':items}
    return render(request,"",context)

def item_page(request,slug,id):
    item = Post.object.get(slug = slug, id=id)
    context = {'item':item}
    return render(request,"",context)