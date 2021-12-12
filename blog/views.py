from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import BlogPost
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """Return the last five blog posts."""

        return BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:510]
 
def reader(request,pk):
    blog_post = get_object_or_404(BlogPost,pk=pk)
    template_name='blog/reader.html'
    print("running code at ",pk,blog_post.blog_subject)
    #blog_post_subject = blog_post.blog_subject
    return render (request,template_name,{'blog_post_subject':blog_post.blog_subject,id:pk,'blog_post':blog_post,'blog_post_content':blog_post.blog_post})


def postnew(request):
    print("this is rendering")
    return render(request,'blog/postnew.html')
    #return HttpResponseRedirect(reverse('blog:index'))

def submit(request):
    print("running this code - fritz")
    blog_post = BlogPost()
    blog_post.publisher_name=request.POST['fname']
    blog_post.blog_subject=request.POST['lname']
    blog_post.blog_post=request.POST['blog']
    blog_post.pub_date = timezone.now()
    if len(blog_post.blog_subject) < 3:
        return render (request,'blog/postnew.html', {'error_message': "Subject was too short, post not accepted"})
    else:
        print('subject and subject length:',len(blog_post.blog_subject),blog_post.blog_subject)
    blog_post.save()
    return HttpResponseRedirect(reverse('blog:index'))

