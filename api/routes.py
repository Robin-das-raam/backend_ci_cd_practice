import os
from fastapi import APIRouter
# import shutil
# import uuid
# from pydantic import BaseModel
# from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse


router = APIRouter()

# UPLOAD_DIR = "/home/robinpc/Desktop/Fastapi_prac/backend_ci_cd_prac/uploads"
# OUTPUT_DIR = "/home/robinpc/Desktop/Fastapi_prac/backend_ci_cd_prac/output"

# os.makedirs(UPLOAD_DIR, exist_ok = True)
# os.makedirs(OUTPUT_DIR, exist_ok = True)

@router.get("/")
def root():
    return {"message": "Backend CI/CD Practice Running . Moving ahead"}


@router.get("/hello",response_class=HTMLResponse)
def say_hello():
    return "<h1>Hello from CI/CD FastaPI aPP! now work  </h1>"