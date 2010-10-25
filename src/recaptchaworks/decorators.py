

from django.utils.decorators import available_attrs
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.

from recaptchaworks.utils import post_payload_add_recaptcha_remote_ip_field


def fix_recaptcha_remote_ip(view_func):
    """
    Modifies a view function so that its request's POST payload contains
    a ``recaptcha_remote_ip_field`` field.

    """
    def wrapped_view(*args, **kwargs):
        args = list(args)
        args[0] = post_payload_add_recaptcha_remote_ip_field(args[0])
        resp = view_func(*args, **kwargs)
        return resp
    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)

