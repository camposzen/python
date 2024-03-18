from flask import Flask, render_template, request
import requests
from post import Post
import smtplib

app = Flask(__name__)

blog_posts = []


@app.route('/')
def home():
    global blog_posts
    blog_posts = []
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
            return render_template("post.html", title=p.title, body=p.text)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    print(request.method)
    print(request.form)
    if request.method == 'GET':
        return render_template("contact.html", contact_message="Contact me")
    else:
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", contact_message="Message successfully sent")


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("202.droidzen@gmail.com", "uliffeqsxrtegsii")
        connection.sendmail("202.droidzen@gmail.com", "202.droidzen@gmail.com", email_message)


if __name__ == "__main__":
    app.run(debug=True)
