from django.views import generic
from .models import post


class PostList(generic.ListView):
    model = post



class PostDetail(generic.DetailView):
        model = post






class AddPost(generic.CreateView):
            model = post
            fields =['author','title','content','tags','image']
            success_url = '/blog/'


class EditPost(generic.UpdateView):
            model = post
            fields =['author','title','content','tags','image']
            success_url = '/blog/'
            template_name = 'posts/edit.html'



class DeletePost(generic.DeleteView):
    model = post
    success_url = '/blog/'            