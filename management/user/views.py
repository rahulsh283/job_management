import email
from re import T
from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from user.models import ContactUs, Frontend
from user import models
from uuid import uuid4
import os
import json
from middleware.auth import auth_middleware
from django.utils.decorators import method_decorator
# from .models import UploadImage


# show home page for site
def index(request):
    return render(request, 'frontend/index.html')
# Create your views here.
def userTable(request):
    frontUser = models.Frontend.objects.all()
    res = {
        "error" : 0,
        "msg" : "User list fetch successfully",
        "data" : frontUser
    }
    return render(request, 'frontend/usertable.html', res)

def userRegistration(request, id=''):
   
    
    res = {
        "error" : 1,
        "msg" : 'Internal error'
    }
    if request.method == 'POST':
        data = request.POST
        fileData = request.FILES
        valid = True
        if 'first_name' in data and data['first_name']:
            first_name = data['first_name']
        else:
            res['error'] = 1
            res['msg'] = 'First name should not be blank'
            res['data'] = data
            valid = False

        if 'last_name' in data and data['last_name']:
        
            last_name = data['last_name']
        else:
            res['error'] = 1
            res['msg'] = 'Last name should not be blank'
            res['data'] = data
            valid = False


        if 'mobile_number' in data and data['mobile_number']:
            mobile_number = data['mobile_number']
        else:
            res['error'] = 1
            res['msg'] = 'Mobile No should not be blank'
            res['data'] = data
            valid = False

        if 'email_address' in data and data['email_address']:
            email_address = data['email_address']
        else:
            res['error'] = 1
            res['msg'] = 'Please fill valid Email Id'
            res['data'] = data
            valid = False

        if 'work_status' in data and data['work_status']:
            work_status = data['work_status']
        else:
            res['error'] = 1
            res['msg'] = 'Please select the work status'
            res['data'] = data
            valid = False
        print(fileData)

        
        if 'resume' in fileData and fileData['resume']:
            resume = fileData['resume']
            
            if not resume.name.endswith('.pdf' or '.doc' or '.docx' ):
                res['error'] = 1
                res['msg'] = 'Please submit your resume in correct format plz use .pdf or .doc or .docx'
                res['data'] = data
                valid = False
        
        
        if 'password' in data and data['password']:
            password = data['password']
        else:
            res['error'] = 1
            res['msg'] = 'password should not be empty'
            res['data'] = data
            valid = False

        confirm_password = data['confirm_password']

        

        country_id = data['country_id']
        state_id = data['state_id']

    
      
        if password != confirm_password:
            res['error'] = 1
            res['msg'] = 'Confirm password and password should be match'
            res['data'] = data
            valid = False
        
        if valid:
            try:

                frontend = Frontend()

                frontend.first_name = first_name
                frontend.last_name = last_name
                frontend.mobile_number = mobile_number
                frontend.email_address = email_address
                frontend.work_status = work_status
                frontend.country_id_id = country_id
                frontend.state_id_id = state_id
        
                frontend.password = make_password(password)
                frontend.save()
                if frontend.id:
                    frontend.upload_resume = resume
                    frontend.save()
                    res['error'] = 0
                    res['msg'] = 'You have registered successfully'
            except Exception as error:
                print(error)
                res['error'] = 1
                res['msg'] = 'Internal server error'
                res['data'] = data
                print(error)
        return JsonResponse(res)
    else:
        country = models.Country.objects.all()
        res = {
            "country_list" : country,
        }
        
        return render(request, 'frontend/userRegistration.html', res)

# this function is using to get state list according to country id
def stateByCountryID(request, id=''):
    res = {
        'error' : 1,
        'msg' : 'Internal server error'
    }
    

    if id :
        try:
            stateList = models.States.objects.filter(country_id=id).values()
            if stateList:
                res['error'] = 0
                res['msg'] = 'State list has been fetch successfully.'
                res['state_list'] = list(stateList)
        except Exception as error:
            res['error'] = 1
            res['msg'] = error
    else:
        res['error'] = 1
        res['msg'] = 'kindly pass country list'
    return JsonResponse(res)




def userLogin(request):
    
    
    res = {
        'error' : 1,
        'msg' : 'Internal Error',
    }
    if request.method == 'POST':
        data = request.POST
        try:
            userDetails = Frontend.objects.get(email_address = data['email_address'])
            # print(userDetails)
            if userDetails is not None:
                login_password = data['password']
                password = userDetails.password
                if check_password(login_password, password):
                    res['error'] = 0
                    res['msg'] = 'You have logged in successfully'
                    userData = {}
                    userData['id'] = userDetails.id
                    userData['email_address'] = userDetails.email_address
                    userData['first_name'] = userDetails.first_name
                    userData['last_name'] = userDetails.last_name
                    request.session['user_detail'] = userData
                    if userDetails.id:
                        return redirect('/user')
                else:
                    res['error'] = 1
                    res['msg'] = 'Username or Password should not match'
                    res['data'] = data
            else:
                res['error'] = 1
                res['msg'] = 'Username or Password should not match'
                res['data'] = data 
        except Exception as error:
            print(error)
            res['error'] = 1
            res['msg'] = 'Your email is not valid'
            res['data'] = data
        # print(res)
        return render(request, "frontend/userLogin.html", res)
    else:
        return render(request, "frontend/userLogin.html")


def contactUs(request):
    res = {
        'error' : 1,
        'msg' : 'Internal error found'
    }
    if request.method == 'POST':
        data = request.POST
        email_address = data['email_address']
        subject = data['subject']
        contact_description = data['contact_description']

        contactUs = ContactUs()
        contactUs.email_addres = email_address
        contactUs.subject = subject
        contactUs.description = contact_description

        contactUs.save()

        if contactUs.id:
            res['error'] = 0
            res['msg'] = 'Thanks for contacting us'
        else:
            res['error'] = 1
            res['msg'] = 'Your rquest is not send'

        return render(request, 'frontend/contact.html', res)
    else:
        return render(request, 'frontend/contact.html')


def userProfile(request):
    id = request.session['user_detail']['id']
    # print(id)
    userDetails = Frontend.objects.get(id=id)
    country_id = userDetails.country_id
    country = models.Country.objects.all()
    state = models.States.objects.filter(country_id=country_id)
    res = {
        "country_list" : country,
        'user_details' : userDetails,
        'state_list' : state

    }
    return render(request,"user/userProfile.html", res)

def userLogout(request):
    if 'user_detail' in request.session:
        del request.session['user_detail']
        return redirect('/login')
    else:
        return redirect('/login')
def userindex(request):
    return render(request , 'user/userindex.html')

def updateUserResume(request):
    res = {
        'error' : 1,
        'msg' : 'Internal server error'
    }
    try:

        id = request.session['user_detail']['id']
        # print(id)
        if id:
            fileData = request.FILES
            if 'user_resume' in fileData and fileData['user_resume']:
                resume = fileData['user_resume']
                
                if not resume.name.endswith('.pdf' or '.doc' or '.docx' ):
                    res['error'] = 1
                    res['msg'] = 'Please submit your resume in correct format plz upload pdf or doc or docx'
                    valid = False
                else:
                    userDetails = Frontend.objects.get(id=id)
                    userDetails.upload_resume = resume
                    userDetails.save()
                    res['error'] = 0
                    res['msg'] = 'Your Resume Updated Successfully'
                    file_path = userDetails.upload_resume.url
                    res['file_name'] = file_path
    except Exception as error:
        print(error)
        res['error'] = 1
        res['msg'] = 'You have not allow to update resume.'

    return JsonResponse(res)

def updateUserDetail(request):
    res = {
        "error" : 1,
        "msg" : "Internal Server Error"
    }
    try:
        id = request.session['user_detail']['id']
        print(id)
        if id:
            data = request.POST
            print(id)
            gender = data["gender"]
            mobile_number = data["mobile_number"]
            country_id = data["country_id"]
            state_id = data["state_id"]
            work_status = data["work_status"]

            userDetails = Frontend.objects.get(id=id)
            userDetails.gender = gender
            userDetails.mobile_number = mobile_number
            userDetails.country_id_id = country_id
            userDetails.state_id_id = state_id
            userDetails.work_status = work_status
            userDetails.save()
            print(userDetails)
            res["error"] = 0
            res['msg'] = "Your Profile updated successfully"
    except Exception as error:
        print(error)
        res['error'] = 1
        res['msg'] = 'Your Profile not updated '

    return JsonResponse(res)
 