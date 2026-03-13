from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.db.models import Count
from django.conf import settings
from .models import Article, Document, GalleryImage, TimelineEvent, Category, Book
import os


def home(request):
    """Home page with featured content"""
    featured_articles = Article.objects.filter(is_featured=True)[:3]
    recent_articles = Article.objects.all()[:5]
    recent_documents = Document.objects.filter(is_active=True)[:5]
    gallery_images = GalleryImage.objects.filter(is_featured=True)[:6]
    
    context = {
        'featured_articles': featured_articles,
        'recent_articles': recent_articles,
        'recent_documents': recent_documents,
        'gallery_images': gallery_images,
    }
    return render(request, 'portal/home.html', context)


def about(request):
    """About Fakir Mohan Senapati page"""
    timeline_events = TimelineEvent.objects.all()
    context = {
        'timeline_events': timeline_events,
    }
    return render(request, 'portal/about.html', context)


def works(request):
    """Literary works of Fakir Mohan Senapati"""
    works_category = get_object_or_404(Category, slug='works') if Category.objects.filter(slug='works').exists() else None
    articles = Article.objects.filter(category=works_category) if works_category else Article.objects.all()
    context = {
        'articles': articles,
        'category': works_category,
    }
    return render(request, 'portal/works.html', context)


def legacy(request):
    """Legacy and influence of Fakir Mohan Senapati"""
    legacy_category = get_object_or_404(Category, slug='legacy') if Category.objects.filter(slug='legacy').exists() else None
    articles = Article.objects.filter(category=legacy_category) if legacy_category else Article.objects.none()
    gallery = GalleryImage.objects.all()[:12]
    context = {
        'articles': articles,
        'category': legacy_category,
        'gallery': gallery,
    }
    return render(request, 'portal/legacy.html', context)


def documents_list(request):
    """List of all downloadable documents"""
    categories = Category.objects.annotate(doc_count=Count('documents')).filter(doc_count__gt=0)
    category_id = request.GET.get('category')
    
    if category_id:
        documents = Document.objects.filter(is_active=True, category_id=category_id)
    else:
        documents = Document.objects.filter(is_active=True)
    
    context = {
        'documents': documents,
        'categories': categories,
        'selected_category': category_id,
    }
    return render(request, 'portal/documents.html', context)


@login_required(login_url='/login/')
def download_document(request, pk):
    """Download a document - Only for logged-in users"""
    document = get_object_or_404(Document, pk=pk, is_active=True)
    
    # Increment download count
    document.increment_download_count()
    
    # Open and serve the file
    try:
        response = FileResponse(document.file, as_attachment=True)
        return response
    except FileNotFoundError:
        return HttpResponse("ଫାଇଲ୍ ମିଳୁନାହିଁ |", status=404)


def article_detail(request, slug):
    """View individual article"""
    article = get_object_or_404(Article, slug=slug)
    related_articles = Article.objects.filter(category=article.category).exclude(pk=article.pk)[:3]
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'portal/article_detail.html', context)


def gallery(request):
    """Photo gallery"""
    images = GalleryImage.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'portal/gallery.html', context)


def register_view(request):
    """User registration"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'portal/register.html', context)


def login_view(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'portal/login.html', context)


def logout_view(request):
    """User logout"""
    logout(request)
    return redirect('home')


def books_list(request):
    """List of all books by Fakir Mohan Senapati"""
    books = Book.objects.filter(is_active=True)
    context = {
        'books': books,
    }
    return render(request, 'portal/books.html', context)


@login_required(login_url='/login/')
def download_book(request, pk):
    """Download a book - Only for logged-in users"""
    book = get_object_or_404(Book, pk=pk, is_active=True)

    # Increment download count
    book.increment_download_count()

    # Build full file path
    file_path = os.path.join(settings.BOOKS_DIR, book.file_path)

    # Open and serve the file
    try:
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=book.file_path)
        return response
    except FileNotFoundError:
        return HttpResponse("ପୁସ୍ତକ ମିଳୁନାହିଁ |", status=404)
