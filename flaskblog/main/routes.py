from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/buddhism")
def buddhism():
    return render_template('buddhism.html', title='Buddhism')

@main.route("/NewPlace")
def NewPlace():
    return render_template('NewPlace.html', title='NewPlace')

@main.route("/Problems")
def Problems():
    return render_template('Problems.html', title='Problems')

@main.route("/GeospatialProgramming")
def GeospatialProgramming():
    return render_template('GeospatialProgramming.html', title='GeospatialProgramming')

@main.route("/Unsatisfactoriness")
def Unsatisfactoriness():
    return render_template('Unsatisfactoriness.html', title='Unsatisfactoriness')

@main.route("/HighRiskBehaviors")
def HighRiskBehaviors():
    return render_template('HighRiskBehaviors.html', title='HighRiskBehaviors')