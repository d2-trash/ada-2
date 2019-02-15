import urllib
from base64 import b64encode
from uuid import uuid4

import jwt
import requests
import uvicorn
from redis import Redis
from starlette.applications import Starlette
from starlette.responses import JSONResponse

with open("secrets/api_key.secret", "r") as f:
    API_KEY = f.read().rstrip("\n")
with open("secrets/client_id.secret", "r") as f:
    CLIENT_ID = f.read().rstrip("\n")
with open("secrets/client_secret.secret", "r") as f:
    CLIENT_SECRET = f.read().rstrip("\n")
with open("secrets/jwt.secret", "r") as f:
    JWT_SECRET = f.read().rstrip("\n")

AUTH_URL = "https://www.bungie.net/en/oauth/authorize"

app = Starlette()


r = Redis(host="db", port=6379, db=0)


@app.route("/")
async def index(request):
    return JSONResponse({"mes": "Hello world!"})


@app.route("/callback/bungie", methods=["GET", "POST"])
async def bungie_redirect(request):
    state = request.query_params.get("state")
    if state is None:
        return JSONResponse("No state found")

    token = jwt.decode(state, JWT_SECRET, algorithms=["HS256"])

    authorization_code = request.query_params.get("code")

    r = requests.post(
        "https://www.bungie.net/platform/app/oauth/token/",
        data={"grant_type": "authorization_code", "code": authorization_code},
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic "
            + b64encode(bytes(":".join([CLIENT_ID, CLIENT_SECRET]), "utf-8")).decode(
                "utf-8"
            ),
        },
    )  # TODO: This should be abstracted over

    # r.set()
    return JSONResponse({token.get("user"): r.json()})
