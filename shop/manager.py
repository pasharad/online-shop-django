from core.manager import BaseManager
from django.db.models import Count


class CategoryManager(BaseManager):
    def discounted_category(self):
        return self.exclude(discount__isnull=True)
    def get_product_number(self):
        return self.annotate(product_count = Count('products'))

class ProductManager(BaseManager):
        def discounted_product(self):
            return self.exclude(discount__isnull=True)

class InventoryManager(BaseManager):
    def get_less_product(self):
         self.exclude(quantity__gte=5)

class OrderManager(BaseManager):
    ...

