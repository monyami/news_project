from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm

def news_list(request):
    news = News.objects.all()
    return render(request, 'mainapp/news_list.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'mainapp/news_detail.html', {'news': news})

@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'mainapp/news_form.html', {'form': form})
