from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Page, Feedback, GalleryImage, Service
from .forms import PageForm, FeedbackForm, GalleryImageForm
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods

def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('-created_at')
    return render(request, 'gallery.html', {'images': images})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Спасибо, {form.cleaned_data["name"]}! Ваш отзыв сохранен.')
            return redirect('feedback')
    else:
        form = FeedbackForm()
    
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback.html', {
        'form': form,
        'feedbacks': feedbacks
    })

@login_required
def admin_panel(request):
    pages = Page.objects.all().order_by('-created_at')
    return render(request, 'admin/panel.html', {'pages': pages})

@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Страница успешно создана.')
            return redirect('admin_panel')
    else:
        form = PageForm()
    
    return render(request, 'admin/page_form.html', {'form': form})

@login_required
def page_edit(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, 'Страница успешно обновлена.')
            return redirect('admin_panel')
    else:
        form = PageForm(instance=page)
    
    return render(request, 'admin/page_form.html', {
        'form': form,
        'page': page
    })

@login_required
def page_delete(request, slug):
    page = get_object_or_404(Page, slug=slug)
    page.delete()
    messages.success(request, 'Страница успешно удалена.')
    return redirect('admin_panel')

@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('index')

@login_required
def gallery_upload(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изображение успешно загружено')
            return redirect('gallery')
    else:
        form = GalleryImageForm()
    return render(request, 'admin/gallery_upload.html', {'form': form})

def page_view(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_view.html', {'page': page})

@login_required
def delete_image(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    image.delete()
    messages.success(request, 'Изображение успешно удалено')
    return redirect('gallery')

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_feedback(request, pk):
    if request.method == 'POST':
        feedback = get_object_or_404(Feedback, pk=pk)
        feedback.delete()
        messages.success(request, 'Отзыв успешно удален')
    return redirect('feedback') 