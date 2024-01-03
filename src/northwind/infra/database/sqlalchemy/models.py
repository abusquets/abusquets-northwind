from sqlalchemy import (
    Column,
    Date,
    Float,
    ForeignKeyConstraint,
    Integer,
    LargeBinary,
    PrimaryKeyConstraint,
    SmallInteger,
    String,
    Table,
    Text,
)

from infra.database.sqlalchemy.sqlalchemy import metadata


categories = Table(
    'categories',
    metadata,
    Column('category_id', Integer, primary_key=True),
    Column('category_name', String(15), nullable=False),
    Column('description', Text),
    Column('picture', LargeBinary),
    PrimaryKeyConstraint('category_id', name='categories_pkey'),
)

customer_demographics = Table(
    'customer_demographics',
    metadata,
    Column('customer_type_id', String(5), primary_key=True),
    Column('customer_desc', Text),
    PrimaryKeyConstraint('customer_type_id', name='pk_customer_demographics'),
)

customers = Table(
    'customers',
    metadata,
    Column('customer_id', String(5), primary_key=True),
    Column('company_name', String(40), nullable=False),
    Column('contact_name', String(30)),
    Column('contact_title', String(30)),
    Column('address', String(60)),
    Column('city', String(15)),
    Column('region', String(15)),
    Column('postal_code', String(10)),
    Column('country', String(15)),
    Column('phone', String(24)),
    Column('fax', String(24)),
    PrimaryKeyConstraint('customer_id', name='pk_customers'),
)

employees = Table(
    'employees',
    metadata,
    Column('employee_id', Integer, primary_key=True),
    Column('last_name', String(20), nullable=False),
    Column('first_name', String(10), nullable=False),
    Column('title', String(30)),
    Column('title_of_courtesy', String(25)),
    Column('birth_date', Date),
    Column('hire_date', Date),
    Column('address', String(60)),
    Column('city', String(15)),
    Column('region', String(15)),
    Column('postal_code', String(10)),
    Column('country', String(15)),
    Column('home_phone', String(24)),
    Column('extension', String(4)),
    Column('photo', LargeBinary),
    Column('notes', Text),
    Column('reports_to', SmallInteger),
    Column('photo_path', String(255)),
    ForeignKeyConstraint(['reports_to'], ['employees.employee_id'], name='fk_employees_employees'),
    PrimaryKeyConstraint('employee_id', name='employees_pkey'),
)

region = Table(
    'region',
    metadata,
    Column('region_id', Integer, primary_key=True),
    Column('region_description', String(60), nullable=False),
    PrimaryKeyConstraint('region_id', name='region_pkey'),
)

shippers = Table(
    'shippers',
    metadata,
    Column('shipper_id', Integer, primary_key=True),
    Column('company_name', String(40), nullable=False),
    Column('phone', String(24)),
    PrimaryKeyConstraint('shipper_id', name='shippers_pkey'),
)

suppliers = Table(
    'suppliers',
    metadata,
    Column('supplier_id', Integer, primary_key=True),
    Column('company_name', String(40), nullable=False),
    Column('contact_name', String(30)),
    Column('contact_title', String(30)),
    Column('address', String(60)),
    Column('city', String(15)),
    Column('region', String(15)),
    Column('postal_code', String(10)),
    Column('country', String(15)),
    Column('phone', String(24)),
    Column('fax', String(24)),
    Column('homepage', Text),
    PrimaryKeyConstraint('supplier_id', name='suppliers_pkey'),
)

us_states = Table(
    'us_states',
    metadata,
    Column('state_id', Integer, primary_key=True),
    Column('state_name', String(100)),
    Column('state_abbr', String(2)),
    Column('state_region', String(50)),
    PrimaryKeyConstraint('state_id', name='us_states_pkey'),
)

customer_customer_demo = Table(
    'customer_customer_demo',
    metadata,
    Column('customer_id', String(5), primary_key=True, nullable=False),
    Column('customer_type_id', String(5), primary_key=True, nullable=False),
    ForeignKeyConstraint(['customer_id'], ['customers.customer_id'], name='fk_customer_customer_demo_customers'),
    ForeignKeyConstraint(
        ['customer_type_id'],
        ['customer_demographics.customer_type_id'],
        name='fk_customer_customer_demo_customer_demographics',
    ),
    PrimaryKeyConstraint('customer_id', 'customer_type_id', name='pk_customer_customer_demo'),
)

orders = Table(
    'orders',
    metadata,
    Column('order_id', Integer, primary_key=True),
    Column('customer_id', String(5)),
    Column('employee_id', SmallInteger),
    Column('order_date', Date),
    Column('required_date', Date),
    Column('shipped_date', Date),
    Column('ship_via', SmallInteger),
    Column('freight', Float),
    Column('ship_name', String(40)),
    Column('ship_address', String(60)),
    Column('ship_city', String(15)),
    Column('ship_region', String(15)),
    Column('ship_postal_code', String(10)),
    Column('ship_country', String(15)),
    ForeignKeyConstraint(['customer_id'], ['customers.customer_id'], name='fk_orders_customers'),
    ForeignKeyConstraint(['employee_id'], ['employees.employee_id'], name='fk_orders_employees'),
    ForeignKeyConstraint(['ship_via'], ['shippers.shipper_id'], name='fk_orders_shippers'),
    PrimaryKeyConstraint('order_id', name='orders_pkey'),
)

products = Table(
    'products',
    metadata,
    Column('product_id', Integer, primary_key=True),
    Column('product_name', String(40), nullable=False),
    Column('supplier_id', SmallInteger),
    Column('category_id', SmallInteger),
    Column('quantity_per_unit', String(20)),
    Column('unit_price', Float),
    Column('units_in_stock', SmallInteger),
    Column('units_on_order', SmallInteger),
    Column('reorder_level', SmallInteger),
    Column('discontinued', Integer, nullable=False),
    ForeignKeyConstraint(['category_id'], ['categories.category_id'], name='fk_products_categories'),
    ForeignKeyConstraint(['supplier_id'], ['suppliers.supplier_id'], name='fk_products_suppliers'),
    PrimaryKeyConstraint('product_id', name='products_pkey'),
)

territories = Table(
    'territories',
    metadata,
    Column('territory_id', String(20), primary_key=True),
    Column('territory_description', String(60), nullable=False),
    Column('region_id', SmallInteger, nullable=False),
    ForeignKeyConstraint(['region_id'], ['region.region_id'], name='fk_territories_region'),
    PrimaryKeyConstraint('territory_id', name='pk_territories'),
)

employee_territories = Table(
    'employee_territories',
    metadata,
    Column('employee_id', SmallInteger, primary_key=True, nullable=False),
    Column('territory_id', String(20), primary_key=True, nullable=False),
    ForeignKeyConstraint(['employee_id'], ['employees.employee_id'], name='fk_employee_territories_employees'),
    ForeignKeyConstraint(['territory_id'], ['territories.territory_id'], name='fk_employee_territories_territories'),
    PrimaryKeyConstraint('employee_id', 'territory_id', name='pk_employee_territories'),
)

order_details = Table(
    'order_details',
    metadata,
    Column('order_id', SmallInteger, primary_key=True, nullable=False),
    Column('product_id', SmallInteger, primary_key=True, nullable=False),
    Column('unit_price', Float, nullable=False),
    Column('quantity', SmallInteger, nullable=False),
    Column('discount', Float, nullable=False),
    ForeignKeyConstraint(['order_id'], ['orders.order_id'], name='fk_order_details_orders'),
    ForeignKeyConstraint(['product_id'], ['products.product_id'], name='fk_order_details_products'),
    PrimaryKeyConstraint('order_id', 'product_id', name='pk_order_details'),
)
