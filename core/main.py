from fastapi import FastAPI

from common.responses import Response

app = FastAPI(default_response_class=Response)


@app.get("/health")
def health_check():
    return {"message": "ok"}
