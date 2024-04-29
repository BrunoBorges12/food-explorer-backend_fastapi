from fastapi import APIRouter

router = APIRouter()
print("ok")


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
