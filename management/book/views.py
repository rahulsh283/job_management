
from book import models
from django.shortcuts import render,HttpResponse,redirect
from book.models import Books,Student_info
from django.http import JsonResponse
# Create your views here.
def studentbook(request , id=''):
    res = {
       'error' : 1,
       'msg' : 'Internal error found'
    }

    if request.method == 'POST':
        data = request.POST
        valid = True

        book_name = data['book_name']
        writer_name = data['writer_name']
        price  = data['price']
        vander_name = data['vander_name']
        purchase_date  = data['purchase_date']

        if valid:
            try: 
                if 'books_id' in data and data['books_id']:
                    books = Books.objects.get(id=data['books_id'])
                else:

                    books = Books()
                books.book_name = book_name
                books.writer_name = writer_name
                books.price =  price
                books.vander_name = vander_name
                books.purchase_date = purchase_date 

                books.save()
                if books.id:
                    res['error'] = 0
                    res['msg'] = 'Thanks for studentbook us'
                    print(res)
            except Exception as error:
                res['error'] = 1
                res['msg'] = 'Your rquest is not send'  
        return JsonResponse(res)

    else:
        if id:
            book_details = Books.objects.get(id=id)
        else:
            book_details = {}

    return render(request , 'frontend/book.html',
    {
        'book_details' : book_details,
        'id' : id

    })
    
    
   


def addtable(request):
    booklist = models.Books.objects.all()
    res = {
        "error" : 0,
        "msg" : "User list fetch successfully",
        "data" : booklist
    }
    return render(request, 'frontend/table.html', res)


def delete_book(request , id =''):

        try:
            book_details = Books.objects.get(id=id)
            book_details.delete()
            res = {
                'error':0,
                'msg': 'Book deleted successfully'
                }
            
            

        except Exception as error:
            pass
        return redirect('/user/books/table')
        

        

def student_information(request):
    data = request.POST  # it is use for intry store in database.
    student_name = data['student_name']
    student_class = data ['student_class']
    mother_name = data['mother_name']
    father_name = data['father_name']
    admission_date = data['admission_dat']
    email_address = data['email_address']

    student_info = Student_info()
    student_name = student_name
    student_class = student_class
    mother_name = mother_name
    father_name = father_name
    admission_date = admission_date
    email_address = email_address 

    student_info.save()
    return render(request,'frontend/student_inf0.html')