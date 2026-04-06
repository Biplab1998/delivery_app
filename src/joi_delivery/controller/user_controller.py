from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_user_service
from ..service.user_service import UserService
from .models import UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, user_service: UserService = Depends(get_user_service)) -> UserResponse:
    user = user_service.fetch_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f"User not found with id: {user_id}")
    return UserResponse(
        user_id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone_number=user.phone_number,
        username=user.username,
    )
