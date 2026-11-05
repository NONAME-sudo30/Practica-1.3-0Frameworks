from fastapi import APIRouter
router = APIRouter(
    prefix = "/proyect",
    tags = ["proyect"]

)
@router.get("/get_proyect")
async def get_proyect():
    pass
@router.post("/create_proyect")
async def create_proyect():
    pass