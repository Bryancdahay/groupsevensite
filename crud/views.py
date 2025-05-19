from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gender
from django.contrib import messages
# Create your views here.

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

