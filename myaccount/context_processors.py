from myaccount.models import User_img, UserProfile


def image(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user_id=user.id)
        img = profile.avatar
        return {
            'image': img,
        }
    except:
        return {}

