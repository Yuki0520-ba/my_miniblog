from django import forms
from .models import Blog   


#フォームの詳細を決める
class BlogForm(forms.ModelForm):

    content=forms.CharField(widget=forms.TextInput(attrs={'size':25}))
    content_detail=forms.CharField(widget=forms.Textarea,required=False)
    url=forms.CharField(widget=forms.TextInput(attrs={'size':25}),required=False)
    

    class Meta:
        model=Blog
        fields=["content","content_detail","url"]
