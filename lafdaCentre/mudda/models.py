from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mudda(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    mudda_desc = models.TextField(max_length=300)
    mudda_img = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    likes_count=models.ManyToManyField(User, related_name='liked_muddas', blank=True)

    def __str__(self):
        return f'{self.userID.username} - {self.mudda_desc[:10]}'
    
    def total_likes(self):
        return self.likes_count.count()  # Return the count of likes

    
#for adding the search funcitonality in our lafda centre
class SearchQuery(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) #models.cascade se ye benefit hota h ki, jb hm userID ko delete krege, to isse related saari info delete ho jaygi:)
    query=models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.query}"