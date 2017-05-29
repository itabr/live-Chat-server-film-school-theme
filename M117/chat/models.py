from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=400)
    location = models.CharField(max_length=400)
    school = models.CharField(max_length=50)
    state = models.IntegerField( default=0 )
    Action = models.IntegerField( default=0 )
    Adventure = models.IntegerField( default= 0 )
    Animation = models.IntegerField( default= 0 )
    Biography = models.IntegerField( default= 0 )
    Comedy = models.IntegerField( default= 0 )
    Crime = models.IntegerField( default= 0 )
    Documentary = models.IntegerField( default= 0 )
    Drama = models.IntegerField( default= 0 )
    Family = models.IntegerField( default= 0 )
    Fantasy = models.IntegerField( default= 0 )
    FilmNoir = models.IntegerField( default= 0 )
    History = models.IntegerField( default= 0 )
    Horror = models.IntegerField( default= 0 )
    Music = models.IntegerField( default= 0 )
    Musical = models.IntegerField( default= 0 )
    Mystery = models.IntegerField( default= 0 )
    Romance = models.IntegerField( default= 0 )
    SciFi = models.IntegerField( default= 0 )
    Sport = models.IntegerField( default= 0 )
    Thriller = models.IntegerField( default= 0 )
    War = models.IntegerField( default= 0 )
    Western = models.IntegerField( default= 0 )

class Action(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Adventure (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Animation (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Biography (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Comedy (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Crime (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Documentary (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Drama (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Family (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Fantasy (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class FilmNoir (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class History (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Horror (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Music (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Musical (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Mystery (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Romance (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class SciFi (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Sport (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Thriller (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class War (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')

class Western (models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.CharField(max_length=500,default='')
