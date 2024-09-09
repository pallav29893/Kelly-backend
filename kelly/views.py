from django.shortcuts import render,get_object_or_404 
from .models import Post, Comment,Category,Tag
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    category = Category.objects.all()
    tags = Tag.objects.all()
    context = {'posts': posts,'category':category,'tags':tags}
    return render(request, 'blog.html', context)    

def about(request):
    return render(request,'about_us.html')

def contact(request):
    return render(request, 'contact_us.html')

def blog_detail(request,slug):
    print(slug, ',,,,,,,,,,,,,,,,,,,,,,,,,,,')
    if request.method == "POST":
        reply = request.POST.get('reply',None)
        parent = request.POST.get('comment',None)
        comment = Comment.objects.filter(id=parent).first()
        post = Post.objects.filter(slug=slug).first
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        text = request.POST.get('text', None)
        if comment is not None:
            Comment.objects.create(text=reply,post=post,parent=comment,name=name)
        else:
            Comment.objects.create(name=name,email=email,text=text,post=post)
        return redirect(reverse('blog_details',kwargs={'slug': post.slug}))        
    else:
        post = Post.objects.filter(slug=slug).first()
        print(post, "--9090-9-090-")
        comment = Comment.objects.filter(post=post,parent__isnull=True)
        print(comment,'<<<<<<<<<<<<<<<<<<<<<<<<')
        category = Category.objects.all()
        tags = Tag.objects.all()
        context =  {'category':category,'tags':tags,'post':post,'comment':comment}
        return render(request, 'blog_detail.html',context)

def home_detail(request):
    return render(request,'home_detail.html')

def category_blog_list(request,slug):
    category = get_object_or_404(Category,slug=slug)
    posts = Post.objects.filter(category=category)
    context = {'posts':posts,'category':category}
    return render(request,'category_blog_list.html',context)

def tag_blog_list(request,slug):
    tags = get_object_or_404(Tag,slug=slug)
    posts = Post.objects.filter(tags=tags)
    context = {'posts':posts,'tags':tags}
    return render(request,'tag_blog_list.html',context)

# def post_detail(request, slug):
  
#     if request.method == "POST":
#         reply = request.POST.get('reply',None)
#         parent = request.POST.get('comment',None)
#         comment = Comment.objects.filter(id=parent).first()
#         post = get_object_or_404(Post, slug=slug)
#         name = request.POST.get('name', None)
#         email = request.POST.get('email', None)
#         text = request.POST.get('text', None)
#         if comment is not None:
#             Comment.objects.create(text=reply, post=post,parent=comment,name=name)
#         else:
#             Comment.objects.create(name=name,email=email,text=text, post=post)
#         return redirect(reverse('post_detail', kwargs={'slug': post.slug}))        
#     else:
#         post = get_object_or_404(Post, slug=slug)
#         comment = Comment.objects.filter(post=post,  parent__isnull= True)
#         category = Category.objects.all()
#         tags = Tag.objects.all()
#         context =  {'post': post,'comment':comment,'category':category,'tags':tags}
#         return render(request, 'blog/post_detail.html',context)
    



# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now())
#     category = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {'posts': posts,'category':category,'tags':tags}
#     return render(request, 'blog/post_list.html', context)    


    














