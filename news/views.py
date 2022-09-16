from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.db.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

from django.contrib.auth.models import User, Group

from .models import News, Category, Song
from .forms import NewsForm, UserRegisterForm, UserLoginForm, SongsForm




class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 4
    # extra_context = {'title': 'Главная'}
    # queryset = News.objects.select_related('category')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])

        return context

    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
    login_url = '/news/login/'
    # raise_exception = Trueя


# Удаление новостей
class Delete_News(LoginRequiredMixin, DeleteView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/news_delete.html'
    login_url = '/news/login/'
    success_url = reverse_lazy('home')



# Штука для регистрации пользователей
def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации!!!')
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }
    return render(request, 'news/register.html', context)


# Штука для авторизации

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'news/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def music(request):
    # song_item = get_object_or_404(Song,pk=song_id)
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"news/music.html",context)

class ViewSong(DetailView):
    model = Song
    context_object_name = 'song_item'
    template_name = 'news/song.html'
    # pk_url_kwarg = 'news_id'



def chart(request):
    songs = Song.objects.all()
    
    context ={
        'songs': songs
    }
    return render(request, "news/chart.html", context)

class CreateSong(LoginRequiredMixin, CreateView):
    model = Song
    form_class = SongsForm
    template_name = 'news/add_song.html'
    login_url = '/news/login/'
    success_url = reverse_lazy('chart')


def UpVote(requets,pk):
    song = Song.objects.get(pk=pk)
    song.rating += 1
    song.save()
    return redirect(reverse('chart'))

def DownVote(requets,pk):
    song = Song.objects.get(pk=pk)
    song.rating -= 1
    song.save()
    return redirect(reverse('chart'))


# def index(request):
#     news = News.objects.all()
#     context ={
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, template_name='news/category.html',context=context)


# def view_news(request, news_id):
#     #news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         "news_item": news_item
#     }
#     return render(request,'news/view_news.html', context=context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#
#     return render(request, 'news/add_news.html', {'form': form})