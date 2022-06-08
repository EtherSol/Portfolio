from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'threes_app/threes/index.html')