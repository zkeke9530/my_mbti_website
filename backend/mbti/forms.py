from django import forms
# from .models import MBTISentenceModified
from .models import MBTISentenceTrue

# class MBTISentenceModifiedForm(forms.ModelForm):
#     class Meta:
#         model = MBTISentenceModified
#         fields = '__all__'
#         widgets = {
#             'sentence': forms.Textarea(attrs={
#                 'rows': 9,
#                 'style': 'white-space: pre-wrap;'  # 关键：保留换行和前导空格
#             }),
#         }



class MBTISentenceTrueForm(forms.ModelForm):
    class Meta:
        model = MBTISentenceTrue
        fields = '__all__'
        widgets = {
            'sentence': forms.Textarea(attrs={
                'rows': 9,
                'style': 'white-space: pre-wrap;'  # 关键：保留换行和前导空格
            }),
        }
        

      
