
from ecomapp.models import Category, Product, CartItem, Cart, Images, MailBox
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, ContactFormCall


# Create your views here.
def feedbackcall(reguest):
    if reguest.method == 'POST':
        form = ContactFormCall(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recepients = ['rufedor@mail.ru']

            # Положим копию письма в базу данных
            MailBox.objects.create(subject=subject, phone=phone, message=message, copy=copy)

            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            try:
                send_mail(subject, message, phone, ['rufedor@mail.ru'] , recepients)

            except BadHeaderError: #Защита от уязвимости
                return render(reguest, 'feedback_error.html', {'form': form})
                # print("ne rabotaet")
            # Переходим на другую страницу, если сообщение отправлено
            return render(reguest, 'thanks.html', {'form': form})
    else:
        form = ContactFormCall()
    # Выводим форму в шаблон
    return render(reguest, 'base.html', {'form': form})


def feedback(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recepients = ['rufedor@mail.ru']

            # Положим копию письма в базу данных
            MailBox.objects.create(subject=subject, sender=sender, phone=phone, message=message, copy=copy)

            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:

                send_mail(subject, message, phone, ['rufedor@mail.ru'] , recepients)

            except BadHeaderError: #Защита от уязвимости
                return render(reguest, 'feedback_error.html', {'form': form})
                # print("ne rabotaet")
            # Переходим на другую страницу, если сообщение отправлено
            return render(reguest, 'thanks.html', {'form': form})




    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'o_nas.html', {'form': form})
# Create your views here.

def base_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    image = Images.objects.get()
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {

        'categorise': categories,
        'products': products,
        'cart': cart,
        'form': form,
        'image': image
    }

    return render(request, 'base.html', context)


def product_view(request, product_slug):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    cart = Cart.objects.first()
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categorise': categories,
        'cart': cart,
        'form': form
    }

    return render(request, 'product.html', context)


def category_view(request, category_slug):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    category = Category.objects.get(slug=category_slug)
    product_of_category = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        #   'category': category,
        'product_of_category': product_of_category,
        'categorise': categories,
        'form': form
    }
    return render(request, 'category.html', context)


def cart_view(request):
    cart = Cart.objects.first()
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)


def add_to_cart_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    new_item, _ = CartItem.objects.get_or_create(product=product, item_tottal=product.price)
    cart = Cart.objects.first()
    if new_item not in cart.item.all():
        cart.item.add(new_item)
        cart.save()
        return HttpResponseRedirect('/cart/')

def thanks(request):

    return render(request, 'thanks.html')

def feedback_error(request):

    return render(request, 'feedback_error.html')


def o_nas(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart,
        'form': form
    }
    return render(request, 'o_nas.html', context)

def images(request):
    image = Images.objects.get()
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'image': image,
        'categorise': categories,
        'products': products,
        'cart': cart
    }

    return render(request, 'contact.html', context)
def contact(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    image = Images.objects.get()
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart,
        'form': form,
        'image': image,
    }
    return render(request, 'contact.html', context)




def online_diagnos(request):


    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart,
        'form': form
    }
    return render(request, "online_diagnos.html", context)
 #   return render(request, "online_diagnos.html", context, {'form': form})





def base2(request):
    cart = Cart.objects.first()
    product = Product.objects.get()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart,
        'product': product,
    }
    return render(request, 'test.html', context)


