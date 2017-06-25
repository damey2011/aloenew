from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from blogs.models import BlogPost, Comment
from products.models import ProductCategory


class AllBlogs(View):
    def get(self, request):
        posts = BlogPost.objects.all()
        paginator = Paginator(posts, 10)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, 'blog-post-list.html', {'posts': posts})


class BlogPostView(View):
    def get(self, request, slug):
        bp = BlogPost.objects.get(slug=slug)
        c = Comment.objects.filter(parent=bp.id)
        bps = BlogPost.objects.all()[:10]
        return render(request, 'blog-single.html', {'bp': bp, 'comments': c, 'bps': bps})


class ComposeBlogPost(View):
    def get(self, request):
        cats = ProductCategory.objects.all()
        return render(request, 'editor.html', {'cats': cats})

    def post(self, request):
        title = request.POST['post-title']
        content = request.POST['editor1']
        author = request.user
        bp = BlogPost(title=title, content=content, author=author)
        bp.save()
        cats = ProductCategory.objects.all()
        return render(request, 'editor.html', {'success_alert': True, 'cats': cats})


class SaveComment(View):
    def post(self, request):
        post_slug = request.POST['slug']

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        parent = request.POST['parent']

        c = Comment(name=name, email=email, message=message, parent=parent)
        c.save()

        return redirect('/blogs/'+post_slug, {'comment_added': True})
        # return render(request, 'blog-single.html', {'comment_added': True})
