from BD import User, Post, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def update_user_email(user_id, new_email):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.email = new_email
        session.commit()
        print(f"Email update {user.username} on {new_email}")

def update_post_content(post_id, new_content):
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        post.content = new_content
        session.commit()
        print(f"Post content '{post.title}' updated")

if __name__ == "__main__":
    update_user_email(1, "newMail@mail.ru")
    update_post_content(1, "Updated content for the first post")