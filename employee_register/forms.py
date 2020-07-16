from django import forms
from . models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
                #(or) '__all__' for importing all fields in Employee model
        labels = {
            'fullname' : 'Full Name',
            'emp_code' : 'EMP.code',
        }

    # for not showing dashes(--)in position field

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "select"

        # for removing any mandatory fields in form
        self.fields['emp_code'].required = False
