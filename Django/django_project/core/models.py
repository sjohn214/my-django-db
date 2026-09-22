from django.db import models




class Categories(models.Model):
    category_id = models.SmallIntegerField(primary_key=True)
    category_name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'categories'
        verbose_name_plural = "Categories"




class customers(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=5)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    password = models.CharField(db_column='Password', max_length=64, blank=True, null=True)  # Field name made lowercase.
    inactive_date = models.DateField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'customers'
        verbose_name_plural = "Customers"




class employee_territories(models.Model):
    pk = models.CompositePrimaryKey('employee_id', 'territory_id')
    employee = models.ForeignKey('employees', models.DO_NOTHING)
    territory = models.ForeignKey('territories', models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'employee_territories'
        verbose_name_plural = "Employee Territories"




class employees(models.Model):
    employee_id = models.SmallIntegerField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    title_of_courtesy = models.CharField(max_length=25, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    home_phone = models.CharField(max_length=24, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reports_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reports_to', blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'employees'
        verbose_name_plural = "Employees"




class order_details(models.Model):
    pk = models.CompositePrimaryKey('order_id', 'product_id')
    order = models.ForeignKey('orders', models.DO_NOTHING)
    product = models.ForeignKey('products', models.DO_NOTHING)
    unit_price = models.FloatField()
    quantity = models.SmallIntegerField()
    discount = models.FloatField()


    class Meta:
        managed = False
        db_table = 'order_details'
        verbose_name_plural = "Order Details"




class orders(models.Model):
    order_id = models.SmallAutoField(primary_key=True)
    customers = models.ForeignKey('customers', models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey('employees', models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    required_date = models.DateField(blank=True, null=True)
    shipped_date = models.DateField(blank=True, null=True)
    ship_via = models.ForeignKey('shippers', models.DO_NOTHING, db_column='ship_via', blank=True, null=True)
    freight = models.FloatField(blank=True, null=True)
    ship_name = models.CharField(max_length=40, blank=True, null=True)
    ship_address = models.CharField(max_length=60, blank=True, null=True)
    ship_city = models.CharField(max_length=15, blank=True, null=True)
    ship_region = models.CharField(max_length=15, blank=True, null=True)
    ship_postal_code = models.CharField(max_length=10, blank=True, null=True)
    ship_country = models.CharField(max_length=15, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name_plural = "Orders"




class products(models.Model):
    product_id = models.SmallIntegerField(primary_key=True)
    product_name = models.CharField(max_length=40)
    supplier = models.ForeignKey('suppliers', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('categories', models.DO_NOTHING, blank=True, null=True)
    quantity_per_unit = models.CharField(max_length=20, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    units_in_stock = models.SmallIntegerField(blank=True, null=True)
    units_on_order = models.SmallIntegerField(blank=True, null=True)
    reorder_level = models.SmallIntegerField(blank=True, null=True)
    discontinued = models.IntegerField()
    date_discontinued = models.DateField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'products'
        verbose_name_plural = "Products"




class region(models.Model):
    region_id = models.SmallIntegerField(primary_key=True)
    region_description = models.CharField(max_length=60)


    class Meta:
        managed = False
        db_table = 'region'
        verbose_name_plural = "Regions"




class shippers(models.Model):
    shipper_id = models.SmallIntegerField(primary_key=True)
    company_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=24, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'shippers'
        verbose_name_plural = "Shippers"




class suppliers(models.Model):
    supplier_id = models.SmallIntegerField(primary_key=True)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'suppliers'
        verbose_name_plural = "Suppliers"




class territories(models.Model):
    territory_id = models.CharField(primary_key=True, max_length=20)
    territory_description = models.CharField(max_length=60)
    region = models.ForeignKey('region', models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'territories'
        verbose_name_plural = "Territories"




class us_states(models.Model):
    state_id = models.SmallIntegerField(primary_key=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    state_abbr = models.CharField(max_length=2, blank=True, null=True)
    state_region = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'us_states'
        verbose_name_plural = "US States"
