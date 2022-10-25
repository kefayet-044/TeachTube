from django.shortcuts import render, redirect
from .models import Video, Category, Comment
from django.http import HttpResponse
from .forms import Post_Model_From, CommentModelForm


def newsfeed(request):
    allVdos = Video.objects.all()
    allCat = Category.objects.all()
    context = {
        "allVdos": allVdos,
        "allCat": allCat,
    }
    return render(request, 'newsfeed.html', context)


def singleVideo(request, pk, title):
    video = Video.objects.get(id=pk)
    user = request.user
    allVdos = Video.objects.all()
    commentBox = CommentModelForm()
    video.views.add(user)

    context = {
        "video": video,
        "allVdos": allVdos.exclude(id=pk),
        "commentBox": commentBox,


    }
    return render(request, 'singlePage.html', context)


def saveComment(request, pk):
    video = Video.objects.get(id=pk)
    if request.method == 'POST':
        comBody = request.POST['body']
        cForm = CommentModelForm(request.POST)
        if cForm.is_valid():
            instance = cForm.save(commit=False)
            instance.user = request.user
            instance.post = video
            instance.body = comBody
            instance.save()
            return redirect('video-reading', pk=pk, title=video.title.replace(' ', '-'))

        else:
            return HttpResponse("SomeThing Went Wrong")
    else:
        return HttpResponse("SomeThing Went Wrong")


def uploadVideo(request):
    if request.user.is_staff:
        videoForm = Post_Model_From()
        context = {
            "vForm": videoForm
        }
        return render(request, "upload.html", context)
    else:
        return HttpResponse("Not Authenticate")


def saveVideo(request):

    if request.method == "POST":
        vForm = Post_Model_From(request.POST, request.FILES or None)
        if vForm.is_valid():
            instance = vForm.save(commit=False)
            instance.save()
            return redirect("newsfeed")
        else:
            return HttpResponse("SomeThing Went Wrong")

    else:
        return HttpResponse("SomeThing Went Wrong")
