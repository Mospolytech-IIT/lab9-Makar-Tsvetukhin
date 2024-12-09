from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from crud import (
    create_users,
    create_posts,
    read_all_users,
    read_all_posts_with_users,
    read_posts_by_user,
    update_user,
    update_post,
    delete_single_post,
    delete_user_and_related_posts
)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <p><a href="/users/">Create Users</a></p>
    <p><a href="/posts/">Create Posts</a></p>
    <p><a href="/users">Read All Users</a></p>
    <p><a href="/posts">Read All Posts</a></p>
    <p><a href="/posts/user/{user_id}">Read Posts by User</a></p>
    <p><a href="/users/{user_id}">Update User</a></p>
    <p><a href="/posts/{post_id}">Update Post</a></p>
    <p><a href="/posts/{post_id}">Delete Post</a></p>
    <p><a href="/users/{user_id}">Delete User</a></p>
    """

#создание данных
@app.post("/users/")
async def api_create_users():
    return create_users()

@app.post("/posts/")
async def api_create_posts():
    return create_posts()

#чтение данных
@app.get("/users/")
async def api_read_all_users():
    return read_all_users()

@app.get("/posts/")
async def api_read_all_posts_with_users():
    return read_all_posts_with_users()

@app.get("/posts/user/{user_id}")
async def api_read_posts_by_user(user_id: int):
    return read_posts_by_user(user_id)

#обновление данных
@app.put("/users/{user_id}")
async def api_update_user(user_id: int, new_email: str):
    result = update_user(user_id, new_email)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@app.put("/posts/{post_id}")
async def api_update_post(post_id: int, new_content: str):
    result = update_post(post_id, new_content)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

#удаление данных
@app.delete("/posts/{post_id}")
async def api_delete_post(post_id: int):
    result = delete_single_post(post_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@app.delete("/users/{user_id}")
async def api_delete_user(user_id: int):
    result = delete_user_and_related_posts(user_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result