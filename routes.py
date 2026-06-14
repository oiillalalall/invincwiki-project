from os import path
from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from ext import app, db
from models import (
    Characters, Episodes, Seasons, Powers, Locations,
    Organizations, Species, Comics, Weapons, Voicecasts, StoryArcs, User
)
from forms import (
    CharacterForm, EpisodeForm, SeasonForm, PowerForm, LocationForm,
    OrganizationForm, SpeciesForm, ComicForm, WeaponForm, VoicecastForm, StoryArcForm, registerForm, LoginForm
)

@app.route('/')
def home():
    return render_template("home.html", role="admin")

@app.route('/add_character', methods=["GET", "POST"])
@login_required
def add_character():
    form = CharacterForm()
    if form.validate_on_submit():
        new_item = Characters(
            name=form.name.data, real_name=form.real_name.data, alias=form.alias.data,
            species_id=form.species_id.data, status=form.status.data, gender=form.gender.data,
            occupation=form.occupation.data, affiliation=form.affiliation.data,
            first_appearance_episode=form.first_appearance_episode.data, first_appearance_comic=form.first_appearance_comic.data,
            powers=form.powers.data, biography=form.biography.data, height=form.height.data,
            weight=form.weight.data, relatives=form.relatives.data, enemies=form.enemies.data,
            voice_actor=form.voice_actor.data, quote=form.quote.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("characters"))
    return render_template("add_character.html", form=form)


@app.route('/edit_character/<int:id>', methods=['GET', 'POST'])
def edit_character(id):
    item = Characters.query.get(id)
    form = CharacterForm(
        name=item.name,
        real_name=item.real_name,
        alias=item.alias,
        species_id=item.species_id,
        status=item.status,
        gender=item.gender,
        occupation=item.occupation,
        affiliation=item.affiliation,
        first_appearance_episode=item.first_appearance_episode,
        first_appearance_comic=item.first_appearance_comic,
        powers=item.powers,
        biography=item.biography,
        height=item.height,
        weight=item.weight,
        relatives=item.relatives,
        enemies=item.enemies,
        voice_actor=item.voice_actor,
        quote=item.quote)
    if form.validate_on_submit():
        item.name = form.name.data
        item.real_name = form.real_name.data
        item.alias = form.alias.data
        item.species_id = form.species_id.data
        item.status = form.status.data
        item.gender = form.gender.data
        item.occupation = form.occupation.data
        item.affiliation = form.affiliation.data
        item.first_appearance_episode = form.first_appearance_episode.data
        item.first_appearance_comic = form.first_appearance_comic.data
        item.powers = form.powers.data
        item.biography = form.biography.data
        item.height = form.height.data
        item.weight = form.weight.data
        item.relatives = form.relatives.data
        item.enemies = form.enemies.data
        item.voice_actor = form.voice_actor.data
        item.quote = form.quote.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            item.image = img.filename

        item.save()
        return redirect(url_for("characters"))
    return render_template("edit_character.html", form=form)
#madloba claude rom errorebi gamomiswore vaxxx

@app.route('/add_episode', methods=["GET", "POST"])
@login_required
def add_episode():
    form = EpisodeForm()
    if form.validate_on_submit():
        new_item = Episodes(
            title=form.title.data, season_id=form.season_id.data, episode_number=form.episode_number.data,
            air_date=form.air_date.data, summary=form.summary.data, runtime=form.runtime.data,
            featured_characters=form.featured_characters.data, important_events=form.important_events.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("episodes"))
    return render_template("add_episode.html", form=form)


@app.route('/edit_episode/<int:id>', methods=['GET', 'POST'])
def edit_episode(id):
    episode = Episodes.query.get(id)
    form = EpisodeForm(
        title=episode.title,
        season_id=episode.season_id,
        episode_number=episode.episode_number,
        air_date=episode.air_date,
        summary=episode.summary,
        runtime=episode.runtime,
        featured_characters=episode.featured_characters,
        important_events=episode.important_events)
    if form.validate_on_submit():
        episode.title = form.title.data
        episode.season_id = form.season_id.data
        episode.episode_number = form.episode_number.data
        episode.air_date = form.air_date.data
        episode.summary = form.summary.data
        episode.runtime = form.runtime.data
        episode.featured_characters = form.featured_characters.data
        episode.important_events = form.important_events.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            episode.image = img.filename
        episode.save()
        return redirect(url_for("episodes"))
    return render_template("edit_episode.html", form=form)

@app.route('/add_season', methods=["GET", "POST"])
@login_required
def add_season():
    form = SeasonForm()
    if form.validate_on_submit():
        new_item = Seasons(
            season_number=form.season_number.data, release_year=form.release_year.data,
            episode_count=form.episode_count.data, summary=form.summary.data
        )
        img = form.poster.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.poster = img.filename
        new_item.create()
        return redirect(url_for("seasons"))
    return render_template("add_season.html", form=form)


@app.route('/edit_season/<int:id>', methods=['GET', 'POST'])
def edit_season(id):
    season = Seasons.query.get(id)
    form = SeasonForm(
        season_number=season.season_number,
        release_year=season.release_year,
        episode_count=season.episode_count,
        summary=season.summary)
    if form.validate_on_submit():
        season.season_number = form.season_number.data
        season.release_year = form.release_year.data
        season.episode_count = form.episode_count.data
        season.summary = form.summary.data
        img = form.poster.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            season.poster = img.filename
        season.save()
        return redirect(url_for("seasons"))
    return render_template("edit_season.html", form=form)

@app.route('/add_power', methods=["GET", "POST"])
@login_required
def add_power():
    form = PowerForm()
    if form.validate_on_submit():
        new_item = Powers(
            name=form.name.data, description=form.description.data,
            power_type=form.power_type.data, weaknesses=form.weaknesses.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("powers"))
    return render_template("add_power.html", form=form)


@app.route('/edit_power/<int:id>', methods=['GET', 'POST'])
def edit_power(id):
    power = Powers.query.get(id)
    form = PowerForm(
        name=power.name,
        description=power.description,
        power_type=power.power_type,
        weaknesses=power.weaknesses)
    if form.validate_on_submit():
        power.name = form.name.data
        power.description = form.description.data
        power.power_type = form.power_type.data
        power.weaknesses = form.weaknesses.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            power.image = img.filename
        power.save()
        return redirect(url_for("powers"))
    return render_template("edit_power.html", form=form)

@app.route('/add_location', methods=["GET", "POST"])
@login_required
def add_location():
    form = LocationForm()
    if form.validate_on_submit():
        new_item = Locations(
            name=form.name.data, location_type=form.location_type.data,
            description=form.description.data, first_appearance=form.first_appearance.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("locations"))
    return render_template("add_location.html", form=form)


@app.route('/edit_location/<int:id>', methods=['GET', 'POST'])
def edit_location(id):
    location = Locations.query.get(id)
    form = LocationForm(
        name=location.name,
        location_type=location.location_type,
        description=location.description,
        first_appearance=location.first_appearance)
    if form.validate_on_submit():
        location.name = form.name.data
        location.location_type = form.location_type.data
        location.description = form.description.data
        location.first_appearance = form.first_appearance.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            location.image = img.filename
        location.save()
        return redirect(url_for("locations"))
    return render_template("edit_location.html", form=form)

@app.route('/add_organization', methods=["GET", "POST"])
@login_required
def add_organization():
    form = OrganizationForm()
    if form.validate_on_submit():
        new_item = Organizations(
            name=form.name.data, description=form.description.data, leader=form.leader.data,
            headquarters=form.headquarters.data, status=form.status.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("organizations"))
    return render_template("add_organization.html", form=form)


@app.route('/edit_organization/<int:id>', methods=['GET', 'POST'])
def edit_organization(id):
    org = Organizations.query.get(id)
    form = OrganizationForm(
        name=org.name,
        description=org.description,
        leader=org.leader,
        headquarters=org.headquarters,
        status=org.status)
    if form.validate_on_submit():
        org.name = form.name.data
        org.description = form.description.data
        org.leader = form.leader.data
        org.headquarters = form.headquarters.data
        org.status = form.status.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            org.image = img.filename
        org.save()
        return redirect(url_for("organizations"))
    return render_template("edit_organization.html", form=form)

@app.route('/add_specie', methods=["GET", "POST"])
@login_required
def add_species():
    form = SpeciesForm()
    if form.validate_on_submit():
        new_item = Species(
            name=form.name.data, homeworld=form.homeworld.data, description=form.description.data,
            abilities=form.abilities.data, weaknesses=form.weaknesses.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("species"))
    return render_template("add_specie.html", form=form)


@app.route('/edit_specie/<int:id>', methods=['GET', 'POST'])
def edit_species(id):
    species = Species.query.get(id)
    form = SpeciesForm(
        name=species.name,
        homeworld=species.homeworld,
        description=species.description,
        abilities=species.abilities,
        weaknesses=species.weaknesses)
    if form.validate_on_submit():
        species.name = form.name.data
        species.homeworld = form.homeworld.data
        species.description = form.description.data
        species.abilities = form.abilities.data
        species.weaknesses = form.weaknesses.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            species.image = img.filename
        species.save()
        return redirect(url_for("species"))
    return render_template("edit_specie.html", form=form)

@app.route('/add_comic', methods=["GET", "POST"])
@login_required
def add_comic():
    form = ComicForm()
    if form.validate_on_submit():
        new_item = Comics(
            issue_number=form.issue_number.data, title=form.title.data,
            release_date=form.release_date.data, summary=form.summary.data
        )
        img = form.cover_image.data  # Map 'cover_image' field
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.cover_image = img.filename
        new_item.create()
        return redirect(url_for("comics"))
    return render_template("add_comic.html", form=form)


@app.route('/edit_comic/<int:id>', methods=['GET', 'POST'])
def edit_comic(id):
    comic = Comics.query.get(id)
    form = ComicForm(
        issue_number=comic.issue_number,
        title=comic.title,
        release_date=comic.release_date,
        summary=comic.summary)
    if form.validate_on_submit():
        comic.issue_number = form.issue_number.data
        comic.title = form.title.data
        comic.release_date = form.release_date.data
        comic.summary = form.summary.data
        img = form.cover_image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            comic.cover_image = img.filename
        comic.save()
        return redirect(url_for("comics"))
    return render_template("edit_comic.html", form=form)

@app.route('/add_weapon', methods=["GET", "POST"])
@login_required
def add_weapon():
    form = WeaponForm()
    if form.validate_on_submit():
        new_item = Weapons(
            name=form.name.data, creator=form.creator.data, description=form.description.data,
            weapon_type=form.weapon_type.data, first_appearance=form.first_appearance.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("weapons"))
    return render_template("add_weapon.html", form=form)


@app.route('/edit_weapon/<int:id>', methods=['GET', 'POST'])
def edit_weapon(id):
    weapon = Weapons.query.get(id)
    form = WeaponForm(
        name=weapon.name,
        creator=weapon.creator,
        description=weapon.description,
        weapon_type=weapon.weapon_type,
        first_appearance=weapon.first_appearance)
    if form.validate_on_submit():
        weapon.name = form.name.data
        weapon.creator = form.creator.data
        weapon.description = form.description.data
        weapon.weapon_type = form.weapon_type.data
        weapon.first_appearance = form.first_appearance.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            weapon.image = img.filename
        weapon.save()
        return redirect(url_for("weapons"))
    return render_template("edit_weapon.html", form=form)

@app.route('/add_voicecast', methods=["GET", "POST"])
@login_required
def add_voicecast():
    form = VoicecastForm()
    if form.validate_on_submit():
        new_item = Voicecasts(
            actor_name=form.actor_name.data, character_id=form.character_id.data,
            biography=form.biography.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("voicecasts"))
    return render_template("add_voicecast.html", form=form)


@app.route('/edit_voicecast/<int:id>', methods=['GET', 'POST'])
def edit_voicecast(id):
    cast = Voicecasts.query.get(id)
    form = VoicecastForm(
        actor_name=cast.actor_name,
        character_id=cast.character_id,
        biography=cast.biography)
    if form.validate_on_submit():
        cast.actor_name = form.actor_name.data
        cast.character_id = form.character_id.data
        cast.biography = form.biography.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            cast.image = img.filename
        cast.save()
        return redirect(url_for("voicecasts"))
    return render_template("edit_voicecast.html", form=form)

@app.route('/add_storyarc', methods=["GET", "POST"])
@login_required
def add_storyarc():
    form = StoryArcForm()
    if form.validate_on_submit():
        new_item = StoryArcs(
            title=form.title.data, description=form.description.data,
            start_episode=form.start_episode.data, end_episode=form.end_episode.data
        )
        img = form.image.data
        if img and img.filename:
            img.save(path.join(app.root_path, "static", "images", img.filename))
            new_item.image = img.filename
        new_item.create()
        return redirect(url_for("storyarcs"))
    return render_template("add_storyarc.html", form=form)


@app.route('/edit_storyarc/<int:id>', methods=['GET', 'POST'])
def edit_storyarc(id):
    arc = StoryArcs.query.get(id)
    form = StoryArcForm(
        title=arc.title,
        description=arc.description,
        start_episode=arc.start_episode,
        end_episode=arc.end_episode)
    if form.validate_on_submit():
        arc.title = form.title.data
        arc.description = form.description.data
        arc.start_episode = form.start_episode.data
        arc.end_episode = form.end_episode.data
        img = form.image.data
        if img and img.filename:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            arc.image = img.filename
        arc.save()
        return redirect(url_for("storyarcs"))
    return render_template("edit_storyarc.html", form=form)

@app.route('/characters')
def characters():
    characters = Characters.query.all()
    return render_template('characters.html',characters=characters)


@app.route('/episodes')
def episodes():
    episodes = Episodes.query.all()
    return render_template('episodes.html',episodes=episodes)


@app.route('/seasons')
def seasons():
    seasons = Seasons.query.all()
    return render_template('seasons.html',seasons=seasons)


@app.route('/powers')
def powers():
    powers = Powers.query.all()
    return render_template('powers.html',powers=powers)


@app.route('/locations')
def locations():
    locations = Locations.query.all()
    return render_template('locations.html',locations=locations)


@app.route('/organizations')
def organizations():
    organizations = Organizations.query.all()
    return render_template('organizations.html',organizations=organizations)


@app.route('/species')
def species():
    species = Species.query.all()
    return render_template('species.html',species=species)


@app.route('/comics')
def comics():
    comics = Comics.query.all()
    return render_template('comics.html',comics=comics)


@app.route('/weapons')
def weapons():
    weapons = Weapons.query.all()
    return render_template('weapons.html',weapons=weapons)


@app.route('/voicecasts')
def voicecasts():
    voicecasts = Voicecasts.query.all()
    return render_template('voicecasts.html',voicecasts=voicecasts)


@app.route('/storyarcs')
def storyarcs():
    storyarcs = StoryArcs.query.all()
    return render_template('storyarcs.html', storyarcs=storyarcs)


@app.route('/characters/<int:id>')
def character(id):
    character = Characters.query.get(id)
    species = Species.query.get(character.species_id)
    return render_template('character.html', character=character, species=species)



@app.route('/episodes/<int:id>')
def episode(id):
    item = Episodes.query.get(id)
    return render_template('episode.html', item=item)

@app.route('/seasons/<int:id>')
def season(id):
    item = Seasons.query.get(id)
    return render_template('season.html', item=item)


@app.route('/powers/<int:id>')
def power(id):
    item = Powers.query.get(id)
    return render_template('power.html', item=item)


@app.route('/locations/<int:id>')
def location(id):
    item = Locations.query.get(id)
    return render_template('location.html', item=item)


@app.route('/organizations/<int:id>')
def organization(id):
    item = Organizations.query.get(id)
    return render_template('organization.html', item=item)

@app.route('/species/<int:id>')
def species_detail(id):
    item = Species.query.get(id)
    return render_template('specie.html', item=item)


@app.route('/comics/<int:id>')
def comic(id):
    item = Comics.query.get(id)
    return render_template('comic.html', item=item)



@app.route('/weapons/<int:id>')
def weapon(id):
    item = Weapons.query.get(id)
    return render_template('weapon.html', item=item)


@app.route('/voicecasts/<int:id>')
def voicecast(id):
    item = Voicecasts.query.get(id)
    return render_template('voicecast.html', item=item)

@app.route('/storyarcs/<int:id>')
def storyarc(id):
    item = StoryArcs.query.get(id)
    return render_template('storyarc.html', item=item)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.create()
        return redirect("/")
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User.query.filter(User.username == form.username.data).first()
    if user:
        login_user(user)
        return redirect("/")
    return render_template('login.html', form=form)

@app.route('/logout')
def log_out():
    logout_user()
    return redirect("/")

@app.route("/delete_character/<int:id>")
def delete_character(id):
    character = Characters.query.get(id)
    if character:
        character.delete()
    return redirect(url_for("characters"))

@app.route("/delete_episode/<int:id>")
def delete_episode(id):
    episode = Episodes.query.get(id)
    if episode:
        episode.delete()
    return redirect(url_for("episodes"))

@app.route("/delete_season/<int:id>")
def delete_season(id):
    season = Seasons.query.get(id)
    if season:
        season.delete()
    return redirect(url_for("seasons"))

@app.route("/delete_power/<int:id>")
def delete_power(id):
    power = Powers.query.get(id)
    if power:
        power.delete()
    return redirect(url_for("powers"))

@app.route("/delete_location/<int:id>")
def delete_location(id):
    location = Locations.query.get(id)
    if location:
        location.delete()
    return redirect(url_for("locations"))

@app.route("/delete_organization/<int:id>")
def delete_organization(id):
    org = Organizations.query.get(id)
    if org:
        org.delete()
    return redirect(url_for("organizations"))

@app.route("/delete_specie/<int:id>")
def delete_species(id):
    species = Species.query.get(id)
    if species:
        species.delete()
    return redirect(url_for("species_list"))

@app.route("/delete_comic/<int:id>")
def delete_comic(id):
    comic = Comics.query.get(id)
    if comic:
        comic.delete()
    return redirect(url_for("comics"))

@app.route("/delete_weapon/<int:id>")
def delete_weapon(id):
    weapon = Weapons.query.get(id)
    if weapon:
        weapon.delete()
    return redirect(url_for("weapons"))

@app.route("/delete_voicecast/<int:id>")
def delete_voicecast(id):
    cast = Voicecasts.query.get(id)
    if cast:
        cast.delete()
    return redirect(url_for("voicecasts"))

@app.route("/delete_storyarc/<int:id>")
def delete_storyarc(id):
    arc = StoryArcs.query.get(id)
    if arc:
        arc.delete()
    return redirect(url_for("storyarcs"))

@app.route('/profile')
def profile():
    return render_template('profile.html', profile=current_user)

@app.route('/search')
def search():
    search_text = request.args.get('text')
    if not search_text:
        return redirect(url_for("home"))
    search_query = f'%{search_text}%'
    results = {
        "characters": Characters.query.filter(Characters.name.ilike(search_query)).all(),
        "episodes": Episodes.query.filter(Episodes.title.ilike(search_query)).all(),
        "seasons": Seasons.query.filter(Seasons.title.ilike(search_query)).all(),
        "powers": Powers.query.filter(Powers.name.ilike(search_query)).all(),
        "locations": Locations.query.filter(Locations.name.ilike(search_query)).all(),
        "organizations": Organizations.query.filter(Organizations.name.ilike(search_query)).all(),
        "species": Species.query.filter(Species.name.ilike(search_query)).all(),
        "comics": Comics.query.filter(Comics.title.ilike(search_query)).all(),
        "weapons": Weapons.query.filter(Weapons.name.ilike(search_query)).all(),
        "voicecasts": Voicecasts.query.filter(Voicecasts.name.ilike(search_query)).all(),
        "storyarcs": StoryArcs.query.filter(StoryArcs.name.ilike(search_query)).all(),
    }
    total_results = sum(len(items) for items in results.values())

    return render_template(
        'search_results.html',
        results=results,
        total=total_results,
        query=search_text,
        role="admin"
    )

#ufff shemovevle ais es rro gamiketa
#wtf ver gavaswore agarr maq tvini karroche es ar moqmedebs