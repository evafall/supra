from flask import Flask,render_template,request
from notifications import send_email

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/partners',methods=['GET','POST'])
def partners():
    return render_template('partners.html')

@app.route('/single',methods=['GET','POST'])
def single():
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        requirements = request.form['requirements']

        data = [name,phone_number,email,requirements]

        subject = "Enquiry"
        fileToSend = None
        msgg = " Name : "+name+" \n Phone Number : "+phone_number+" \n Email : "+email+" \n Requirements : "+requirements+"  "

        toaddr = "supra.enterprises7@gmail.com"
        send_email(msgg,subject,toaddr,fileToSend)

        return render_template('index.html')


@app.route('/services',methods=['GET','POST'])
def services():
    return render_template('services.html')


if __name__ == '__main__':
   app.run(debug=True)
