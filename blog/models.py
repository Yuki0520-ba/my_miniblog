from django.db import models

# Create your models here.
class Blog(models.Model):
    content=models.CharField(max_length=140)
    content_detail=models.CharField(max_length=600,null=True)
    url=models.CharField(max_length=140,null=True)
    


    posted_date=models.DateTimeField(auto_now_add=True) #auto_now_addで追加時に自動で保存する
    
    class Meta:
        ordering =['-posted_date']


    
    
    