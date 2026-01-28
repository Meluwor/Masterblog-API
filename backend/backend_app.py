from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
        return jsonify(POSTS)

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
        return jsonify({"error": "There is no post by given id."}), 404
    POSTS.remove(post)
    return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200


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
