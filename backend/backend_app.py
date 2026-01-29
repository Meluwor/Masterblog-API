from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "Kaffee-Code-Konfetti", "content": "Warum Koffein die beste Syntax-Hervorhebung ist."},
    {"id": 2, "title": "Die Kunst des Nichtstuns", "content": "Ein Guide für gestresste Entwickler."},
    {"id": 3, "title": "Veganer Speck aus Bananen?", "content": "Ein kulinarisches Experiment mit fragwürdigem Ausgang."},
    {"id": 4, "title": "Mars-Kolonie Update", "content": "Die ersten 100 Tage ohne WLAN – ein Überlebensbericht."},
    {"id": 5, "title": "Minimalismus im Kleiderschrank", "content": "Warum ich nur noch 7 identische schwarze T-Shirts besitze."},
    {"id": 6, "title": "Die Psychologie der Schriftarten", "content": "Warum dich Comic Sans heimlich aggressiv macht."},
    {"id": 7, "title": "Urban Gardening für Faulpelze", "content": "Kakteen sind auch nur Blumen mit Charakter."},
    {"id": 8, "title": "Quantenphysik beim Frühstück", "content": "Ist das Ei gleichzeitig gekocht und roh?"},
    {"id": 9, "title": "Analoge Fotografie im 21. Jahrhundert", "content": "Warten auf den Film: Entschleunigung pur."},
    {"id": 10, "title": "Geheimnisse der Pizzabäcker", "content": "Der Teig muss 72 Stunden ruhen, genau wie ich."},
    {"id": 11, "title": "Das Comeback der Schallplatte", "content": "Es knistert nicht, es lebt."},
    {"id": 12, "title": "Homeoffice im Baumhaus", "content": "Wie man Termine mit Eichhörnchen koordiniert."},
    {"id": 13, "title": "Die Macht der Gewohnheit", "content": "Jeden Tag um 5 Uhr aufstehen – Ein Selbstversuch."},
    {"id": 14, "title": "Vom Bug zum Feature", "content": "Wie man Programmierfehler als Innovation verkauft."},
    {"id": 15, "title": "Nachhaltig Reisen", "content": "Mit dem Klapprad durch die Alpen."},
    {"id": 16, "title": "DIY: Roboter-Staubsauger-Rennen", "content": "Wenn Technik im Wohnzimmer außer Kontrolle gerät."},
    {"id": 17, "title": "Warum wir Emojis brauchen", "content": "Eine linguistische Analyse des lachenden Kackhaufens."},
    {"id": 18, "title": "Yoga für Tastatur-Akrobaten", "content": "Dehnübungen für den schmerzenden Maus-Arm."},
    {"id": 19, "title": "Künstliche Intelligenz und Humor", "content": "Warum ChatGPT keine guten Flachwitze erzählen kann."},
    {"id": 20, "title": "Die Renaissance der Brettspiele", "content": "Mensch ärgere dich nicht – digital detoxed."},
    {"id": 21, "title": "Survival-Guide: Festival-Camping", "content": "Drei Tage ohne Dusche, aber mit viel Bass."},
    {"id": 22, "title": "Büropflanzen-Flüsterer", "content": "Warum meine Monstera mehr Follower hat als ich."},
    {"id": 23, "title": "Blockchain einfach erklärt", "content": "Stell dir vor, dein Tagebuch gehört allen."},
    {"id": 24, "title": "Die Ästhetik des Brutalismus", "content": "Beton ist das neue Samt."},
    {"id": 25, "title": "Weltraumtourismus für Anfänger", "content": "Was man beim Packen für die ISS beachten muss."},
    {"id": 26, "title": "Slow-Cooking Rezepte", "content": "Acht Stunden warten für ein Gulasch – lohnt es sich?"},
    {"id": 27, "title": "Podcast-Wahn", "content": "Warum heutzutage jeder ein Mikrofon braucht."},
    {"id": 28, "title": "Die vergessene Welt der Flohmärkte", "content": "Schätze finden zwischen altem Besteck und VHS-Kassetten."},
    {"id": 29, "title": "Cybersecurity im Alltag", "content": "Warum 'Passwort123' keine gute Idee ist."},
    {"id": 30, "title": "Vom Amateur zum Marathonprofi", "content": "Die ersten 5 Kilometer sind die härtesten."},
    {"id": 31, "title": "E-Sports als Olympia-Disziplin?", "content": "Daumensport auf höchstem Niveau."},
    {"id": 32, "title": "Zukunft der Mobilität", "content": "Fliegende Autos oder doch nur mehr Lastenräder?"},
    {"id": 33, "title": "Meditation für Hibbelige", "content": "Stillsitzen ist Schwerstarbeit."},
    {"id": 34, "title": "Street-Art Touren", "content": "Hinterhof-Galerien in Berlin-Kreuzberg."},
    {"id": 35, "title": "Zero Waste Badezimmer", "content": "Haarewaschen mit Roggenmehl – ein Fazit."},
    {"id": 36, "title": "Retro-Gaming Liebe", "content": "Warum 8-Bit Grafik immer noch verzaubert."},
    {"id": 37, "title": "Der perfekte Espresso", "content": "Druck, Temperatur und eine Prise Voodoo."},
    {"id": 38, "title": "Tiny Houses: Großes Glück", "content": "Wohnen auf 15 Quadratmetern."},
    {"id": 39, "title": "Die Welt der Kryptiden", "content": "Wo versteckt sich Bigfoot eigentlich im Sommer?"},
    {"id": 40, "title": "Sprachen lernen mit Memes", "content": "Wie man fließend Internet-Slang spricht."},
    {"id": 41, "title": "Autonome Drohnen-Taxis", "content": "Über den Stau einfach hinwegfliegen."},
    {"id": 42, "title": "Wandern im Nebel", "content": "Wenn man die Aussicht nur erahnen kann."},
    {"id": 43, "title": "Smart Home Failures", "content": "Warum mein Kühlschrank mich nachts aussperrt."},
    {"id": 44, "title": "Brotbacken im Lockdown-Modus", "content": "Sauerteig-Babys brauchen Namen."},
    {"id": 45, "title": "Die Magie der Nordlichter", "content": "Tanzende Farben am Polarkreis."},
    {"id": 46, "title": "Virtual Reality Dating", "content": "Liebe auf den ersten Pixel-Blick."},
    {"id": 47, "title": "Geschichte der Videospiele", "content": "Von Pong bis Raytracing."},
    {"id": 48, "title": "Alternative Energien", "content": "Kann man mit Hamsterrädern ein Handy laden?"},
    {"id": 49, "title": "Insekten-Pasta im Test", "content": "Proteine mit Beinchen."},
    {"id": 50, "title": "Der letzte Blogpost", "content": "Warum 50 Einträge genau genug sind."}
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    sort_by = request.args.get('sort')
    sort_direction = request.args.get('direction')
    if not sort_by and not sort_direction:
        return jsonify(POSTS)
    is_valid_sort, sorted_posts = get_sorted_posts(sort_by,sort_direction)
    if is_valid_sort:
        return jsonify(sorted_posts),200
    return jsonify({"message": sorted_posts}), 400

@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided."}), 400
    title = data.get('title')
    content = data.get('content')
    if title and content:
        post_id = generate_post_id()
        post = {'id': post_id, 'title': title, 'content': content}
        POSTS.append(post)
        return jsonify(post), 201
    else:
        # I hope this is enough to inform the user
        return jsonify({"error": "You have to enter both: title and content."}), 400


#I don't like to use just id cause of potential shadowing but by task it shall be id
@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = get_post(id)
    if not post:
        return jsonify({"error": f"There is no post by given id:{id}."}), 404
    POSTS.remove(post)
    return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200


@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.get_json()
    if not data:
        #the post hasn't changed
        return jsonify({"message": f"There were no changes."}), 200
    post = get_post(id)
    if not post:
        return jsonify({"error": f"There is no post by given id:{id}."}), 404
    title = data.get('title')
    if title:
        post['title'] = title
    content = data.get('content')
    if content:
        post['content'] = content

    return jsonify(post), 200


@app.route('/api/posts/search', methods=['GET'])
def search():
    #using an empty string if no title or content to prevent None value
    search_title = request.args.get('title','').lower()
    search_content = request.args.get('content','').lower()
    if not search_title and not search_content:
        #there was no search at all the user gets the full list
        return jsonify({
            "message": "No matches found. Showing all posts instead.",
            "posts": POSTS
        }), 200
    searched_posts = get_searched_posts(search_title,search_content)
    return jsonify(searched_posts), 200


def get_sorted_posts(sort_by, sort_direction):
    """
    This function will sort all posts by title/content in oder ASC/DESC
    """
    reverse = False #default
    sort_func = lambda post: post['id'] #default
    error_message = ''
    if sort_by and sort_by in ['content', 'title']:
        sort_func = lambda post: post[sort_by].lower()
    else:
        if sort_by:
            #sort parameter was given but does not exist
            error_message += f'The sort parameter: {sort_by} is not provided. '
    if sort_direction and sort_direction in ['asc','desc']:
        reverse = sort_direction == "desc"
    else:
        if sort_direction:
            # direction parameter was given but does not exist
            error_message += f'The direction parameter: {sort_direction} is not provided.'
    if not error_message:
        return True, sorted(POSTS, key=sort_func, reverse=reverse)
    return False , error_message


def get_searched_posts(search_title, search_content):
    """
    This function will do a partial search by given title or content.
    """
    searched_posts = []
    for post in POSTS:
        if search_title and search_title in post['title'].lower():
            searched_posts.append(post)
            continue
        elif search_content and search_content in post['content'].lower():
            searched_posts.append(post)
            continue
    return searched_posts



def get_post(post_id):
    """
    This function will return a specific post by given id if possible.
    """
    for post in POSTS:
        if post['id'] == post_id:
            return post
    return None


def generate_post_id():
    """
    This function will generate a new post_id.
    """
    if POSTS:
        return POSTS[-1]["id"] + 1
    return 1


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
