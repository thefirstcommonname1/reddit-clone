from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Forum
# Create your views here.
def index(request):
    objects = Forum.objects.all()
    context = {
        "objects": objects
    }
    return render(request, "redclone/index.html", context)
def listing(request, id_param):
    objects = Forum.objects.get(id=id_param)
    if objects != None:
        context = {
            "objects": objects
        }
        return render(request, "redclone/listing.html", context)
    return HttpResponseRedirect("404 Page not found buddy")
def upvote(request, id_param):
    objects = Forum.objects.get(id=id_param)
    if objects != None:
        objects.votes += 1
        objects.save()
    return redirect('/'+str(id_param))
def downvote(request, id_param):
    objects = Forum.objects.get(id=id_param)
    if objects != None:
        objects.votes -= 1
        objects.save()
    return redirect('/'+str(id_param))
