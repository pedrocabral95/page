from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.

def home_view(request,*args, **kwargs):

	#return HttpResponse("ist.html")
	return render(request,"home.html",{})
def about_view(request,*args, **kwargs):
	aboutMe = {
		"general" : ["Good Command in Excell, Word, Acess" ,
					"Installing and Maintenance Software",
					"Good Command in Linux Systems", "Multithreading", "Git"],
		"good" : ["Python"," Django (Python)","C","Java","C++"],
		"normal" : ["Visual Basic","Prolog","Ruby","CSS", "JavaScript","Assembly","Flask (Python)", "Shell Script", "Bash"]
	}
	return render(request,"about.html",aboutMe)

def run_view(request,*args, **kwargs):

	return render(request,"run.html",{})

def football_view(request,*args, **kwargs):

	return render(request,"football.html",{})

def family_view(request,*args, **kwargs):
	return render(request,"family.html",{})

def git_view(request):
	return redirect("https://github.com/pedrocabral95")
