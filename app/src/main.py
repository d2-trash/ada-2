import urllib
from base64 import b64encode
from uuid import uuid4

import redis
import requests
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse

with open("secrets/api_key.secret", "r") as f:
    API_KEY = f.read().rstrip("\n")
with open("secrets/client_id.secret", "r") as f:
    CLIENT_ID = f.read().rstrip("\n")
with open("secrets/client_secret.secret", "r") as f:
    CLIENT_SECRET = f.read().rstrip("\n")

AUTH_URL = "https://www.bungie.net/en/oauth/authorize"

app = Starlette()


r = redis.Redis(host="db", port=6379, db=0)


def generate_oauth_url_with_tokens():
    # TODO: In the future we should include a JWT CSRF token
    return AUTH_URL


@app.route("/")
async def index(request):
    return JSONResponse({"mes": "Hello world!"})


@app.route("/register")
async def register(request):
    user = request.query_params.get("u")
    if user is None:
        return "Invalid registration link."
    else:
        if r.get(user) is not None:
            print("User already registered")
            # Todo handle this
    state = str(uuid4())
    # session["state"] = state
    # session["user"] = user
    return JSONResponse(
        AUTH_URL
        + "?"
        + urllib.parse.urlencode(
            {"state": state, "client_id": CLIENT_ID, "response_type": "code"}
        )
    )


@app.route("/callback/bungie", methods=["GET", "POST"])
async def bungie_redirect(request):
    # TODO: In the future we should check the included JWT CSRF token
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
    return JSONResponse(r.json())


# if __name__ == "__main__":
#     uvicorn.run(app, host='0.0.0.0', port=80)
