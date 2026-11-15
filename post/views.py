from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from post.models import Articles

# Vue d'accueil
class HomePageView(ListView):
    model = Articles
    context_object_name = 'articles'

    # verifier si l'utilisateur est connecter
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

# Vue pour un article
class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'post/article_detail.html'
    context_object_name = 'article'

# Vue d'ajout
@method_decorator(login_required, name='dispatch')
class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'post/article_create.html'
    fields = ['title', 'content', 'slug',]


# Vue de modification
class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'post/article_update.html'
    fields = ['title', 'content', 'published',]

# Vue de suppression
class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'post/article_delete.html'
    context_object_name = 'suppression'
    success_url = reverse_lazy('post:home')
