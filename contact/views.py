from flask import render_template, request, redirect, url_for, flash, jsonify
from models import MyContact


def reg_views(app):
    db_session = app.config['DATABASE']

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/get_contacts')
    def get_contacts():
        contacts = MyContact.query.all()
        contact_list = []
        for contact in contacts:
            contact_item = {
                'id': contact.id,
                'name': contact.name,
                'phone': contact.number,
                'about': contact.about,
            }
            contact_list.append(contact_item)
        return jsonify({'data': contact_list})

    @app.route('/add', methods=['POST'])
    def add_contact():
        try:
            contact = MyContact(name=request.json.get('name'),
                                number=request.json.get('phone'),
                                about=request.json.get('about')
                                )
            db_session.add(contact)
            db_session.commit()
            flash('New contact saved !!')
        except Exception as e:
            flash(e.message)

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
            return render_template('show_update_contact.html', contact=contact)

    @app.route('/delete/contact/<int:contact_id>', methods=['POST'])
    def delete_contact(contact_id):
        contact = MyContact.query.get(contact_id)
        db_session.delete(contact)
        db_session.commit()
        flash('Contact Deleted !!')
        return redirect(url_for('index'))
