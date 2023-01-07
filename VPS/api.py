from fastapi import FastAPI
import config as cfg
import uvicorn
import proxy


app = FastAPI()

@app.get("/")
async def root():
    return {"server_name": cfg.SERVER_NAME}


@app.get("/search")
async def search(query: str):
    html = proxy.make_req_requests(query, "EN", res_number=40) 
    return {"status": 1, "data": html}


if __name__ == "__main__":
    uvicorn.run("api:app", port=7777, host="0.0.0.0", reload=True) # run async web server