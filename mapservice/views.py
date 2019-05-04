from django.shortcuts import render


def testpage(request):
    context = {'s' : 100, 'string' : 'moi'}
    return render(request, 'testpage.html', context)	
	