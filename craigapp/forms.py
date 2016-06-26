from django.forms import ModelForm
from craigapp.models import Listing

# Create the form class.
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['category', 'shopper', 'item_price']



