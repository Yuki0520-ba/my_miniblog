from django import forms
from .models import Blog   


#フォームの詳細を決める
class BlogForm(forms.ModelForm):

    #サイズを５０にする
    content=forms.CharField(widget=forms.TextInput(attrs={'size':50}))

    class Meta:
        model=Blog
        fields=["content"]
