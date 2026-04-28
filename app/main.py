
from fastapi import FastAPI
from app.router import tag_router,studio_router,user_router,shot_router


app = FastAPI()



app.include_router(studio_router.api)
app.include_router(user_router.api)
app.include_router(shot_router.api)
app.include_router(tag_router.api)



