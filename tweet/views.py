from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.


#Website Launcher View

def launcher(request):
    return render(request, 'tweet/launcher.html')
    
# User Signup 

def signuphandle(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']

        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, "Successfully created twitter account, Now you can login !!!!!")
        return redirect('login')

    else:
        return render(request,'tweet/signup.html')



# User Login       
def loginhandle(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Succefully logged into the Twitter !!!!")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again later")
            return redirect('login')
    else:
        return render(request,'tweet/login.html')



#User Logout

def logouthandle(request):
    logout(request)
    messages.success(request,"Successfully Logged Out !!!!")
    return redirect('launcher')


#After Successful Login the Restricted content Shows to logged in users

def home(request):
    tweet = Tweet.objects.all()
    rtweet=reversed(tweet)
    context = {'tweet': rtweet}
    return render(request, 'tweet/home.html', context)

# Creating Tweet

def mytweet(request):
    if request.method=='POST':
        content = request.POST.get('tweet')
        user=request.user
        newtweet = Tweet(content=content,author=user)
        newtweet.save()
        return redirect('tweethandle')
        
    return render(request, 'tweet/mytweet.html')
    
def tweethandle(request):
    alldata = Tweet.objects.filter(author=request.user)
    rtweet = reversed(alldata)
    context = {'tweet': rtweet}
    return render(request, 'tweet/updatedelete.html', context)


#Updating Tweet

def updatetweet(request, id):
    tweet = get_object_or_404(Tweet, id=id)
    context = {
        'tweet':tweet
    }
    tweet.delete()
    return render(request,'tweet/tweetupdate.html',context)

#deleting tweet
    
def deletetweet(request, id):
    tweet=get_object_or_404(Tweet,id=id)
    tweet.delete()
    return redirect('tweethandle')
        
# About page
     
def about(request):
    return render(request,'tweet/about.html')
    
