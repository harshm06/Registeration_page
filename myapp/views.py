from django.http import HttpResponse
from myapp.models import details,user
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json




# Create your views here.

def myfunc(request):

	if request.method == 'POST':
		data = json.loads(request.body)
		obj=user.objects.all()

		for x in obj:
			if(x.username==data['username'] and x.password==data['password']):
				d=user.objects.filter(username=data['username']).values('link__fname','link__lname','link__address','link__city','link__state','link__zip1','link__board','link__qualified','link__mobileno','link__email','link__gender')
				# data2=details.objects.filter(id=d[0]['link']).values('fname','lname','address','city','state','zip1','board','qualified','mobileno','email','gender')
				return JsonResponse(list(d), safe=False)


			elif(x.username==data['username'] and x.password!=data['password']):
				data3={"pass":"wrong"}
				return JsonResponse(data3)


		try:		
			query = details.objects.create(fname=data['fname'],lname=data['lname'],address=data['address'],city=data['city'],state=data['state'],zip1=data['zip1'],board=data['board'],qualified=data['qualified'],mobileno=data['mobileno'],email=data['email'],gender=data['gender'])
			query2=user.objects.create(username=data['username'],password=data['password'],link=query)
			if(query.fname==data['fname']):
				data1 = {"status1": "ok"} 
				return JsonResponse(data1)

		except:
			q={"username":"invalid"}
			return JsonResponse(q)
		


		

	elif request.method == 'GET':
		# fname1 = request.GET.get('fname', '1')
		# lname1 = request.GET.get('lname', '1')
		# mobileno1 = request.GET.get('mobileno', '1')
		# email1 = request.GET.get('email', '1')
		# Qualified1 = request.GET.get('Qualified', '1')
		# query = details.objects.create(fname=fname1 ,lname=lname1, mobileno=mobileno1, email=email1, Qualified=Qualified1)
		# return HttpResponse("GET se chalega")

		obj1 = details.objects.filter().values('fname','lname','address','city','state','zip1','board','qualified','mobileno','email','gender')
		return JsonResponse(list(obj1), safe=False)


	
	# elif request.method == 'PUT':			
	# 	id1 = json.loads(request.body)
	# 	query = details.objects.filter(id=id1['id']).update(fname="Narendra",lname="modi",id=3)
	# 	return HttpResponse("put se update hua hai")

	# elif request.method == 'DELETE':			
	# 	id1 = json.loads(request.body)
	# 	query = details.objects.filter(id=id1['id']).delete()
	# 	return HttpResponse("gaya")


def home_page(request):
	return HttpResponse("Welcome to home page")
