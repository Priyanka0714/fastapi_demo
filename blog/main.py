from fastapi import FastAPI, Depends
from . import schemas, models
from .databse import engine, SessionLocal
from sqlalchemy.orm import Session 

app = FastAPI()

models.Base.metadata.create_all(engine) 



def get_db():
  db = SessionLocal()
  try:
    yield db 
  finally:
    db.close()


#create blog
@app.post('/blog')
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
  new_blog = models.Blog(title=request.title, body=request.body)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog


@app.get('/blog')
def all(db: Session = Depends(get_db)):
  blogs = db.query(models.Blog).all()
  return blogs

@app.get('/blog/{id}')
def show(db: Session = Depends(get_db)):
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()

  return blog

 