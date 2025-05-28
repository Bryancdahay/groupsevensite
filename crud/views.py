from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Gender, Users
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "home.html")

def AuthView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # This is where you print form errors to the console for debugging
            print(form.errors)
            return render(request, "registration/signup.html", {"form": form})
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})



    

def gender_list(request):
    try:
        gender = Gender.objects.all()
        data = {
            'gender': gender
        }

        return render(request, 'gender/Genderslist.html', data)
    except Exception as e:
        return HttpResponse(f'Error occured during load genders: {e}')
    

def add_gender(request):

    try:
        if request.method == 'POST':
            gender = request.POST.get('gender')

            Gender.objects.create(gender=gender).save()
            messages.success(request, 'Gender added succesfully!')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f'Error occured during add gender: {e}')
    
def edit_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderobj = Gender.objects.get(pk=genderId)

            gender = request.POST.get('gender')
            genderobj.gender = gender
            genderobj.save()

            messages.success(request, 'Gender updated successfully!')

            data = {
                'gender': genderobj
            }

            return render(request, 'gender/EditGender.html', data)
        else:
            genderobj = Gender.objects.get(pk=genderId) 

            data = {
                'gender': genderobj
            }

        return render(request, 'gender/EditGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error occured during edit gender: {e}')
    
def delete_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderobj = Gender.objects.get(pk=genderId)
            genderobj.delete()

            messages.success(request, 'Gender deleted successfully')
            return redirect('/gender/list')
        else:
            genderobj = Gender.objects.get(pk=genderId)

            data = {
                    'gender': genderobj
                }

            return render(request, 'gender/DeleteGender.html', data)    
    except Exception as e:
        return HttpResponse(f'Error occured during delete gender: {e}')


def user_list(request):
    try:
        userObj = Users.objects.select_related('gender')

        data = {
            'users': userObj
        }

        return render(request, 'user/UsersList.html', data)
    except Exception as e:
        return HttpResponse (f'Error occured during load users:{e}')

def add_user(request):
    try:
        if request.method == 'POST':
            fullname = request.POST.get('full_name', '').strip()
            gender = request.POST.get('gender', '').strip()
            birth_date = request.POST.get('birth_date', '').strip()
            address = request.POST.get('address', '').strip()
            contact = request.POST.get('contact_number', '').strip()
            email = request.POST.get('email', '').strip()
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '')
            confirmpassword = request.POST.get('confirm_password', '')

            errors = {}

            if not fullname:
                errors['full_name'] = "Full name is required."
            if not gender:
                errors['gender'] = "Gender is required."
            if not birth_date:
                errors['birth_date'] = "Birth date is required."
            if not address:
                errors['address'] = "Address is required."
            if not contact:
                errors['contact_number'] = "Contact number is required."
            if not email:
                errors['email'] = "Email is required."
            if not username:
                errors['username'] = "Username is required."
            if not password:
                errors['password'] = "Password is required."
            if not confirmpassword:
                errors['confirm_password'] = "Confirm password is required."
            elif password != confirmpassword:
                errors['confirm_password'] = "Passwords do not match."

            if errors:
                gendervar = Gender.objects.all()
                data = {
                    'genders': gendervar,
                    'form_data': {
                        'full_name': fullname,
                        'gender': gender,
                        'birth_date': birth_date,
                        'address': address,
                        'contact_number': contact,
                        'email': email,
                        'username': username,
                    },
                    'errors': errors
                }
                return render(request, 'user/AddUser.html', data)

            Users.objects.create(
                full_name=fullname,
                gender=Gender.objects.get(pk=gender),
                birth_date=birth_date,
                address=address,
                contact_number=contact,
                email=email,
                username=username,
                password=make_password(password),
            )
            messages.success(request, 'User added successfully')
            return redirect('/user/add')

        else:
            gendervar = Gender.objects.all()
            return render(request, 'user/AddUser.html', {'genders': gendervar, 'errors': {}})
    except Exception as e:
        return HttpResponse(f'Error occurred during add user: {e}')
