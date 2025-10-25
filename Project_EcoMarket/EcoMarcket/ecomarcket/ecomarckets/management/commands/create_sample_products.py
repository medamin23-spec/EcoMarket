from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from ecomarckets.models import Product
import os

class Command(BaseCommand):
    help = 'Create sample products for the eco marketplace'

    def handle(self, *args, **options):
        # Create sample products with English descriptions
        sample_products = [
            {
                'name': 'Reusable Stainless Steel Water Bottle',
                'description': 'Eco-friendly water bottle made from stainless steel. Keeps water cold for 24 hours and hot for 12 hours. Perfect for daily use.',
                'price': 25.00,
                'image': 'products/water-bottle.jpg'
            },
            {
                'name': 'Organic Cotton Tote Bag',
                'description': 'Durable shopping tote made from organic cotton. Perfect replacement for plastic bags. Machine washable and biodegradable.',
                'price': 15.00,
                'image': 'products/tote-bag.jpg'
            },
            {
                'name': 'Bamboo Coffee Cup Set',
                'description': 'Set of 4 bamboo coffee cups. Heat resistant and safe for hot beverages. Naturally antibacterial and biodegradable.',
                'price': 45.00,
                'image': 'products/bamboo-cups.jpg'
            },
            {
                'name': 'Natural Shampoo Bar',
                'description': '100% natural solid shampoo bar free from harmful chemicals. Suitable for all hair types. Lasts 2-3 months.',
                'price': 18.00,
                'image': 'products/shampoo-bar.jpg'
            },
            {
                'name': 'Bamboo Toothbrush Set',
                'description': 'Eco-friendly toothbrush made from natural bamboo. Biodegradable handle with soft bristles. Pack of 4.',
                'price': 12.00,
                'image': 'products/bamboo-brush.jpg'
            },
            {
                'name': 'Silicone Food Storage Bags',
                'description': 'Reusable food storage bags made from food-grade silicone. Heat resistant up to 400°F. Dishwasher safe.',
                'price': 35.00,
                'image': 'products/silicone-bags.jpg'
            }
        ]

        # Delete existing products
        Product.objects.all().delete()
        
        created_count = 0
        for product_data in sample_products:
            # Create dummy image file
            dummy_image = ContentFile(b'dummy image content', name=product_data['image'])
            product = Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price']
            )
            # Set dummy image
            product.image.save(product_data['image'], dummy_image, save=True)
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Created product: {product.name}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} products!')
        )
