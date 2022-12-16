from django.shortcuts import render,HttpResponse,redirect
import random


def index(request):
   if not 'random_num' in request.session:

      request.session['random_num']=random.randint(1,100)
      print(request.session['random_num'])

   return render(request,'basic.html')

def validate(request,num):

   num=request.POST["num"]
   if num < request.session['random_num']:
      status = 'Too Low'

   elif num > request.session['random_num']:
      status = 'Too High'
   
   else :
      status='Success'
      request.session['num']=num
   request.session['status']=status

   redirect ('/')


