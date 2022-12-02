from flask import render_template, request
from __init__ import app
import dao


@app.route("/")
def home():
    # cates = dao.load_categories()
    return render_template('index.html')

# @app.route("/productsAll")
# def products():
    
#     categories_id = request.args.get("category_id")
#     kw = request.args.get("search")


#     cates = dao.load_categories()
#     products = dao.load_products(categories_id = categories_id,
#                                 kw = kw
                                
#                         )

#     return render_template('productsAll.html', 
#                                             products = products,
#                                             categories = cates
#                         )




if __name__ == '__main__':
    app.run(debug=True)