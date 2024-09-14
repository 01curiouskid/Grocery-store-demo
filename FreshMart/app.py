from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='AG13@sql',
    database='freshmart_db'
)

# Home page - Login
@app.route('/')
def index():
    return render_template('login.html')

# Admin dashboard
@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    cursor = db.cursor(dictionary=True)
    
    # Fetch orders
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    
    # Fetch inventory
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()
    
    return render_template('admin.html', orders=orders, inventory=inventory)


# Edit inventory
@app.route('/edit_inventory', methods=['POST'])
def edit_inventory():
    item_id = request.form['id']
    cost_per_unit = request.form['cost_per_unit']
    quantity_left = request.form['quantity_left']
    
    cursor = db.cursor()
    cursor.execute("""
        UPDATE inventory SET cost_per_unit = %s, quantity_left = %s WHERE id = %s
    """, (cost_per_unit, quantity_left, item_id))
    db.commit()
    
    flash('Inventory updated successfully!')
    return redirect(url_for('admin_dashboard'))

# Add item
@app.route('/add_item', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    cost_per_unit = request.form['cost_per_unit']
    quantity_left = request.form['quantity_left']
    unit = request.form['unit']
    
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO inventory (item_name, cost_per_unit, quantity_left, unit)
        VALUES (%s, %s, %s, %s)
    """, (item_name, cost_per_unit, quantity_left, unit))
    db.commit()
    
    flash('Item added successfully!')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
