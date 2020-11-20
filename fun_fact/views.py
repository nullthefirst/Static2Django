from django.shortcuts import render


def submission(request):
    return render(request, 'pages/submit.html')
