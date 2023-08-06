from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.db.models import Max  # Add this import
from .models import ProcessedURL
from .forms import URLForm
import requests
from django.http import HttpResponse



def scan_website(url):
    api_key = 'YOUR_VIRUSTOTAL_API_KEY'
    scan_url = f'https://www.virustotal.com/api/v3/urls/{url}'
    headers = {'x-apikey': api_key}
    response = requests.get(scan_url, headers=headers)
    return response.json()



def input_data(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_1 = form.cleaned_data['url_1']
            url_2 = form.cleaned_data['url_2']
            url_3 = form.cleaned_data['url_3']
            
            urls = [url_1.strip(), url_2.strip(), url_3.strip()]
            
            max_processed_order = ProcessedURL.objects.aggregate(Max('processed_order'))['processed_order__max']
            next_order = 1 if max_processed_order is None else max_processed_order + 1
            
            for url in urls:
                if url:
                    try:
                        ProcessedURL.objects.create(url=url, processed_order=next_order)
                        next_order += 1
                    except IntegrityError:
                        # Handle duplicate URL error
                        error_message = f"URL '{url}' is already in the database."
                        return render(request, 'data_processor/input_data.html', {'form': form, 'error_message': error_message})
            return redirect('output_data')
    else:
        form = URLForm()
    return render(request, 'data_processor/input_data.html', {'form': form})

def output_data(request):
    processed_urls = ProcessedURL.objects.order_by('processed_order')
    # processed_urls = ProcessedURL.objects.all()
    return render(request, 'data_processor/output_data.html', {'processed_urls': processed_urls})
