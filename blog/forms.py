from django import forms
from .models import Blog   


#フォームの詳細を決める
class BlogForm(forms.ModelForm):

    content=forms.CharField(widget=forms.TextInput(attrs={'size':25}))
    content_detail=forms.CharField(widget=forms.Textarea)
    url=forms.CharField(widget=forms.TextInput(attrs={'size':25}))
    

    class Meta:
        model=Blog
        fields=["content","content_detail","url"]
