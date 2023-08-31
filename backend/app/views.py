from django.shortcuts import render


# Create your views here.
def show_index_page(request):
    return render(request, 'app/index.html')
