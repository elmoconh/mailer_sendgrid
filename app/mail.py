from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from app.db import get_db
import sendgrid
from sendgrid.helpers.mail import *

bp = Blueprint('mail', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute('SELECT * FROM email ORDER BY id DESC')
    emails = c.fetchall()

    return render_template('mails/index.html' , emails = emails)

@bp.route('/create' , methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        content = request.form['content']
        errors = []

        # Validations
        if not email:
            errors.append('Falta el email')
        if not subject:
            errors.append('Falta el Asunto')
        if not content:
            errors.append('Falta el contenido')
        
        #  Save in database
        if len(errors) == 0:            
            send_mail(email, subject, content)
            db, c = get_db()
            c.execute('INSERT INTO email (email, subject, content) VALUES (%s, %s, %s)', (email, subject, content))
            db.commit()
            return redirect(url_for('mail.index'))
        else:
           for error in errors:
                flash(error)
        
    return render_template('mails/create.html')


def send_mail(email, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
    from_email = Email(current_app.config['FROM_EMAIL'])
    to_email = To(email)
    subject = subject
    content = Content("text/plain", content)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response)
