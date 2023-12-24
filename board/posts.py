from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from board.database import get_db

bp = Blueprint("posts", __name__)

@bp.route("/posts")
def posts():
    db = get_db()
    posts = db.execute(
        "SELECT * FROM post ORDER BY created DESC"
    ).fetchall()
    return render_template("posts/posts.html", posts=posts)

@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anyonymous"
        message = request.form["message"]
        
        if message:
            db = get_db()
            db.execute(
                "INSERT INTO post (author, message) VALUES (?, ?)",
                (author, message)
            )
            db.commit()
            return redirect(url_for("posts.posts"))
        
    return render_template("posts/create.html")