# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

from .models import *


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        interested_product = request.POST.get('interested_product')
        message = request.POST.get('message')

        # Here you can handle the data, e.g., save it to the database
        # For this example, I'll just print it to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Address: {address}")
        print(f"City: {city}")
        print(f"State: {state}")
        print(f"Country: {country}")
        print(f"Interested Product: {interested_product}")
        print(f"Message: {message}")

        data = Enquiry(name=name, email=email, phone=phone, address=address, city=city, state=state, country=country,
                       interested_product=interested_product, message=message)
        data.save()
        # Send email
        #     subject = 'New Enquiry'
        #     email_message = f"""
        #             Name: {name}
        #             Email: {email}
        #             Phone: {phone}
        #             Address: {address}
        #             Interested Product: {interested_product}
        #             Message: {message}
        #             """
        #     from_email = 'your_email@gmail.com'
        #     recipient_list = ['parthghantala1999@gmail.com']
        #
        #     send_mail(subject, email_message, from_email, recipient_list)

        send_mail(
            'Testing Mail',
            f"""
                        Name: {name}
                        Email: {email}
                        Phone: {phone}
                        Address: {address}
                        City: {city}
                        State: {state}
                        Country: {country}
                        Interested Product: {interested_product}
                        Message: {message}
                        """,
            'settings.EMAIL_HOST_USER',
            ['info@prravishinternational.com'],
            fail_silently=False
        )
        messages.success(request, 'Form submitted successfully!')
        return render(request, 'index.html', {'name': name,
                                              'email': email,
                                              'phone': phone,
                                              'address': address,
                                              'city': city,
                                              'state': state,
                                              'country': country,
                                              'interested_product': interested_product,
                                              'message': message})
    return render(request, 'index.html')


def products(request):
    starter = MenuStarter.objects.all()
    main_course = MenuMain.objects.all()
    drinks = MenuDrinks.objects.all()
    offers = MenuOffers.objects.all()
    special = MenuSpecial.objects.all()
    return render(request, 'products.html', {'starter': starter,
                                             'main_course': main_course,
                                             'drinks': drinks,
                                             'offers': offers,
                                             'special': special})
