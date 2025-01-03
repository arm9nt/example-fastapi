from fastapi import FastAPI

app = FastAPI()

@app.get("/posts")
def get_posts():
    return{"Just type this message:"}