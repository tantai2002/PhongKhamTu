import json
from __init__ import app

# def read_json(path):
#     with open(path, 'r') as f:
#         return json.load(f)
    
# def load_categories():
#     return read_json(os.path.join(app.root_path, 'data/categories.json'))

def load_categories():
    with open('%s/data/categories.json' % app.root_path, encoding = 'utf-8') as f:
        return json.load(f)

def load_products(categories_id = None, kw = None, btkw = None):
    with open('%s/data/products.json' % app.root_path, encoding = 'utf-8') as f:
        products = json.load(f)
    if categories_id:
        products = [p for p in products if p['category_id'] == int(categories_id)]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
    
    return products

# def load_products():
#     with open('%s/data/products.json' % app.root_path, encoding = 'utf-8') as f:
#         return json.load(f)

# if __name__ == '__main__':
#     import os
#     os.ro