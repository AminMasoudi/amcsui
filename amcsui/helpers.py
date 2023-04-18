from django.contrib.auth.models import User
from users.models import UserProfile


def profile_finder(request):
    ''' finds `UserProfile` if user has been authenticated
     else returns `False`'''
    if request.user.is_authenticated:

        user    = User.objects.get(username=request.user.username)
        profile = UserProfile.objects.get(user=user)
        return profile

    return False
