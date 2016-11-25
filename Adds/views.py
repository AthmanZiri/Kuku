from __future__ import unicode_literals
from django.shortcuts import render

# def get_form(request):
# 	if request.method=='POST':
# 		form=AddForm(request.POST)
# 		if form.is_valid():
# 			return HttpResponseRedirect('/thanks/')
# 	else:
# 		form=AddForm()

# 	return render(request, 'addform.html', {'form':form})

def about(request):
	return render(request, 'Adds/about.html')

def blog(request):
	return render(request, 'Adds/blog.html')

def login(request):
	return render(request, 'Adds/login.html')

def detail(request):
	return render(request, 'Adds/detail.html')		

def map(request):
	return render(request, 'Adds/map.html')