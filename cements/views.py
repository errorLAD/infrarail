from django.shortcuts import render, get_object_or_404
from .models import Cement
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
# Create your views here.
def cements(request):
    cements = Cement.objects.order_by('-created_date')
    paginator = Paginator(cements, 4)
    page = request.GET.get('page')
    paged_cements = paginator.get_page(page)

    model_search = Cement.objects.values_list('model', flat=True).distinct()
    city_search = Cement.objects.values_list('city', flat=True).distinct()
    year_search = Cement.objects.values_list('year', flat=True).distinct()
    body_style_search = Cement.objects.values_list('body_style', flat=True).distinct()

    data = {
        'cements': paged_cements,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cements/cements.html', data)

def cement_detail(request, id):
    single_cement = get_object_or_404(Cement, pk=id)

    data = {
        'single_cement': single_cement,
    }
    return render(request, 'cements/cement_detail.html', data)


def cementsearch(request):
    cements = Cement.objects.order_by('-created_date')

    model_search = Cement.objects.values_list('model', flat=True).distinct()
    city_search = Cement.objects.values_list('city', flat=True).distinct()
    year_search = Cement.objects.values_list('year', flat=True).distinct()
    body_style_search = Cement.objects.values_list('body_style', flat=True).distinct()
  
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cements = cements.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cements = cements.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cements = cements.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cements = cements.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cements = cements.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cements = cements.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cements':  cements,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cements/cementsearch.html', data)
