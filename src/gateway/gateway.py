"""Entrypoint to invoke the FastAPI application service with."""

from fastapi import FastAPI, status
from pydantic import BaseModel

from src.logic import super_secret_function, error_function

app = FastAPI()


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"


class RandomResponse(BaseModel):
    status: str = "OK"
    result: float


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="OK")


@app.get(
    "/random",
    tags=["random"],
    summary="Random value",
    response_description="Return random value",
    status_code=status.HTTP_200_OK,
    response_model=RandomResponse
)
async def random() -> RandomResponse:
    result = await super_secret_function()
    return RandomResponse(result=result)


@app.get(
    "/error_test",
    tags=["error_test"],
    summary="Test raise error"
)
def error_test():
    error_function()
