from django.db import models

class Nation(models.Model):
    name = models.CharField(max_length=100)

    @property
    def authors_count(self):
        return Author.objects.filter(nationality=self).count()

    def __repr__(self):
        return self.name + f"{self.authors_count}"

    __str__ = __repr__

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(blank=True, null=True)
    nationality = models.ForeignKey(Nation, on_delete=models.PROTECT, default=None)
    photo = models.ImageField(blank=True, null=True)

    # @property
    # def news_count(self):
    #     return 5

    def __repr__(self):
        return self.name

    __str__ = __repr__



class News(models.Model):
    title = models.CharField(max_length= 600)
    date = models.DateTimeField()
    text = models.CharField(max_length=100000)
    category = models.ForeignKey('Category',on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tags')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length= 100)
    position = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.position}'

class Tags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
'''
+ новость
+ категория новости
+ теги новости
'''


'''SELECT * FROM nations where name = ? '''