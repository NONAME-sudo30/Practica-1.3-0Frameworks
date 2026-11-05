from fastapi import APIRouter
router = APIRouter(
    prefix = "/task",
    tags = ["task"]
)

@router.get("/get_task")
async def get_task():
    pass
@router.post("/create_task")
async def create_task():
    pass
    