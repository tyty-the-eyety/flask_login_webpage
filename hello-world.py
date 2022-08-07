# import the Flask class from the flask module

from flask import Flask, render_template, redirect , url_for , request

from pwd import check_usr_pwd

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('welcome.html')
    #return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        is_user = check_usr_pwd(request.form['username'] , request.form['password'])
        #error = 'Invalid Credentials. ' + str(is_user)
        if is_user:
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials. Please try again.'
        #if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        #    error = 'Invalid Credentials. Please try again.'
        #else:
        #    return redirect(url_for('home'))
    return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)