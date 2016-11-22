from django.shortcuts import render
from djngo.http import HttpResponseRedirect
from forms import AddForm

def get_form(request):
	if request.method=='POST':
		form=AddForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form=AddForm()

	return render(request, 'addform.html', {'form':form})
