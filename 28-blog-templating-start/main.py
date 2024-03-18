from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_posts = []


@app.route('/')
def home():
    global blog_posts
    result = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    json = result.json()
    for b in json:
        post = Post(b["id"], b["title"], b["subtitle"], b["body"])
        blog_posts.append(post)
    return render_template("index.html", posts=blog_posts)


@app.route('/blog/<int:post_id>')
def blog(post_id):
    for p in blog_posts:
        if p.id == post_id:
            return render_template("post.html", title=p.title, intro=p.intro, body=p.text)



if __name__ == "__main__":
    app.run(debug=True)
