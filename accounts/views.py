from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from carts.models import Cart
from products.models import Product
from accounts.models import Profile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
import smtplib

def register(requset):
    if requset.method == "POST":
        first_name = requset.POST['first_name']
        last_name = requset.POST['last_name']
        email = requset.POST['email']
        emailId = requset.POST['email-id'] 
        password = requset.POST['password']
        cnfpassword = requset.POST['cnfpassword']
        if password == cnfpassword:
            if User.objects.filter(username = email).exists():
                messages.info(requset, "Username Taken")
                return render(requset, 'Register.html')
            else:
                if email == "" or password == "" or first_name == "" or last_name == "":
                    messages.info(requset, "Please Fill Out All the Fields")
                    return render(requset, 'Register.html')
                else:
                    user = User.objects.create_user(username = email, password = password, first_name = first_name, last_name = last_name, email = emailId)
                    user.save()
                    messages.info(requset, "User Created")
                    return redirect('/accounts/')
        else:
            messages.info(requset, "Passwords Not Matching")
            return redirect('/accounts/register/')
    else:
        return render(requset , 'Register.html')

def login(requset):
    if requset.method == "POST":
        email = requset.POST['username']
        password = requset.POST['password']
        idCardNo  = requset.POST['id-card-no'] 
        user = auth.authenticate(username = email, password = password, IdCardNo = idCardNo)
       
        if user is not None:
            auth.login(requset, user)
            return redirect('/products')
        else:
            messages.info(requset, "Invalid Credentials")
            return redirect('/accounts/')
    else:
        return render(requset, 'Login.html')
    

def logout(requset):
    cart = Cart.objects.all()[0]
    profile = Profile.objects.get(user = requset.user)
    print(cart)
    if requset.user.profile.balance >= cart.total: 
        requset.user.profile.balance -= cart.total
        requset.user.profile.save()
        product = Product.objects.all()
        # sendto_mail = requset.user.email
        # if sendto_mail == "":
        #     sendto_mail = 'shubhamkukreja1111@gmail.com'
        # print(sendto_mail)
        # content = "Subject : Transaction Alert\n\n" + "Hello " + requset.user.first_name + ",\n" + "Your Order :\n "
        # for item in cart.products.all():
        #     content += str(item.title) + " x "
        #     content += str(item.quantity) + "\n"
        # content += "You have spent Rs." + str(cart.total)
        # mail = smtplib.SMTP('smtp.gmail.com', 587)
        # mail.ehlo()
        # mail.starttls()
        # mail.login('skukreja434@gmail.com', 'vijan5562')
        # mail.sendmail('skukreja434@gmail.com', sendto_mail, content)
        # mail.close()
        for item in product:
            cart.products.remove(item)
        cart.total = 0
        cart.save()
        print(requset.user.profile.balance)
        
        auth.logout(requset)
        return redirect('/accounts/')
    else:
        messages.info(requset, "Amount Exceeded")
        return redirect('/products')

# def cart(request):
#     return render(request, 'cart.html')

# Create your views here.
