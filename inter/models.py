from django.db import models

# Create your models here.


class Division(models.Model):
    name = models.CharField("Отряд", max_length=50)
    number = models.IntegerField()
    slug = models.SlugField(max_length=60, unique=True)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField("Отдел", max_length=50)
    division = models.ForeignKey(Division, verbose_name="Отряд", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField("Подразделение", max_length=50)
    department = models.ForeignKey(Department, verbose_name="Отдел", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    sector = models.ForeignKey(Department, verbose_name="Подразделение", on_delete=models.CASCADE)
    rank = models.CharField("Звание", max_length=20)
    grade = models.IntegerField()
    position = models.CharField("Должность", max_length=40)
    first_name = models.CharField("Имя", max_length=15)
    second_name = models.CharField("Фамилия", max_length=15)
    patronymic_name = models.CharField("Отчество", max_length=15)
    telephone_on_net = models.CharField("тел. в сети", max_length=12)
    telephone_on_division = models.CharField("тел. внутренний", max_length=9)
    intranet_email = models.EmailField("интранет почта")
    internet_email = models.EmailField("интернет почта")
    photo = models.ImageField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.second_name
'''
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})
'''