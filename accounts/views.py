from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

# SignUp Page
def signup(request):
    print('IN REGISTER METHOD')

    if request.method == 'POST':

        print('POST Request Recieved')

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        comfirm_password = request.POST['comfirm_password']

        # Check If Both Passwords Match
        if password == comfirm_password:

            # Check If Username Is Already In DataBase
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print(' ')
                print('|| Username Taken ||')
                print(' ')
                return redirect('/accounts/signup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                print(' ')
                print('|| Email Taken ||')
                print(' ')
                return redirect('/accounts/signup/')
            
            else:
                user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    password = password,
                    email = email
                )
                user.save()
                print(' ')
                print('|| Password Matching ||')
                print('||| Registration Successful, New User Created ||')
                print(' ')
                # To call the Home Page
                return redirect('/accounts/login/')
            

        else:
            messages.info(request, 'Password Not Matching')
            print(' ')
            print('||| Passwords Not Matching |||')
            print(' ')
            return redirect('/accounts/signup/')

    else:
        print('Get Request Recieved')
        return render(request, 'signup.html') 



# Login Page
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username = username,
            password = password
        )

        if user is not None:
            auth.login(request, user)
            print(' ')
            print(' || Login Successfull || ')
            print(' ')
            return redirect('/eComm')
        else:
            messages.info(request, 'Invalid Credentials')
            print(' ')
            print(' || Wrong Credentials || ')
            print(' ')
            return redirect('/accounts/login/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/eComm/')



# Account Page
def accounts_Page(request):
    return render(request, 'accounts.html')



