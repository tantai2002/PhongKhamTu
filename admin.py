from __init__ import admin, db
from model import Category, Product
from flask_admin.contrib.sqla import ModelView

class ProductView(ModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True

admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))