from BD import User, Post, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def get_all_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def get_all_posts_with_users():
    posts = session.query(Post).all()
    for post in posts:
        print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}, User: {post.user.username}")

def get_posts_by_user(user_id):
    posts = session.query(Post).filter_by(user_id=user_id).all()
    for post in posts:
        print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")

if __name__ == "__main__":
    get_all_users()
    get_all_posts_with_users()
    get_posts_by_user(1) 