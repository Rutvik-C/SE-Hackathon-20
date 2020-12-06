
from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Authority.models import Belongs,problem,otherDetails,Cities
from Authority.forms import Registerdetail,otherDetails,problem
from .forms import Rate, UploadFileForm
from .models import rate, problem_selected
from datetime import timedelta
from django.core.mail import send_mail
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

def Email(username,email):
    send_mail(
        subject = "alert",
        message = f'thanks {username} for joining us. Your account has been successfully created login for more details',
        from_email = "ranadeamr@gmail.com",
        recipient_list = [email],
        fail_silently = False,
    )
def send(username,email,quantity):
    send_mail(
        subject = "alert",
        message = f'thanks {username} for the food you provided. {quantity} number of people have been fed !',
        from_email = "ranadeamr@gmail.com",
        recipient_list = [email],
        fail_silently = False,

    )
def mailtoo(email,username):
    send_mail(
        subject = "alert",
        message = f'NGO {username} will come to collect the food order has been confirmed',
        from_email = "ranadeamr@gmail.com",
        recipient_list = [email],
        fail_silently = False,
    )

def index(request):
    return render(request,'Student/index.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists try with a new one !")
            return redirect('signup')
        if(len(username)<2 or len(username)>20):
            messages.error(request,"Username doesnt match the requirements")
            return redirect('signup')
        if(password!=password1):
            messages.error(request,"Both passwords dont match")
            return redirect('signup')
        myuser=User.objects.create_user(username,email,password)
        belong = Belongs(user=myuser,is_student =  True)
        belong.save()
        myuser.save()
        Email(username,email)
        form= Registerdetail(request.POST ,request.FILES)
        if form.is_valid():
                object = form.save(commit=False)
                object.user = myuser
                object.save()
        
        messages.success(request,"Your account has been successfully created")
        return redirect("/Student/login")
        
    else:
        form = Registerdetail()
        return render(request,'Student/signup.html',{"form":form})

def login_u(request):
    return render(request,'Student/login.html')
    
def logout_u(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("/Student/login")


def loginpage(request):
    if request.method=="POST":
        #s=problem.objects.get(city=request.user.city)
        now = timezone.now()
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            if Belongs.objects.get(user = user).is_student:
                login(request,user)
                details=otherDetails.objects.filter(user=request.user).values_list('city')
                for d in details:
                    s=Cities.objects.get(pk=d[0])
                
                j=problem.objects.all()
                print(j)
                h=problem_selected.objects.all()
                print(h)
                parameter={'j':j,'h':h}
                messages.success(request,"Successfully Logged in")
                return render(request,'Student/loginpage.html',parameter)
            else:
                messages.error(request,"Wrong credentials,Please try again !")
                return render(request,'Student/login.html')

        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'Student/login.html')
    if request.user.is_authenticated:
        details=otherDetails.objects.filter(user=request.user).values_list('city')
        for d in details:
            s=Cities.objects.get(pk=d[0])
        j=problem.objects.all()
        print(j)
        h=problem_selected.objects.all()
        print(h)
        
        parameter={'j':j}
        messages.success(request,"Successfully Logged in")
        return render(request,'Student/loginpage.html',parameter)
    else:
        messages.success(request, "You need to login to access this")
        return render(request, 'Student/login.html')

def displaypage(request,id):
    # form = FoodRequest()
    y=problem.objects.filter(id=id)
    print(y)    
    return render(request,'Student/thankyou.html',{'y':y})

def handle_uploaded_file(f):
    with open('Student/documents/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_soln(request,id):
    m = id
    y = problem.objects.get(id=id)
    j = problem.objects.all()
    if(request.method=="POST"):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            (handle_uploaded_file(request.FILES['file']))
            z = problem_selected(p_id=id,user=y.user,problem_title=y.problem_title)
            z.pdf = request.FILES['file']
            z.save()
            return render(request, 'Student/loginpage.html' ,{'j':j})
    else:
        form = UploadFileForm()        
        z = problem_selected(p_id=id,user=y.user,problem_title=y.problem_title)
        z.save()
    return render(request, 'Student/upload_soln.html', {'form': form,'y':y})

        # return render(request,'Student/upload_soln.html',{})

# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })

# def status1(request,id):
#     if(request.method=="POST"):
#         form=FoodRequest()
#         m=id
#         y=problem.objects.filter(id=id).values_list("quantity")
#         h=problem.objects.get(id=id)
#         form= FoodRequest(request.POST ,request.FILES)
#         if(int(form['quantity_required'].value())>int(y[0][0])):
#             print("HIIIIIIIIIIIIIIIIII")
#             messages.error(request,"Cant be greater than available food")
#             form = FoodRequest()
#             y=problem.objects.filter(id=id)
#             return render(request,'Student/thankyou.html',{'form':form,'y':y})
#         elif(int(form['quantity_required'].value())<int(y[0][0])):
#             if form.is_valid():    
#                 a=problem_selected(O_ID=id,user=h.user,quantity=int(form['quantity_required'].value()),pickup_address=h.pickup_address,s=1)
#                 a.save()
#                 print(a)
#                 object = form.save(commit=False)
#                 object.user = request.user
#                 object.save()
#                 object.foodtakenfrom=m
#                 object.save()
#                 u=int(y[0][0])-int(form['quantity_required'].value())
#                 print(u)    
#                 h.quantity=u
#                 h.save()
#                 messages.success(request,"Response Noted")
#                 y=problem.objects.filter(id=id)
#                 y1=problem.objects.get(id=id) 
#                 parameter={'y':y,'y1':y1}
#                 return render(request,"Student/status1.html",parameter)   
#         else:
#             messages.success(request,"Form invalid")
#             return render(request,"/Student/thankyou.html")
#     else:
#         y=problem.objects.filter(id=id)
#         y1=problem.objects.get(id=id) 
#         parameter={'y':y,'y1':y1}   
#         return render(request,"Student/status1.html", parameter)

# # def feedback(request,id):
# #     if(request.method=="POST"):
# #         print("Hi")
# #         print("%%%%%%%%%%")
# #         y=problem.objects.get(id=id)
# #         email=y.user.email
# #         form= Rate(request.POST ,request.FILES)
# #         if form.is_valid():
# #             object = form.save(commit=False)
# #             quantity= form.instance.fedto
# #             object.user=y.user
# #             object.save()
# #             send(y.user.username,email,quantity)
# #             return HttpResponse("Well Done !")
# #         else:
# #             return HttpResponse("Bad Work")    
# #     else:
# #         form = Rate()
# #         y=problem.objects.filter(id=id) 
# #         return render(request,"Student/rate.html",{'form':form,'y':y})

    
# def status2(request,id):
#     y=problem.objects.filter(id=id)
#     y1=problem.objects.get(id=id) 
#     parameter={'y':y,'y1':y1}
#     if(request.method=="POST"):
#         email=y1.user.email
#         username=request.user
#         mailtoo(email,username) 
#         a=problem_selected.objects.get(O_ID=id)    
#         a.s=2
#         a.save()
#         return render(request,"Student/status2.html",parameter)
#     else:
#         return render(request,"Student/status2.html",parameter)

# def status3(request,id):
#     y=problem.objects.filter(id=id)
#     y1=problem.objects.get(id=id) 
#     parameter={'y':y,'y1':y1}
#     if(request.method=="POST"):       
#         a=problem_selected.objects.get(O_ID=id)     
#         a.s=3
#         a.save()
#         return render(request,"Student/status3.html",parameter)
#     return render(request,"Student/status3.html",parameter)
    
# def status4(request,id):
#     y=problem.objects.filter(id=id)
#     y1=problem.objects.get(id=id) 
#     parameter={'y':y,'y1':y1}
#     if(request.method=="POST"):
#         email=y1.user.email
#         form = Rate(request.POST ,request.FILES)
#         if form.is_valid():
#             object = form.save(commit=False)
#             quantity= form.instance.fedto
#             object.user=y1.user
#             object.save()
#             a=problem_selected.objects.get(O_ID=id)     
#             a.s=4
#             a.save()
#             send(y1.user.username,email,quantity)
#             messages.success(request,"You have completed the campaign. GOOD WORK!")
#             return render(request,"Student/status4.html",parameter)
#         else:
#             messages.success(request,"You couldn't complete the campaign. TRY AGAIN!")
#             return render(request,"Student/status4.html",parameter)  
#     else:
#         form = Rate()
#         y=problem.objects.filter(id=id) 
#         return render(request,"Student/rate.html",{'form':form,'y':y})
