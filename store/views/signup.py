from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData=request.POST
        first_name= postData.get('firstname')
        last_name= postData.get('lastname')
        phone= postData.get('phone')
        email= postData.get('email')
        password= postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer=Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password )

        error_message = self.validationCustomer(customer)
        if not error_message:
            print(first_name,last_name,phone,email,password)
            customer.password=make_password(customer.password)
            customer.register()

            return redirect('homepage') 
        else:
            data={'error':error_message,
                  'values':value
                  }

            return render(request, 'signup.html', data)

    def validationCustomer(self, customer):
        error_message = None

        first_name=customer.first_name
        last_name=customer.last_name
        phone=customer.phone
        email=customer.email
        password=customer.password
        if(not first_name):
            error_message="First name required"
        elif first_name:
            if len(first_name) < 4:
                error_message='First name must be 4 char long'
        if (not last_name):
            error_message = 'Last Name Required'
        elif (len(last_name) < 4):
            error_message = 'Last Name must be 4 char long or more'
        elif not phone:
            error_message = 'Phone Number required'
        elif len(phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(email) < 5:
            error_message = 'Email must be 5 char long'
        elif Customer.isExists(customer.email):
            error_message = 'Email Address Already Registered!'
    
        return error_message
        #saving
        