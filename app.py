from flask import Flask, render_template, request, redirect

app = Flask(__name__)
products=[]
@app.route('/', methods=['POST', 'GET'])
def index():
    name = None
    if request.method == "POST":
        name = request.form.get('product_name') 
        products.append(name)
    return render_template('index.html', products_=products)
@app.route('/submit_products', methods=['POST'])
def index():
        name = request.form.get('product_name')
        products.append(name)
        return redirect(url_for('index'))
if __name__== "__main__":
    app.run(debug=True)