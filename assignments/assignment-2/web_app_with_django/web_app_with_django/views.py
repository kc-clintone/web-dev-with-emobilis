from django.shortcuts import render

# ======Home screen=======
def index(request):
    return render (request, 'index.html')