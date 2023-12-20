from flask import Flask,render_template,flash,redirect,url_for
from form import RegistrationForm,LoginForm
app=Flask(__name__)

app.config['SECRET_KEY']='f506a7c4dc212fd815d63d10ba97a48e'

posts=[
    {
        'name':'Hari Haran',
        'department':'IT',
        'role':'flask'
    },
    {
        
        'name':'Harit',
        'department':'IT',
        'role':'front'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)
                              
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash('Account created','success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html',form=form)

if __name__=="__main__":
    app.run(debug=True)
