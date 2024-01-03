from northwind.di.mixins.category import CategoryContainerMixin
from northwind.di.mixins.product import ProductContainerMixin
from northwind.di.mixins.supplier import SupplierContainerMixin


class NorthwindContainerMixin(CategoryContainerMixin, ProductContainerMixin, SupplierContainerMixin):
    pass
