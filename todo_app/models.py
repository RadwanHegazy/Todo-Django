from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo (models.Model) :
    user = models.ForeignKey(User,null=True,related_name='userTodo',on_delete=models.CASCADE)    
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)


    def __str__(self) :
        return f"{self.date}"

    def create_action (text,user) :
        Todo.objects.create(text=text,user=user)

    def make_done (id,user) :
        to = Todo.objects.get(id=id,user=user)
        if to.is_done :
            to.is_done = False
        else :
            to.is_done = True
        to.save()
    
    def delete_action (user,id) :
        todo = Todo.objects.get(user=user,id=id)
        todo.delete()