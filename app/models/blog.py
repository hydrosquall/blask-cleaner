from app import db

class BlogPost(db.Document):
    author = db.StringField(required=True, max_length=100)
    title = db.StringField(required=True, max_length=100)
    body = db.StringField(required=True)

BlogPostForm = model_form(BlogPost)
