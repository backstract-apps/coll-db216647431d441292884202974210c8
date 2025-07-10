from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/profile/')
async def get_profile(db: Session = Depends(get_db)):
    try:
        return await service.get_profile(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profile/id')
async def get_profile_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_profile_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/profile/id/')
async def put_profile_id(id: int, name: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], mobile: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_profile_id(db, id, name, address, mobile, password, email)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/profile/id')
async def delete_profile_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_profile_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/records/')
async def get_records(db: Session = Depends(get_db)):
    try:
        return await service.get_records(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/records/id')
async def get_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_records_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/records/id/')
async def put_records_id(id: int, username: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], pincode: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_records_id(db, id, username, address, pincode)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/records/id')
async def delete_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_records_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/class/')
async def get_class(db: Session = Depends(get_db)):
    try:
        return await service.get_class(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/class/id')
async def get_class_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_class_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/class/')
async def post_class(id: int, subject: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_class(db, id, subject)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/class/id/')
async def put_class_id(id: int, subject: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_class_id(db, id, subject)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/class/id')
async def delete_class_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_class_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/id')
async def get_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(id: int, name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, id, name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/id/')
async def put_students_id(id: int, name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_students_id(db, id, name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/id')
async def delete_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/records/')
async def post_records(id: int, username: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], pincode: Annotated[str, Query(max_length=100)], user_amount: int, db: Session = Depends(get_db)):
    try:
        return await service.post_records(db, id, username, address, pincode, user_amount)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/profile/')
async def post_profile(id: int, name: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], mobile: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], amount: int, db: Session = Depends(get_db)):
    try:
        return await service.post_profile(db, id, name, address, mobile, password, email, amount)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

