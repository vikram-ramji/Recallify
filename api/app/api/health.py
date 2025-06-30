from fastapi import APIRouter

router = APIRouter(prefix="/health")

@router.get("/")
def check():
    return {"status": "OK"}