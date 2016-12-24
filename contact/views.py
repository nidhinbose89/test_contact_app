from flask import render_template, request, flash, jsonify
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
            # TODO - implement serializer in model
            return jsonify({'data': {
                'id': contact.id,
                'name': contact.name,
                'phone': contact.number,
                'about': contact.about
            }})
        except Exception as e:
            raise e

    @app.route('/contact/<int:contact_id>', methods=['GET', 'PUT', 'DELETE'])
    def contact(contact_id):
        contact = MyContact.query.get(contact_id)
        if request.method == "PUT":
            # its update
            contact.name = request.json.get('name')
            contact.number = request.json.get('phone')
            contact.about = request.json.get('about')
            db_session.commit()

            return jsonify({'data': {
                'id': contact.id,
                'name': contact.name,
                'phone': contact.number,
                'about': contact.about
            }})
        elif request.method == "DELETE":
            db_session.delete(contact)
            db_session.commit()
            flash('Contact Deleted !!')
            return jsonify({'data': {'message': 'Deleted'}})
