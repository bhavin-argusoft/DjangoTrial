from django import forms  
from guest.models import Guest  
class GuestForm(forms.ModelForm):  
    class Meta:  
        model = Guest  
        fields = "__all__"  

    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'