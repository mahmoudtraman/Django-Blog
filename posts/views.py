from django.shortcuts import render
from .models import post


def post_list(request):
    data = post.objects.all()
    return render(request,'posts.html',{'posts':data})