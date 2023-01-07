from fastapi import FastAPI
import config as cfg
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"server_name": cfg.SERVER_NAME}


@app.get("/search")
async def search():
    pass


if __name__ == "__main__":
    uvicorn.run("api:app", port=3232, host="0.0.0.0", reload=True) # run async web server