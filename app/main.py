from fastapi import FastAPI
from app.api.v1.user import user_router
from app.api.v1.group import group_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup action
    print("🚀 Application is running...")
    yield
    # Shutdown action
    print("🛑 Application is stopped...")


app = FastAPI(
    title="DuckDuckChat API",
    version="1.0.0",
    description="The template of messenger",
    lifespan=lifespan,
)

app.include_router(user_router, prefix="/users")
app.include_router(group_router, prefix="/groups")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

