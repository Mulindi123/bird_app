from app import app
from models import db, Bird

with app.app_context():
    print("Deleting existing birds...")
    Bird.query.delete()

    print("Creating bird objects...")
    chickadee = Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus')
    grackle = Bird(name='Grackle', species='Quiscalus Quiscula')
    starling = Bird(name='Common Starling', species='Sturnus Vulgaris')
    dove = Bird(name='Mourning Dove', species='Zenaida Macroura')

    bird_objects = [chickadee, grackle, starling, dove]

    print("Adding bird objects to transaction...")
    db.session.add_all(bird_objects)

    print("Committing transaction...")
    db.session.commit()

    print("Complete!")