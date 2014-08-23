from flask import render_template, request, redirect, url_for, flash

from app import app
from models import MyContact
from database import db_session


@app.route('/')
def index():
    contacts = MyContact.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/add', methods=['POST'])
def add_contact():
    contact = MyContact(name=request.form.get('name'),
                        number=request.form.get('number'),
                        about=request.form.get('about')
                        )
    db_session.add(contact)
    db_session.commit()
    flash('New contact saved !!')
    return redirect(url_for('index'))


@app.route('/edit/contact/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    contact = MyContact.query.get(contact_id)
    if request.method == "GET":
        # show the contact
        return render_template('show_update_contact.html', contact=contact)
    elif request.method == "POST":
        # its update
        contact.name = request.form.get('name')
        contact.number = request.form.get('number')
        contact.about = request.form.get('about')
        db_session.commit()
        flash('Contact Updated !!')
        return redirect(url_for('index'))


@app.route('/delete/contact/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    contact = MyContact.query.get(contact_id)
    db_session.delete(contact)
    db_session.commit()
    flash('Contact Deleted !!')
    return redirect(url_for('index'))
