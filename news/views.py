from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from news.models import Nation, Author, Category

def one_nations(request, id):
    print("ONE!!!!!")
    return render(request, 'nations.html', {'authors': Author.objects.filter(id=id).select_related('nationality').order_by('name')})

def list_nations(request):
    print(request.GET)
    if 'id' in request.GET:
        return
    return render(request, 'nations.html', {'authors': Author.objects.all().select_related('nationality').order_by('name')})

    ret = [{'id': n.pk, 'name': n.name} for n in Nation.objects.all().order_by('name')]
    return JsonResponse({'data': ret, })


def index_page(request):
    print(request)
    return render(request, 'index.html', {'title': "PREVET!", 'categories_list': Category.objects.all().order_by('position') })


