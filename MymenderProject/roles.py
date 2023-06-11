from rest_framework_roles.roles import is_user, is_anon, is_admin


def is_buyer(request, view):
    return is_user(request, view) and request.user.usertype = 'buyer'

def is_seller(request, view):
    return is_user(request, view) and request.user.usertype = 'seller'


ROLES = {
    # Django out-of-the-box
    'admin': is_admin,
    'user': is_user,
    'anon': is_anon,

    # Some custom role examples
    'buyer': is_buyer,
    'seller': is_seller,
}