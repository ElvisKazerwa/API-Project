from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import  List, Optional

from .. import models, schemas, oauth2
from ..database import  get_db
from sqlalchemy import func

router = APIRouter(
  prefix="/posts", 
  tags=['Posts']
)

#@router.get("/", response_model=list[schemas.post])
@router.get("/", response_model=list[schemas.Postout])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = " " ):
    print(search)
     #results = db.query(models.post, func.count(models.vote.post_id).label("votes")).join(
      #  models.vote, models.vote.post_id == models.post.id, isouter = True).group_by (model.post.id)   
   
    #cursor.execute(""" SELECT * FROM posts """)
    #posts = cursor.fetchall()
    #posts = db.execute(
    #    'SELECT posts.*, count(votes.post_id)as votes from posts LEFT JOIN votes ON posts.
        # id = votes.pos_id group by posts.id')
        #results = []
        #for post in posts:
             #result.append(dict(post))
        #print(results)
   
    
    Posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
   
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
   
    print(Posts)
    
    return results


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
                  # (post.title, post.content, post.published))
    
    #new_post = cursor.fetchone()
    #conn.commit()
    print(current_user.id)
    new_post= models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

 
#@router.get("/posts/latest")
#def get_latest_post():
    #post= my_posts[len(my_posts)-1]
    #return post 

  
@router.get("/{id}", response_model=schemas.post)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    #cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    #Post = cursor.fetchone()
    Post = db.query(models.Post).filter(models.Post.id == id).first()
    print(Post)
    
    if not Post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the post with id: {id} was not found")
    return Post
 
 
  #delete post
  
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,  db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    #cursor.execute(""" DELETE FROM posts WHERE id = %s returning * """, (str(id),))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    Post_query = db.query(models.Post).filter(models.Post.id == id)
    
    Post = Post_query.first()
    
    if Post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
      
    if Post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized to perform action!")
          
    Post_query.delete (synchronize_session=False) 
    
    db.commit() 
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, #post.published, str(id),))
   # updated_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized to perform action!")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    
    return post_query.first()


