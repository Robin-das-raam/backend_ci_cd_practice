from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Backend CI/CD Practice Running"}