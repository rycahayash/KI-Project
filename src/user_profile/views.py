from django.shortcuts import render, redirect
from user_profile.models import UserProfile
from account.models import Account
from .forms import UserProfileForm
from django.http import HttpResponse 

def user_profile_view(request):
    # Ambil data profil pengguna yang sedang login
    current_user = request.user
    data = request.user
    result = Account.objects.filter(email=data).values()
    
    # data = []
    # for row in result:
    #     data.append(row.email)
    #     data.append(row.username)
    #     data.append(row.date_joined)

    try:
        profile = UserProfile.objects.get(user=current_user)
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        # Jika form dikirim dengan metode POST, proses data
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        # Jika metode GET, tampilkan data profil dalam form
        form = UserProfileForm(instance=profile)

    context = {
        # 'form': form,
        'profile': profile,
        'current_user': current_user,
        'data': result,
    }

    return render(request, 'user_profile/profile.html', context)

