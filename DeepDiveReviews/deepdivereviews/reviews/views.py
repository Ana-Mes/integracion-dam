from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import DivingSpot
from django.views.generic import ListView

class StaffRequiredMixin(object):
    """ 
    Este Mixin requerirá que el usuario sea miembro del staff 
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
# Create your views here.
    
class ReviewListView(ListView):
    model = DivingSpot