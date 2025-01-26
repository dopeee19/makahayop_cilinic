# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.db.models import Count, Avg
from .models import Appointment, Service, Vet, Feedback,User

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')



def home(request):
    services = Service.objects.all()
    vets = Vet.objects.all()
    return render(request, 'first.html', {'services': services, 'vets': vets})


@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment/appointment_list.html', {'appointments': appointments})
@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment/appointment_detail.html', {'appointment': appointment})
@login_required
def appointment_create(request):
    if request.method == "POST":
        pet_name = request.POST.get('pet_name')
        owner_name = request.POST.get('owner_name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')

        Appointment.objects.create(
            pet_name=pet_name,
            owner_name=owner_name,
            date=date,
            time=time,
            description=description
        )
        return redirect('home')

    return render(request, 'appointment/appointment_form.html')
@login_required
def customerappointment_create(request):
    if request.method == "POST":
        pet_name = request.POST.get('pet_name')
        owner_name = request.POST.get('owner_name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')

        Appointment.objects.create(
            pet_name=pet_name,
            owner_name=owner_name,
            date=date,
            time=time,
            description=description
        )
        return redirect('home')

    return render(request, 'appointment/customerappointment.html')
@login_required
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == "POST":
        appointment.pet_name = request.POST.get('pet_name')
        appointment.owner_name = request.POST.get('owner_name')
        appointment.date = request.POST.get('date')
        appointment.time = request.POST.get('time')
        appointment.description = request.POST.get('description')
        appointment.save()
        return redirect('appointment_list')

    return render(request, 'appointment/appointment_form.html', {'appointment': appointment})
@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointment/appointment_confirm_delete.html', {'appointment': appointment})



@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})
@login_required
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

@login_required
def service_create(request):
    if request.method == "POST":
        # Get the data from the form
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        # Handle the image file if it exists
        if 'image' in request.FILES:
            pimage = request.FILES['image']
        else:
            pimage = None

        # Create the new service in the database
        Service.objects.create(name=name, description=description, price=price, image=pimage)
        
        # Redirect to the service list page
        return redirect('service_list')

    # Handle GET request to display the form
    return render(request, 'services/service_form.html')

@login_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == "POST":
        service.name = request.POST.get('name')
        service.description = request.POST.get('description')
        service.price = request.POST.get('price')

        if 'image' in request.FILES:
            service.image = request.FILES['image']
        else:
            service.image = None

        service.save()
        return redirect('service_list')

    return render(request, 'services/service_form.html', {'service': service})
@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        service.delete()
        return redirect('service_list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})






@login_required
def vet_list(request):
    vets = Vet.objects.all()
    return render(request, 'vets/vet_list.html', {'vets': vets})
@login_required
def vet_detail(request, pk):
    vet = get_object_or_404(Vet, pk=pk)
    return render(request, 'vets/vet_detail.html', {'vet': vet})
@login_required
def vet_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        specialty = request.POST.get('specialty')
        contact_number = request.POST.get('contact_number')

          # Handle the image file if it exists
        if 'image' in request.FILES:
            pimage = request.FILES['image']
        else:
            pimage = None

        Vet.objects.create(name=name, specialty=specialty, contact_number=contact_number,image=pimage)
        return redirect('vet_list')

    return render(request, 'vets/vet_form.html')
@login_required
def vet_update(request, pk):
    vet = get_object_or_404(Vet, pk=pk)

    if request.method == "POST":
        vet.name = request.POST.get('name')
        vet.specialty = request.POST.get('specialty')
        vet.contact_number = request.POST.get('contact_number')


        if 'image' in request.FILES:
            vet.image = request.FILES['image']
        else:
            vet.image = None

        vet.save()
        return redirect('vet_list')

    return render(request, 'vets/vet_form.html', {'vet': vet})
@login_required
def vet_delete(request, pk):
    vet = get_object_or_404(Vet, pk=pk)
    if request.method == "POST":
        vet.delete()
        return redirect('vet_list')
    return render(request, 'vets/vet_confirm_delete.html', {'vet': vet})



# views.py

@login_required
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedbacks/feedback_list.html', {'feedbacks': feedbacks})

@login_required
def feedback_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        description = request.POST.get('description')
        contactdetails = request.POST.get('contact')

        Feedback.objects.create(name=name, rating=rating, description=description, contact_details=contactdetails)
        return redirect('home')

    return render(request, 'feedbacks/feedback_form.html')




@login_required
def dashboard_view(request):
    total_appointments = Appointment.objects.count()
    total_services = Service.objects.count()
    total_vets = Vet.objects.count()
    avg_rating = Feedback.objects.aggregate(Avg('rating'))['rating__avg'] or 0

    # Appointments Per Day (for chart)
    appointments_per_day = (
        Appointment.objects.values('date')
        .annotate(count=Count('date'))
        .order_by('date')
    )
    dates = [item['date'].strftime('%Y-%m-%d') for item in appointments_per_day]
    counts = [item['count'] for item in appointments_per_day]

    # Feedback Ratings Count (for chart)
    rating_counts = [Feedback.objects.filter(rating=i).count() for i in range(1, 6)]

    context = {
        'total_appointments': total_appointments,
        'total_services': total_services,
        'total_vets': total_vets,
        'avg_rating': round(avg_rating, 2),
        'dates': dates,
        'counts': counts,
        'rating_counts': rating_counts,
    }
    return render(request, 'dashboard/dashboard.html', context)



CustomUser = get_user_model()  # Ensure Django recognizes your custom user model

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate input
        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            password=password
        )

        # Authenticate and login user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('home')
        else:
            messages.error(request, "Authentication failed.")
            return redirect('register')

    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')