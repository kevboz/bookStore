from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[
             MinValueValidator(1),
             MaxValueValidator(5)
            ])
    author = models.CharField(max_length=100,null=True)
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) #harry-potter-1

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # self.slug = self.title.replace(" ", "-").lower() # using the above in replace of this line
        super(Book, self).save(*args, **kwargs) # makes sure the django default save method is called
    
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    

    def __str__(self):
        return f"{self.title} rating of {self.rating}"


    