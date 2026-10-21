from fastapi import FastAPI, Body,Request
from neiro_client import get_ansver_from_neiro
from contextlib import asynccontextmanager
from db import Base,engine,ChatRequests,get_user_requests,add_requests_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/requests")
def get_my_requests(request: Request):
    user_ip_address = request.client.host
    print(f"{user_ip_address}")
    user_requests = get_user_requests(ip_address=user_ip_address)
    return user_requests

@app.post("/requests")
def send_promt(request:Request,promt:str = Body(embed=True)):
    user_ip_address =  request.client.host
    ansver = get_ansver_from_neiro(promt)
    add_requests_data(
        ip_address=user_ip_address,
        promt=promt,
       response=ansver,
    )
    return {"ansver": ansver}