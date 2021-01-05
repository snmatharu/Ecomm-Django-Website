from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    
    def post(self, request):
        email= request.POST.get('email')
        password= request.POST.get('password')
        customer = Customer.checkCred(email)
        if customer:
            flag= check_password(password,customer.password)
            if flag:
                request.session['customer'] = customer.id
                # request.session['email'] = customer.email

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    return redirect('homepage') 
            else:
                error_message='Email and Password invalid'    
        else:
            error_message='Email and Password invalid'

        data={'error':error_message}
        
        return render(request, 'login.html', data)
