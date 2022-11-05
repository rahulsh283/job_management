
from django.shortcuts import render,HttpResponse,redirect
from student.models import studentRegister
from django.http import JsonResponse
from student import models
from django.db.models import Q


# Create your views here.
def studentRegistration(request , id = ''):
    res = {
        "error" : 1,
        "msg" : "Internal Error"
    }

    if request.method == 'POST':
        data = request.POST
        valid = True
        roll_no = data['roll_no']
        student_name = data['student_name']
        class_name = data['class_name']
        section_name = data['section_name']
        mobile_no = data['mobile_no']
        email_address = data['email_address']
        course = data['course']
        year = data['year']
        semester = data['semester']
        gender = data['gender']
        join_date = data['join_date']

        

        try:
            
            if 'student_id' in data and data['student_id']:
                
                studentRollno = studentRegister.objects.get(~Q(id=data['student_id']), roll_no=data["roll_no"])
                
            else:
                
                studentRollno = studentRegister.objects.get(roll_no = data["roll_no"])
            
            if studentRollno:
                res['error'] = 1
                res['msg'] = "This Roll No already exist"
                valid = False
                print(studentRollno)
        except Exception as error:
            pass

        try:
            if 'student_id' in data and data['student_id']:

                studentDetail = studentRegister.objects.get(~Q(id = data['student_id']) , email_address = data['email_address'])
            else:
                studentDetail = studentRegister.objects.get(email_address = data['email_address'])

            if studentDetail:
                res["error"] = 1
                res["msg"] = "Email id already exist"
                valid = False
            
        except Exception as error:
            pass
        

        if valid:
            try:
                
                if 'student_id' in data and data['student_id']:

                    studentregister = studentRegister.objects.get(id=data['student_id'])
                else:

                    studentregister = studentRegister()

                studentregister.roll_no = roll_no
                studentregister.student_name = student_name
                studentregister.class_name = class_name
                studentregister.section_name = section_name
                studentregister.mobile_no = mobile_no
                studentregister.email_address = email_address
                studentregister.course = course
                studentregister.year = year
                studentregister.semester = semester
                studentregister.gender = gender
                studentregister.join_date = join_date

                studentregister.save()
                if studentregister.id :
                    res['error'] = 0
                    res['msg'] = 'you have registered successfully'
                
            except Exception as error:
                res['error'] = 1
                res['msg'] = 'you have not registered'
                
        return  JsonResponse(res)
    else:
        if id :
            student_details = studentRegister.objects.get(id=id)
        else:
            student_details = {}

        return render (request , 'user/studentRegister.html', 
        {
            'semester_count':range(1, 9),
            'student_details' : student_details,
            'id' : id
        })

def studentdata(request):
    studentDetail = models.studentRegister.objects.all()
    res = {

        'error' : 0,
        'msg' : 'Student data fetch successfully',
        'data': studentDetail

    }
    return render(request , 'user/studentData.html' ,res)

def studentDelete(request , id = ''):
    try:
        student_delete = studentRegister.objects.get(id=id)
        student_delete.delete()
        res = {

        'error' : 0,
        'msg' : 'Student data delete successfully',

        }
        # return redirect('/user/students')
        return JsonResponse(res)
    except Exception as error:
        # return redirect('/user/students')
        pass

