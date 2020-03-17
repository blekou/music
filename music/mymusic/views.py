from django.shortcuts import render

# Create your views here.

def index(request):
    datas = {

    }
    return render(request, "pages/index.html", datas)

def about(request):
    datas = {

    }
    return render(request, "pages/about.html", datas)

def blog(request):
    datas = {

    }
    return render(request, "pages/blog.html", datas)

def track(request):
    datas = {

    }
    return render(request, "pages/track.html", datas)


def contact(request):
    datas = {

    }
    return render(request, "pages/contact.html", datas)


def single(request):
    datas = {

    }
    return render(request, "pages/single-blog.html", datas)


def elements(request):
    datas = {

    }
    return render(request, "pages/elements.html", datas)


def page(request):
    datas = {

    }
    return render(request, "pages/elements.html", datas)
