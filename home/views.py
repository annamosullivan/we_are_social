from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView


# Create your views here.
def get_index(request):
    return render(request, 'index.html')


class BlogRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('blog_posts')
