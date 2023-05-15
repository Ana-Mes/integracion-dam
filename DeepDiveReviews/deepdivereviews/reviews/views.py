from django.shortcuts import render, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import DivingSpot, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView
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
class ReviewListView(ListView):
    model = DivingSpot
class ReviewDetailView(HitCountDetailView):
    model = DivingSpot
    count_hit = True

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            divingspot = self.get_object()
            form.instance.author = self.request.user
            form.instance.divingspot = divingspot
            form.save()

            return self.get(request, *args, **kwargs) 
        
    def get_context_data(self, **kwargs):
        divingspot_comments_count = Comment.objects.all().filter(divingspot=self.object.id).count()
        divingspot_comments = Comment.objects.all().filter(divingspot=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form':self.form,
            'divingspot_comments': divingspot_comments,
            'divingspot_comments_count': divingspot_comments_count,
        })
        return context
    
"""     def get_success_url(self):
        return reverse_lazy('reviews:detail', args=[self.object.id]) """
        


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