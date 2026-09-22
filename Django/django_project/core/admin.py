from django.contrib import admin
from .models import customers, employees, orders, products, shippers, suppliers, us_states

# Register your core tables so they appear in the admin panel
admin.site.register(customers)
# admin.site.register(employee_territories)
admin.site.register(employees)
# admin.site.register(order_details)
admin.site.register(orders)
admin.site.register(products)
# admin.site.register(region)
admin.site.register(shippers)
admin.site.register(suppliers)
# admin.site.register(territories)
admin.site.register(us_states)

# Register your models here.
