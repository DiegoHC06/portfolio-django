from django.shortcuts import render

# Create your views here.
def renderPosts(request):
    return render(request,'posts.html')
