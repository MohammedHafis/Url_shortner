import random, string, re
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from .models import URL
from .forms import URLForm

def generate_code(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=length))

def home(request):
    short_url = None
    code = None
    form = URLForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        long_url = form.cleaned_data['long_url'].strip()
        custom_code = form.cleaned_data.get('custom_code') or None

        if custom_code:
            if not re.match(r'^[A-Za-z0-9_-]{3,20}$', custom_code):
                form.add_error('custom_code', "Use 3–20 chars: letters, numbers, '-' or '_'")
            elif URL.objects.filter(short_code=custom_code).exists():
                form.add_error('custom_code', 'That code is taken. Try another.')
            else:
                code = custom_code
        if not custom_code:
            existing = URL.objects.filter(long_url__iexact=long_url).first()
            if existing:
                code = existing.short_code
            else:
                code = generate_code()
                while URL.objects.filter(short_code=code).exists():
                    code = generate_code()

        if not form.errors:
            url_obj, created = URL.objects.get_or_create(short_code=code, defaults={'long_url': long_url})
            short_url = request.build_absolute_uri(f'/{url_obj.short_code}')
    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url, 'code': code})

def redirect_url(request, code):
    url_obj = get_object_or_404(URL, short_code=code)
    url_obj.clicks += 1
    url_obj.last_accessed = timezone.now()
    url_obj.save(update_fields=['clicks', 'last_accessed'])
    return redirect(url_obj.long_url)

def stats(request, code):
    url_obj = get_object_or_404(URL, short_code=code)
    return render(request, 'shortener/stats.html', {'url': url_obj})

@require_POST
def api_shorten(request):
    long_url = request.POST.get('long_url', '').strip()
    custom_code = request.POST.get('custom_code', '').strip() or None
    if not long_url:
        return HttpResponseBadRequest('long_url required')
    code = custom_code or generate_code()
    if custom_code and URL.objects.filter(short_code=custom_code).exists():
        return JsonResponse({'error': 'custom code taken'}, status=409)
    obj, created = URL.objects.get_or_create(short_code=code, defaults={'long_url': long_url})
    short_url = request.build_absolute_uri(f'/{obj.short_code}')
    return JsonResponse({'short_code': obj.short_code, 'short_url': short_url, 'long_url': obj.long_url}, status=201 if created else 200)
