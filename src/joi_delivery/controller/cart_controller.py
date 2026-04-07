from fastapi import APIRouter, Depends, Query

from ..dependencies import get_cart_service
from ..domain.cart import Cart
from ..service.cart_service import CartService
from .models import AddProductRequest, CartProductInfo, RemoveProductFromCart, RemoveProductRequest

router = APIRouter(prefix="/cart", tags=["cart"])


@router.post("/product", response_model=CartProductInfo)
def add_product_to_cart(data: AddProductRequest, cart_service: CartService = Depends(get_cart_service)):
    result = cart_service.add_product_to_cart_for_user(data)
    return result

@router.delete('/product', response_model=RemoveProductFromCart)
def delete_product_from_cart(request: RemoveProductRequest, cart_service:CartService = Depends(get_cart_service)):
    try:
        cart = cart_service.remove_product_from_cart(request)
        return cart
    
    except ValueError as e:
        if str(e) == "USER_NOT_FOUND":
            raise HTTPException(status_code=404, detail="User not found")
        elif str(e) == "CART_NOT_FOUND":
            raise HTTPException(status_code=404, detail="Cart not found")
        elif str(e) == "PRODUCT_NOT_FOUND":
            raise HTTPException(status_code=404, detail="Product not found")
        elif str(e) == "PRODUCT_NOT_IN_CART":
            raise HTTPException(status_code=400, detail="Product not in cart")



@router.get("/view", response_model=Cart)
def view_cart(user_id: str = Query(..., description="User ID"), cart_service: CartService = Depends(get_cart_service)):
    cart = cart_service.get_cart_for_user(user_id)
    return cart
