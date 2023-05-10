from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import DivingSpot, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm, DivingSpotForm

class StaffRequiredMixin(object):
    """ 
    Este Mixin requerirá que el usuario sea miembro del staff 
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
# Create your views here.
@method_decorator(staff_member_required, name='dispatch')      
class ReviewListView(ListView):
    model = DivingSpot
@method_decorator(staff_member_required, name='dispatch')  
class ReviewDetailView(DetailView):
    model = DivingSpot

@method_decorator(staff_member_required, name='dispatch')
class DivingSpotCreate(CreateView):
    model = DivingSpot
    form_class = DivingSpotForm

    def form_valid(self, form):
        form.instance.author = self.request.user # Asignar el usuario actual como autor
        return super().form_valid(form)
        

    success_url = reverse_lazy('reviews:reviews')

@method_decorator(staff_member_required, name='dispatch')
class DivingSpotUpdate(UpdateView):
    model = DivingSpot
    form_class = DivingSpotForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('reviews:update', args=[self.object.id]) + '?ok'
    
@method_decorator(staff_member_required, name='dispatch')   
class DivingSpotDelete(DeleteView):
    model = DivingSpot
    success_url = reverse_lazy('reviews:reviews')

class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):  
        return reverse_lazy('reviews:reviews', args=[self.object.id])