from add import add_users, add_posts
from Extraction import get_all_users, get_all_posts_with_users, get_posts_by_user
from Update import update_user_email, update_post_content
from Delete import delete_post, delete_user_and_posts

def create_users():
    users = add_users()
    return users  

def create_posts():
    posts = add_posts()
    return posts  


def read_all_users():
    return get_all_users()  

def read_all_posts_with_users():
    return get_all_posts_with_users()  

def read_posts_by_user(user_id):
    return get_posts_by_user(user_id)  


def update_user(user_id, new_email):
    return update_user_email(user_id, new_email)  

def update_post(post_id, new_content):
    return update_post_content(post_id, new_content)  


def delete_single_post(post_id):
    return delete_post(post_id)  
def delete_user_and_related_posts(user_id):
    return delete_user_and_posts(user_id)  