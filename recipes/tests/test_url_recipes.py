from django.test import TestCase
from django.urls import reverse


class RecipeUrlTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 3})
        self.assertEqual(url, '/recipes/category/3/')

    def test_recipe_datail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 3})
        self.assertEqual(url, '/recipes/3/')
