from ext import db, app
from models import Characters, Episodes, Seasons, Powers, Locations, Organizations, Species, Comics, Weapons, Voicecasts, StoryArcs, User

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(username="iliasuyvars20larianishaurma", password="iliabasketbalerria", role="admin")
    admin.create()