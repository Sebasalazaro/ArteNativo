from django.forms import ModelForm, DateTimeInput

from .models import Auction

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['starting_price', 'bid_end_time']
        widgets = {
            'bid_end_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }