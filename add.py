from BD import User, Post, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def add_users():
    users = [
        User(username="Makar", email="tsvetukhin@list.ru", password="123"),
        User(username="Makar2", email="2tsvetukhin@list.ru", password="321"),
        User(username="Makar3", email="3tsvetukhin@list.ru", password="213"),
    ]
    session.add_all(users)
    session.commit()
    print("Пользователи добавлены")

def add_posts():
    posts = [
        Post(title="First Post", content="First_content", user_id=1),
        Post(title="Second Post", content="Second_content", user_id=2),
        Post(title="Third Post", content="Third_content", user_id=3),
    ]
    session.add_all(posts)
    session.commit()
    print("Посты добавлены")

if __name__ == "__main__":
    add_users()
    add_posts()