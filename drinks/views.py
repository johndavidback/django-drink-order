# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import View


from drinks.forms import Order
from drinks.models import Drink, DrinkOrder


class HomeView(View):

    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):

        form = Order()

        ctx = RequestContext(self.request, {
            'form': form,
            'drinks': Drink.objects.filter().order_by('name')
        })

        return render_to_response('home.html', context_instance=ctx)

    def post(self, *args, **kwargs):

        form = Order(self.request.POST)

        if form.is_valid():
            drink = DrinkOrder()
            drink.drink = form.cleaned_data['drink']
            drink.person = form.cleaned_data['person']
            drink.notes = form.cleaned_data['notes']

            drink.save()

            ctx = RequestContext(self.request, {
                'drink': drink,
            })

            return render_to_response('thanks.html', context_instance=ctx)



        ctx = RequestContext(self.request, {
            'form': form,
            'drinks': Drink.objects.filter().order_by('name')
        })


        return render_to_response('home.html', context_instance=ctx)