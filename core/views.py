from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, OwnerForm, AnimalForm, VaccinationForm
from .models import Owner
from django.contrib.auth.decorators import login_required
from .models import Animal, Vaccination, Owner
from datetime import date


def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/home.html')


def register_view(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        owner_form = OwnerForm(request.POST)
        if user_form.is_valid() and owner_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            owner = owner_form.save(commit=False)
            owner.user = user
            owner.save()

            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        owner_form = OwnerForm()

    return render(request, 'core/register.html', {'user_form': user_form, 'owner_form': owner_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')  # 👈 redirected here
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'core/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')




@login_required
def dashboard_view(request):
    owner = Owner.objects.get(user=request.user)

    animals = Animal.objects.filter(owner=owner)

    vaccinations = Vaccination.objects.filter(
        animal__owner=owner
    ).order_by('-date_given')[:5]

    today = date.today()

    # Upcoming vaccinations
    reminders = Vaccination.objects.filter(
        animal__owner=owner,
        next_due__isnull=False,
        next_due__gte=today
    ).order_by('next_due')[:5]

    # Overdue vaccinations
    overdue = Vaccination.objects.filter(
        animal__owner=owner,
        next_due__isnull=False,
        next_due__lt=today
    ).order_by('next_due')

    context = {
        'owner': owner,
        'animals': animals,
        'vaccinations': vaccinations,
        'reminders': reminders,
        'overdue': overdue,
        'today': today,
    }
    return render(request, 'core/dashboard.html', context)



@login_required
def add_animal_view(request):
    owner = Owner.objects.get(user=request.user)

    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.owner = owner
            animal.save()
            return redirect('dashboard')
    else:
        form = AnimalForm()

    return render(request, 'core/add_animal.html', {'form': form})

@login_required
def add_vaccination_view(request):
    owner = Owner.objects.get(user=request.user)

    if request.method == 'POST':
        form = VaccinationForm(owner=owner, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = VaccinationForm(owner=owner)

    return render(request, 'core/add_vaccination.html', {'form': form})



@login_required
def edit_animal_view(request, id):
    owner = Owner.objects.get(user=request.user)
    animal = Animal.objects.get(id=id, owner=owner)

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'core/edit_animal.html', {'form': form, 'animal': animal})



@login_required
def delete_animal_view(request, id):
    owner = Owner.objects.get(user=request.user)
    animal = Animal.objects.get(id=id, owner=owner)

    if request.method == 'POST':
        animal.delete()
        return redirect('dashboard')

    return render(request, 'core/delete_animal.html', {'animal': animal})


@login_required
def edit_vaccination_view(request, id):
    owner = Owner.objects.get(user=request.user)
    vaccination = Vaccination.objects.get(id=id, animal__owner=owner)

    if request.method == 'POST':
        form = VaccinationForm(owner=owner, data=request.POST, instance=vaccination)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = VaccinationForm(owner=owner, instance=vaccination)

    return render(request, 'core/edit_vaccination.html', {'form': form, 'vaccination': vaccination})


@login_required
def delete_vaccination_view(request, id):
    owner = Owner.objects.get(user=request.user)
    vaccination = Vaccination.objects.get(id=id, animal__owner=owner)

    if request.method == 'POST':
        vaccination.delete()
        return redirect('dashboard')

    return render(request, 'core/delete_vaccination.html', {'vaccination': vaccination})
