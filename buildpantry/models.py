from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
# Create your models here.

dishtypes=[
('Appetizers & Snacks','Appetizers & Snacks'),
('Bread Recipes','Bread Recipes'),
('Cake Recipes','Cake Recipes'),
('Candy and Fudge','Candy and Fudge'),
('Casserole Recipes','Casserole Recipes'),
('Christmas Cookies','Christmas Cookies'),
('Cocktail Recipes','Cocktail Recipes'),
('Cookie Recipes','Cookie Recipes'),
('Mac and Cheese Recipes','Mac and Cheese Recipes'),
('Main Dish','Main Dish'),
('Pasta Salad Recipes','Pasta Salad Recipes'),
('Pasta Recipes','Pasta Recipes'),
('Pie Recipes','Pie Recipes'),
('Pizza','Pizza'),
('Sandwiches','Sandwiches'),
('Sauces and Condiments','Sauces and Condiments'),
('Smoothie Recipes','Smoothie Recipes'),
('Soups, Stews, and Chili','Soups, Stews, and Chili'),
('Side Dish','Side Dish'),
('Salad','Salad')
]
cuisines=[
    ('Chinese','Chinese'),
    ('Indian','Indian'),
    ('Italian','Italian'),
    ('Mexican','Mexican'),
    ('Southern','Southern'),
    ('Thai','Thai')
]
categories=[
('condiments','condiments'),
('Legumes','Legumes'),
('Seasonings','Seasonings'),
('Alcohol','Alcohol'),
('Added Sweetners','Added Sweetners'),
('Dairy Alternatives','Dairy Alternatives'),
('Oils','Oils'),
('Nuts','Nuts'),
('Meats','Meats'),
('Vegetables','Vegetables'),
('Seafood','Seafood'),
('Fruits','Fruits'),
('Dairy','Dairy'),
('Fish','Fish'),
('Desserts&Snacks','Desserts&Snacks'),
('Soup','Soup'),
('Baking & Grains','Baking & Grains'),
('Spices','Spices'),
('Sauces','Sauces'),
('Beverages','Beverages'),
]
marks=[
      ('green','green'),('red','red'),('yellow','yellow')
]
class ingredient(models.Model):
    name=models.CharField(max_length=25,primary_key=True)
    category=models.CharField(max_length=25,choices=categories,blank=False)
    image=models.URLField()

    def __str__(self):
        return self.name


class recipe(models.Model):
    title=models.CharField(max_length=40,primary_key=True)
    description=models.TextField()
    instructions=models.TextField()
    cuisine=models.CharField(max_length=25,choices=cuisines,default='',null=True,blank=True)
    dishtype=models.CharField(max_length=35,choices=dishtypes,default='',null=True,blank=True)
    mark=models.CharField(max_length=7,choices=marks)
    ingredients=models.ManyToManyField(
        ingredient,
        through='ingredientList',
        through_fields=('recipe_name','ingredient_name')
    )
    images=ArrayField(base_field=models.URLField())
    timetocook=models.TimeField()
    
    def __str__(self):
        return self.title


class ingredientList(models.Model):
    recipe_name=models.ForeignKey(recipe,on_delete=models.CASCADE)
    ingredient_name=models.ForeignKey(ingredient,on_delete=models.PROTECT)
    quantity=models.CharField(max_length=40,blank=False)
    directions=models.CharField(max_length=40,blank=True,null=True)
