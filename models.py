from ext import db, login_manager
from flask_login import UserMixin

from ext import db

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Characters(db.Model,BaseModel):
    __tablename__ = 'characters'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    real_name = db.Column(db.String())
    alias = db.Column(db.String())
    species_id = db.Column(db.Integer(), db.ForeignKey("species.id"), nullable=False)
    status = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String())
    occupation = db.Column(db.String())
    affiliation = db.Column(db.String())
    first_appearance_episode = db.Column(db.String(), nullable=False)
    first_appearance_comic = db.Column(db.String())
    powers = db.Column(db.Text())
    biography = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(), server_default='add_image.jpg')
    height = db.Column(db.String())
    weight = db.Column(db.String())
    relatives = db.Column(db.Text())
    enemies = db.Column(db.Text())
    voice_actor = db.Column(db.String())
    quote = db.Column(db.Text())

class Episodes(db.Model,BaseModel):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    season_id = db.Column(db.Integer(), db.ForeignKey("seasons.id"), nullable=False)
    episode_number = db.Column(db.Integer(), nullable=False)
    air_date = db.Column(db.String(), nullable=False)
    summary = db.Column(db.Text(), nullable=False)
    runtime = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), server_default='add_image.jpg')
    featured_characters = db.Column(db.Text(), nullable=False)
    important_events = db.Column(db.Text(), nullable=False)

class Seasons(db.Model,BaseModel):
    __tablename__ = 'seasons'

    id = db.Column(db.Integer(), primary_key=True)
    season_number = db.Column(db.Integer(), nullable=False)
    release_year = db.Column(db.Integer(), nullable=False)
    episode_count = db.Column(db.Integer(), nullable=False)
    summary = db.Column(db.Text(), nullable=False)
    poster = db.Column(db.String(), server_default='add_image.jpg')

class Powers(db.Model,BaseModel):
    __tablename__ = 'powers'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    power_type = db.Column(db.String(), nullable=False)
    weaknesses = db.Column(db.Text())
    image = db.Column(db.String(), server_default='add_image.jpg')

class Locations(db.Model,BaseModel):
    __tablename__ = 'locations'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    location_type  = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(), server_default='add_image.jpg')
    first_appearance = db.Column(db.String())

class Organizations(db.Model,BaseModel):
    __tablename__ = 'organizations'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    leader = db.Column(db.String())
    headquarters = db.Column(db.String())
    status = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), server_default='add_image.jpg')

class Species(db.Model,BaseModel):
    __tablename__ = 'species'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    homeworld = db.Column(db.String())
    description = db.Column(db.Text(), nullable=False)
    abilities = db.Column(db.Text())
    weaknesses = db.Column(db.Text())
    image = db.Column(db.String(), server_default='add_image.jpg')

class Comics(db.Model,BaseModel):
    __tablename__ = 'comics'

    id = db.Column(db.Integer(), primary_key=True)
    issue_number = db.Column(db.Integer(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.String(), nullable=False)
    summary = db.Column(db.Text(), nullable=False)
    cover_image = db.Column(db.String(), server_default='add_image.jpg')

class Weapons(db.Model,BaseModel):
    __tablename__ = 'weapons'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    creator = db.Column(db.String())
    description = db.Column(db.Text(), nullable=False)
    weapon_type = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), server_default='add_image.jpg')
    first_appearance = db.Column(db.String(), nullable=False)

class Voicecasts(db.Model,BaseModel):
    __tablename__ = 'voicecasts'

    id = db.Column(db.Integer(), primary_key=True)
    actor_name = db.Column(db.String(), nullable=False)
    character_id = db.Column(db.Integer(), db.ForeignKey("characters.id"), nullable=False)
    image = db.Column(db.String(), server_default='add_image.jpg')
    biography = db.Column(db.String(), nullable=False)

class StoryArcs(db.Model,BaseModel):
    __tablename__ = 'story_arcs'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    start_episode = db.Column(db.Integer(), db.ForeignKey('episodes.id'), nullable=False)
    end_episode = db.Column(db.Integer(), db.ForeignKey('episodes.id'),  nullable=False)
    image = db.Column(db.String(), server_default='add_image.jpg')


class User(db.Model,BaseModel, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    role = db.Column(db.String(), default='guest')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)