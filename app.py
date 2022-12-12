"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '12345678'
connect_db(app)


def seriazlie_cupcake(cupcake):
    """Serialize a cupcake SQLALCHEMY OBJ to dict"""
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }
@app.route('/index')
def index():
    """Render and return index page"""
    cupcakes = Cupcake.query.all()
    return render_template('index.html', cupcakes = cupcakes)

@app.route('/api/cupcakes')
def list_cupcakes():
    """Return JSON with all cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """Return data about a specific cupcake in JSON"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes', methods = ['POST'])
def create_cupcake():
    """Create a cupcake with flavor, rating, size, etc."""
    new_cupcake = Cupcake(id = request.json['id'],
    flavor = request.json['flavor'],
    size = request.json['size'],
    rating = request.json['size'],
    image = request.json['image'])

    with app.app_context():
        db.session.add(new_cupcake)
        db.session.commit()
    resp_json = jsonify(cupcake = new_cupcake.serialize())
    return (resp_json, 201)

@app.route('/api/cupcakes/<int:id>', methods = ['PATCH'])
def update_cupcake(id):
    """Update a particular cupcake and response with JSON of that updated cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.id = request.json.get('id', cupcake.id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    
    with app.app_context():
        db.session.commit()
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods = ['DELETE'])
def delete_cupcake(id):
    """delete a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    with app.app_context():
        db.session.delete(cupcake)
        db.session.commit()
    return jsonify(message = 'deleted')
