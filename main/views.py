from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306217430',
        'name': 'Simforiannus Jonathan Flonas Harefa',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)