from fastapi import APIRouter
from models import Product, Category
from schemas import ProductModel, CategoryModel
from database import session, ENGINE
from fastapi.encoders import jsonable_encoder

product_router = APIRouter(prefix='/product')
session = session(bind=ENGINE)

@product_router.get('/')
async def product_list():
    products = session.query(Product).all()
    category = session.query(Category).filter()
    context = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "category_id": product.category_id
        }
        for product in products
    ]
    return jsonable_encoder(context)


