# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id':1, 'date':'2026-10-16', 'amount':100},
    {'id':2, 'date':'2026-10-16', 'amount':200},
    {'id':3, 'date':'2026-10-16', 'amount':500}
]


# Read operation
@app.route('/read')
def get_transactions():
    return render_template("transactions.html", transactions=transactions)


# Create operation
@app.route('/add', methods=["GET","POST"])
def add_transaction():
    if request.method == 'POST':
        transaction_new = {
            'id': len(transactions) + 1, #generate new transactions id
            'date': request.form['date'], #get the new date
            'amount': float(request.form['amount']), #get the new amount
        }
        transactions.append(transaction_new)
        return redirect(url_for("get_transactions"))
    
    return render_template("form.html") #if the method is get, create a form.html to display 


# Update operation
@app.route('/edit/<int:transaction_id>', methods=["GET","POST"])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        date = request.form['date']
        amount =float(request.form ['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        return redirect(url_for("get_transactions"))
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction = transaction )
        

# Delete operation

@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for('get_transactions'))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)   