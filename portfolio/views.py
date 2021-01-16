from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from portfolio.models import Message, Portfolio

# Create your views here.


def index(request):
	blogs = Portfolio.objects
	return render(request, "portfolio/index.html", {'blogs':blogs})

def contact(request):

	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		message=request.POST.get('message')
		
		msg=Message(name=name, email=email, subject=subject, message=message)
		msg.save()
		return HttpResponse("Thanks, Your message has been recevied successfully.")




def detail(request, pk):
	detailblog = get_object_or_404(Portfolio, pk=pk)
	return render(request, 'portfolio/detail.html', {'blog':detailblog})





#uplpad Documents:
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form = DocumentForm()
    return render(request, 'portfolio/model_form_upload.html', {
        'form': form
    })