from django.forms import ModelForm
from .models import Bb
# create form for new board
class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title','content','price','rubric')