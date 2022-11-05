import email
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from Employee.models import Employee
# Create your views here.
def add_employee(request):
    res = {
        'error': 1,
        'msg': 'internal error found'
    }
    
    if request.method == 'POST':
        data = request.POST
        valid = True
        company_name = data['company_type']
        official_email = data['official_email']
        mobile_number = data['mobile_number']
        contact_person_name = data['contact_person_name']
        pin_code = data['pin_code']
        company_type = data['company_type']
        GSTIN = data['GSTIN']
        password = data['password']
        confirm_password = data['confirm_password']

        if password != confirm_password:
            res['error'] = 1
            res['msg'] = "Confirm password and password should be match"
            res['data'] = data
            valid = False

        if valid:
            try:

                employee = Employee()

                employee.company_name = company_name
                employee.official_email =official_email 
                employee.mobile_number = mobile_number
                employee.Contact_person_name = contact_person_name
                employee.pin_code = pin_code
                employee.company_type =company_type
                employee.GSTIN = GSTIN
                employee.password = make_password(password) 
                employee.save()
                if employee.id :
                    res['error'] = 0
                    res['msg'] = "You hane successfully registered"

            except Exception as error:
                res['error'] = 1
                res['msg'] = "You have not registered"
                print(error)
    else:
        return render(request,'frontend/employee.html')
    return JsonResponse(res)

def users(request):
    return render(request,'frontend/index2.html')
            
            
def employeelogin(request):
    res = {
        'error' : 1,
        'msg' : "Internal Error",
    }

    if request.method == "POST":
        data = request.POST

        try:
            employerDetails = Employee.objects.get(official_email = data["official_email"])
            if employerDetails is not None:
                login_password = data['password']
                password = employerDetails.password
                if check_password(login_password, password):
                    res['error'] = 0
                    res['msg'] = "You have logged in successfully"
                    employerData = {}
                    employerData['id'] = employerDetails.id
                    employerData['official_email'] = employerDetails.official_email
                    request.session['employer_detail'] = employerData
                    if employerDetails.id:
                        return redirect('/employee/user')
                else:
                    res['error'] = 1
                    res['msg'] = "Username and Password should not match"
                    res['data'] = data

            else:
                res['error'] = 1
                res['msg'] = 'Username or Password should not match'
                res['data'] = data
        
        except Exception as error:
            res['error'] = 1
            res['msg'] = "Your Email is not valid"
            res['data'] = data

        return render(request,'frontend/login_employer.html',res)
    else:
        return render(request,'frontend/login_employer.html')