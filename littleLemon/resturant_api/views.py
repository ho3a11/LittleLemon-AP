from django.shortcuts import render,redirect
from . models import Booking,Menu
from . forms import BookingForm
from rest_framework import generics
from .serializers import BookingSerializer,RegistrationSerializer , MenuSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout


# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


@login_required
def book(request):
    if request.user.is_authenticated:
        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form':form}
        return render(request, 'book.html', context=context)
    else :
        return redirect('login')

def menu(request):
    menu = Menu.objects.all().order_by('name')
    context = {'menu':menu}
    return render(request , 'menu.html' , context=context)
    

def menu_detail(request,pk=None):
    menu_item = Menu.objects.get(id=pk)
    context = {'menu_item':menu_item}
    return render(request, 'menu_item.html', context=context)




class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer





#Login user


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Invalid login credentials
            pass
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



