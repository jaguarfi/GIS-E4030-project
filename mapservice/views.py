from django.shortcuts import render


def testpage(request):
    return render(request, 'testpage.html')	
	