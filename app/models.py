from django.db import models

class PizzaRestaurant(models.Model):
   address = models.CharField(verbose_name='住所', max_length=100, blank=True, null=True)
   city = models.CharField(verbose_name='市', max_length=100, blank=True, null=True)
   postalcode = models.CharField(verbose_name='郵便番号', max_length=20, blank=True, null=True)
   name = models.CharField(verbose_name='レストラン名', max_length=100, blank=True, null=True)
   category = models.CharField(verbose_name='カテゴリー', max_length=100, blank=True, null=True)
   cust_id = models.CharField(verbose_name='ID', max_length=100, blank=True, null=True)
   class Meta:
       db_table = 'pizza_restaurants'
       verbose_name = 'ピザ屋さん'
       verbose_name_plural = 'ピザ屋さんリスト'