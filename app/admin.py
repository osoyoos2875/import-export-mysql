from django.contrib import admin
from .models import PizzaRestaurant  # 追加
from import_export import resources  # 追加
from import_export.admin import ImportExportModelAdmin  # 追加
from import_export.fields import Field # 追加

class PizzaRestaurantResource(resources.ModelResource):
   # field名とcsvの列名が異なる場合はここで指定する。
   # ここでは、postalcode / postalCode、category / categoriesと微妙に異なる。   
   postalcode = Field(attribute='postalcode', column_name='postalCode')
   category = Field(attribute='category', column_name='categories')
   address = Field(attribute='address', column_name='address')
   city = Field(attribute='city', column_name='city')
   name = Field(attribute='name', column_name='name')
   csut_id = Field(attribute='cust_id', column_name='cust_id')
   # django-import-exportのModel設定
   class Meta:
       model = PizzaRestaurant
       # Controls if the import should skip unchanged records. Default value is False
       skip_unchanged = True
       use_bulk = True

@admin.register(PizzaRestaurant)
# ImportExportModelAdminを継承したAdminクラスを作成する
class PizzaRestaurantAdmin(ImportExportModelAdmin):
   ordering = ['id']
   list_display = ('id', 'postalcode', 'name', 'category', 'city', 'address','cust_id')
   # resource_classにModelResourceを継承したクラス設定
   resource_class = PizzaRestaurantResource