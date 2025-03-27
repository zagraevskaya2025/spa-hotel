from .models import Page

def pages_processor(request):
    return {
        'pages': Page.objects.all()
    } 