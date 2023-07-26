from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import *
from orders.models import *
from .forms import *
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        coupon_valid = Order.objects.filter(coupon=code)
        if coupon_valid:
            messages.add_message(request, messages.ERROR, _('Купон вже був використаний'))
        else:
            try:
                coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
                request.session['coupon_id'] = coupon.id
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
                messages.add_message(request, messages.ERROR, _('Купон не дійсний'))
    return redirect('cart:cart_detail')

