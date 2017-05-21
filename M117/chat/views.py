from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def ontoone(value):
	if(value=='on'):
		value=1
	else:
		value=0
	return value


# /chat
def chathome(request):
	if request.method == "POST":
		try:
			first_name_n = request.POST.get('fname')
			last_name_n = request.POST.get('lname')
			user_name_n = request.POST.get('uname')
			password_n = request.POST.get('psw')
			email_n = request.POST.get('email')
			location_n = request.POST.get('location')
			school_n = request.POST.get('school')
			Action_n = ontoone(request.POST.get('Action'))
			Adventure_n = ontoone(request.POST.get('Adventure'))
			Animation_n = ontoone(request.POST.get('Animation'))
			Biography_n = ontoone(request.POST.get('Biography'))
			Comedy_n = ontoone(request.POST.get('Comedy'))
			Crime_n = ontoone(request.POST.get('Crime'))
			Documentary_n = ontoone(request.POST.get('Documentary'))
			Drama_n = ontoone(request.POST.get('Drama'))
			Family_n = ontoone(request.POST.get('Family'))
			Fantasy_n = ontoone(request.POST.get('Fantasy'))
			FilmNoir_n = ontoone(request.POST.get('FilmNoir'))
			History_n = ontoone(request.POST.get('History'))
			Horror_n = ontoone(request.POST.get('Horror'))
			Music_n = ontoone(request.POST.get('Music'))
			Musical_n = ontoone(request.POST.get('Musical'))
			Mystery_n = ontoone(request.POST.get('Mystery'))
			Romance_n = ontoone(request.POST.get('Romance'))
			SciFi_n = ontoone(request.POST.get('SciFi'))
			Sport_n = ontoone(request.POST.get('Sport'))
			Thriller_n = ontoone(request.POST.get('Thriller'))
			War_n = ontoone(request.POST.get('War'))
			Western_n = ontoone(request.POST.get('Western'))
			User.objects.create(first_name = first_name_n , last_name =last_name_n , user_name =user_name_n , password = password_n , email = email_n , location = location_n , school = school_n , Action = Action_n , Adventure = Adventure_n , Animation = Animation_n , Biography = Biography_n , Comedy = Comedy_n , Crime = Crime_n , Documentary = Documentary_n , Drama = Drama_n , Family = Family_n , Fantasy = Fantasy_n , FilmNoir = FilmNoir_n , History = History_n , Horror = Horror_n , Music = Music_n , Musical = Musical_n , Mystery = Mystery_n, Romance = Romance_n, SciFi = SciFi_n , Sport = Sport_n , Thriller = Thriller_n , War = War_n , Western = Western_n)

			return redirect(user_home_page,user_name=user_name_n)

		except Exception as msg:

			uname = request.POST.get('uname')
			psw = request.POST.get('psw')

			if User.objects.filter(user_name=uname):
				if User.objects.filter(password=psw):
					return redirect(user_home_page,user_name=user_name_n)
				else:
					pass
			else:
				pass

	return render(request,'chat/home.html')


#/chat/{{username}}
def user_home_page(request,user_name):
	data = User.objects.get(user_name=user_name)
	print(data.first_name)

	context = {
		'fname' : data.first_name,
		'lname' : data.last_name,
		'uname' : data.user_name,
		'school' : data.school
    }

	return render(request,'chat/user_home_page.html', context)


def chatrooms(request,chatrooms,user_name):
	context = {
		'uname' : user_name,
		'chatroom_name' : chatrooms.title(),
    }
	return render(request,'chat/chatrooms.html', context)
