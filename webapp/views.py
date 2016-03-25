from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'webapp/home.html')
def kontakt(request):
	return render(request, 'webapp/basic.html', {'content': ['Walterscheid - Serwis |  R.Bresiński','ul.Wiosenna 67', '62-081 Baranowo k/Poznania', 'tel/fax 061 814 22 36  kom. 602 520 510']})