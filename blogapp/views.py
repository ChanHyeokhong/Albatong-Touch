from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.contrib.auth.decorators import login_required
	
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

#카테고리 별로 블로그 불러오기
def search(request):
    queryset = Blog.objects.all()
    location = request.GET.get("location")
    job_type = request.GET.get("job_type")


    if(location == "" and job_type == ""):
        queryset = Blog.objects.all()
        return render(request, 'home.html', {'blogs': queryset})

    elif(location == "" or job_type == ""):
        queryset = Blog.objects.all()
        if(location == ""):
            queryset = queryset.filter(job_type=job_type)
        else:
            queryset = queryset.filter(area=location)
        return render(request, 'home.html', {'blogs': queryset})

    else:
        queryset = queryset.filter(area=location, job_type=job_type)
        return render(request, 'home.html', {'blogs': queryset})

def detail(request, blog_id): 
	details = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'detail.html', {'details':details})

def new(request):
    if request.user.is_authenticated: 
        # 로그인 한 상태라면 new포스트 html로 보내기.
        return render(request, 'new.html')
    else:
        # 회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.     
        blogs = Blog.objects
        return render(request, 'home.html', {'blogs': blogs, 'error': 'You have to login to make newpost'})
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.author = request.user
    blog.title = request.POST['title']
    blog.area = request.POST['place']
    blog.job_type = request.POST['job']
    blog.gender = request.POST['gender']
    blog.age=request.POST['age']
    blog.condition = request.POST['condition']
    blog.edu = request.POST['edu']
    blog.pay = request.POST['pay']
    # blog.body = request.POST['body']
    blog.userdate1 = request.POST['userdate1']
    blog.userdate2 = request.POST['userdate2']
    blog.time1 = request.POST['time1']
    blog.time2 = request.POST['time2']
    blog.plus = request.POST['plus']
    blog.call = request.POST['call']
    blog.email = request.POST['email']
    blog.etc = request.POST['etc']
    blog.enddate = request.POST['enddate']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) 

def delete(request, blog_id):
    destroy = get_object_or_404(Blog, pk=blog_id)
    destroy.delete()
    return redirect('home')

def update(request, blog_id):
    updates= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'updates': updates})

def edit(request, blog_id):
    edit = Blog.objects.get(pk=blog_id)
    edit.title = request.POST['title']
    edit.area = request.POST['place']
    edit.job_type = request.POST['job']
    edit.gender = request.POST['gender']
    edit.age=request.POST['age']
    edit.condition = request.POST['condition']
    edit.edu = request.POST['edu']
    edit.pay = request.POST['pay']
    edit.userdate1 = request.POST['userdate1']
    edit.userdate2 = request.POST['userdate2']
    edit.time1 = request.POST['time1']
    edit.time2 = request.POST['time2']
    edit.enddate = request.POST['enddate']
    # edit.body = request.POST['body']
    edit.plus = request.POST['plus']
    edit.call = request.POST['call']
    edit.email = request.POST['email']
    edit.etc = request.POST['etc']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')

@login_required
def post_like(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        return redirect('/blog/'+str(post.id))
    return redirect('/blog/'+str(post.id))
