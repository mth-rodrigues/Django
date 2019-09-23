from django.shortcuts import render

def index(request):
    context = {
        'nomes':[
            'matheus',
            'thays',
            'murilo'
        ],
    'vazio':False,
    'teste': 'teste'}
    return render(request, 'index.html', context)
