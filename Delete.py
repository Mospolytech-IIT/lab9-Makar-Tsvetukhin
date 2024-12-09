from BD import User, Post, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def delete_post(post_id):
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        session.delete(post)
        session.commit()
        print(f"Post ID {post_id} deleted")

def delete_user_and_posts(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        posts = session.query(Post).filter_by(user_id=user_id).all()
        for post in posts:
            session.delete(post)
        
        session.delete(user)
        session.commit()
        print(f"User {user.username} and posts deleted")

if __name__ == "__main__":
    delete_post(2) 
    delete_user_and_posts(3) 