from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'zmones': ['Tomas', "Rokas", "Ainis", "Dar kažkas"],
    }
    return render(request, template_name="index.html", context=context)

