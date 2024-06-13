from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def is_admin():
    def decorator(view_function):
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.is_admin:
                    return view_function(request, *args, **kwargs)
                else:
                    raise PermissionDenied
            else:
                return redirect('accounts:login')
        return wrap
    return decorator
