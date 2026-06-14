from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.fields import StringField, PasswordField, IntegerField, DateField, SelectField, EmailField
from wtforms.validators import DataRequired, length, equal_to, Optional
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed


class CharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    real_name = StringField('Real Name', validators=[Optional()])
    alias = StringField('Alias', validators=[Optional()])
    species_id = IntegerField('Species ID (Foreign Key)', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    gender = StringField('Gender', validators=[Optional()])
    occupation = StringField('Occupation', validators=[Optional()])
    affiliation = StringField('Affiliation (Orgs)', validators=[Optional()])
    first_appearance_episode = StringField('First Appearance (Episode)', validators=[DataRequired()])
    first_appearance_comic = StringField('First Appearance (Comic)', validators=[Optional()])
    powers = TextAreaField('Powers & Abilities', validators=[Optional()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    image = FileField('Character Portrait', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    height = StringField('Height', validators=[Optional()])
    weight = StringField('Weight', validators=[Optional()])
    relatives = TextAreaField('Relatives', validators=[Optional()])
    enemies = TextAreaField('Enemies', validators=[Optional()])
    voice_actor = StringField('Voice Actor Name', validators=[Optional()])
    quote = TextAreaField('Notable Quote', validators=[Optional()])
    submit = SubmitField('Save Character')

class EpisodeForm(FlaskForm):
    title = StringField('Episode Title', validators=[DataRequired()])
    season_id = IntegerField('Season ID (Foreign Key)', validators=[DataRequired()])
    episode_number = IntegerField('Episode Number', validators=[DataRequired()])
    air_date = StringField('Air Date', validators=[DataRequired()])
    summary = TextAreaField('Episode Summary', validators=[DataRequired()])
    runtime = StringField('Runtime', validators=[DataRequired()])
    image = FileField('Episode Thumbnail', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    featured_characters = TextAreaField('Featured Characters', validators=[DataRequired()])
    important_events = TextAreaField('Important Events', validators=[DataRequired()])
    submit = SubmitField('Save Episode')


class SeasonForm(FlaskForm):
    season_number = IntegerField('Season Number', validators=[DataRequired()])
    release_year = IntegerField('Release Year', validators=[DataRequired()])
    episode_count = IntegerField('Total Episodes', validators=[DataRequired()])
    summary = TextAreaField('Season Summary', validators=[DataRequired()])
    poster = FileField('Season Poster', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    submit = SubmitField('Save Season')


class PowerForm(FlaskForm):
    name = StringField('Power Name', validators=[DataRequired()])
    description = TextAreaField('Power Description', validators=[DataRequired()])
    power_type = StringField('Power Type (e.g., Physical, Energy)', validators=[DataRequired()])
    weaknesses = TextAreaField('Associated Weaknesses', validators=[Optional()])
    image = FileField('Power Icon/Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    submit = SubmitField('Save Power')


class LocationForm(FlaskForm):
    name = StringField('Location Name', validators=[DataRequired()])
    location_type = StringField('Location Type (e.g., Planet, City, Lab)', validators=[DataRequired()])
    description = TextAreaField('Location Description', validators=[DataRequired()])
    image = FileField('Location Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    first_appearance = StringField('First Appearance', validators=[Optional()])
    submit = SubmitField('Save Location')


class OrganizationForm(FlaskForm):
    name = StringField('Organization Name', validators=[DataRequired()])
    description = TextAreaField('Organization Description', validators=[DataRequired()])
    leader = StringField('Leader', validators=[Optional()])
    headquarters = StringField('Headquarters Location', validators=[Optional()])
    status = StringField('Status (Active, Disbanded)', validators=[DataRequired()])
    image = FileField('Organization Logo/Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    submit = SubmitField('Save Organization')


class SpeciesForm(FlaskForm):
    name = StringField('Species Name', validators=[DataRequired()])
    homeworld = StringField('Homeworld Planet', validators=[Optional()])
    description = TextAreaField('Species Description', validators=[DataRequired()])
    abilities = TextAreaField('Common Traits/Abilities', validators=[Optional()])
    weaknesses = TextAreaField('Species Weaknesses', validators=[Optional()])
    image = FileField('Species Representative Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    submit = SubmitField('Save Species')


class ComicForm(FlaskForm):
    issue_number = IntegerField('Issue Number', validators=[DataRequired()])
    title = StringField('Comic Title', validators=[DataRequired()])
    release_date = StringField('Release Date', validators=[DataRequired()])
    summary = TextAreaField('Issue Summary', validators=[DataRequired()])
    cover_image = FileField('Comic Cover Art', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    submit = SubmitField('Save Comic Issue')


class WeaponForm(FlaskForm):
    name = StringField('Weapon/Tech Name', validators=[DataRequired()])
    creator = StringField('Creator/Developer', validators=[Optional()])
    description = TextAreaField('Description & Capabilities', validators=[DataRequired()])
    weapon_type = StringField('Weapon Type (e.g., Ranged, Armor)', validators=[DataRequired()])
    image = FileField('Weapon/Tech Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    first_appearance = StringField('First Appearance', validators=[DataRequired()])
    submit = SubmitField('Save Weapon')


class VoicecastForm(FlaskForm):
    actor_name = StringField('Voice Actor Name', validators=[DataRequired()])
    character_id = IntegerField('Character ID (Foreign Key Link)', validators=[DataRequired()])
    image = FileField('Actor Headshot', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    biography = TextAreaField('Actor Biography', validators=[DataRequired()])
    submit = SubmitField('Save Voice Actor')


class StoryArcForm(FlaskForm):
    title = StringField('Story Arc Title', validators=[DataRequired()])
    description = TextAreaField('Arc Description/Overview', validators=[DataRequired()])
    start_episode = IntegerField('Start Episode ID (Foreign Key)', validators=[DataRequired()])
    end_episode = IntegerField('End Episode ID (Foreign Key)', validators=[DataRequired()])
    image = FileField('Story Arc Promotional Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', "webp", "avif"])])
    submit = SubmitField('Save Story Arc')

class registerForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    password = PasswordField("Enter Password", validators=[DataRequired(), length(min=8, max=12)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), equal_to("password", message="Passwords must match")])
    email = EmailField("Enter Email", validators=[DataRequired()])
    mobile = IntegerField("Enter Mobile Number", validators=[DataRequired()])
    birthdate = DateField("Enter Birth Date", validators=[DataRequired()])
    gender = SelectField("Enter Gender", choices=["Choose Gender","male", "female"])
    country = SelectField(choices=["Choose Country", "Georgia", "USA", "Germany", "Canada"], validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8, max=24)])