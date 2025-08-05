from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Очистить базу и добавить тестовые категории и продукты"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        electronics = Category.objects.create(name="Электроника", description="Гаджеты")
        clothing = Category.objects.create(name="Одежда", description="Футболки и куртки")

        Product.objects.create(
            name="Смартфон",
            description="Современный телефон с большим экраном",
            category=electronics,
            purchase_price=499.99
        )

        Product.objects.create(
            name="Наушники",
            description="Беспроводные, с шумоподавлением",
            category=electronics,
            purchase_price=199.99
        )

        Product.objects.create(
            name="Футболка",
            description="Хлопковая, белая",
            category=clothing,
            purchase_price=29.99
        )

        self.stdout.write(self.style.SUCCESS("✅ Добавлены тестовые категории и продукты!"))
