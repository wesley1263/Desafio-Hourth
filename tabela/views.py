from django.http import JsonResponse
from django.shortcuts import render
from .utils.datatable import DataTable


def index(request):
    return render(request, 'tabela/index.html')


def tabela(request):
    if request.method == 'GET':
        products = DataTable()
        page = int(request.GET.get("page", 1))
        result = products.get_data_table(page)
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=400)
