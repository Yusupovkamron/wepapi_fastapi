from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"Hello word"}


# from fastapi import FastAPI
# from database import session, ENGINE
# from order_router import order_router
# from product_router import product_router
# # from schemas import JWTModel
# from fastapi_jwt_auth import AuthJWT
#
#
# session = session(bind=ENGINE)
# app = FasrAPI
#
#
# # @AuthJWT.load_config
# # def config():
# #     return JWTModel()
#
# app.include_router(order_router)
# app.include_router(product_router)
#
#
# @app.get("/")
# async def landing():
#     return {
#         'message': "this is landing page"
#     }