from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import DivingSpot, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView
from django.urls import reverse_lazy
from .forms import CommentForm, DivingSpotForm
from django.db.models import Sum
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import folium, branca

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

            return HttpResponseRedirect(reverse_lazy('reviews:review_detail', args=[divingspot.id, slugify(divingspot.name)]))
        
    def get_context_data(self, **kwargs):
        divingspot = self.get_object()
        divingspot_comments_count = Comment.objects.all().filter(divingspot=self.object.id).count()
        divingspot_comments = Comment.objects.all().filter(divingspot=self.object.id)
        comments_score = divingspot_comments.aggregate(Sum('score'))['score__sum']

        if(comments_score is None):
            divingspot.score = 0

        else:
            divingspot.score = comments_score/divingspot_comments_count
        
        divingspot.save()

        context = super().get_context_data(**kwargs)
        context.update({
            'form':self.form,
            'divingspot_comments': divingspot_comments,
            'divingspot_comments_count': divingspot_comments_count,
            #'divingspot_score': divingspot_score
        })
        return context
    

        


@method_decorator(staff_member_required, name='dispatch')
class DivingSpotCreate(CreateView):
    model = DivingSpot
    form_class = DivingSpotForm

    def form_valid(self, form):
        form.instance.author = self.request.user # Asignar el usuario actual como autor
        return super().form_valid(form)
        

    success_url = reverse_lazy('reviews:review_home')

@method_decorator(staff_member_required, name='dispatch')
class DivingSpotUpdate(UpdateView):
    model = DivingSpot
    form_class = DivingSpotForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('reviews:review_update', args=[self.object.id]) + '?ok'
    
@method_decorator(staff_member_required, name='dispatch')   
class DivingSpotDelete(DeleteView):
    model = DivingSpot
    success_url = reverse_lazy('reviews:review_home')
@method_decorator(login_required, name = 'dispatch')
class CommentDelete(DeleteView):
    model = Comment
    def get_success_url(self):
        return reverse_lazy('reviews:review_detail', args=[self.object.divingspot.id, slugify(self.object.divingspot.name)]) + '?ok'
    
@method_decorator(login_required, name = 'dispatch')
class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('reviews:review_detail', args=[self.object.divingspot.id, slugify(self.object.divingspot.name)]) + '?ok'
    
class CommentListView(ListView):
    model = Comment
    
class ReviewSearchView(ListView):
    model = DivingSpot

    def get_queryset(self):
        query = self.request.GET.get('search')
        data = DivingSpot.objects.filter(name__icontains=query)|DivingSpot.objects.filter(description__icontains=query)|DivingSpot.objects.filter(location__icontains=query)
        return data.order_by('-created')
    
    
def divingspot_map(request):
    #Obtener puntos de inmersión
    divingspots = DivingSpot.objects.all()
    
    #Crear mapa
    map = folium.Map(location=[28.15, -16.5], zoom_start=9)
    for divingspot in divingspots:
        url = reverse('reviews:review_detail', args=[divingspot.id, slugify(divingspot.name)])
        folium.Marker([divingspot.latitude, divingspot.longitude], tooltip=divingspot.name,
                    popup=f"<a href='{url}' target='_parent'>Ver "+divingspot.name+"</a>").add_to(map)
    fig = branca.element.Figure(height="100%")
    fig.add_child(map)
    map = map._repr_html_()
    
    context = {
        'map' : map,

    }
    
    return render(request, 'reviews/divingspot_map.html', context)