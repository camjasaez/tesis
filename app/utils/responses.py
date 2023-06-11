from fastapi import HTTPException
from fastapi.responses import JSONResponse


def success_response(
    status: int = 200, message: str = "Success", data: dict = None
) -> JSONResponse:
    return JSONResponse(status_code=status, content={"message": message, "data": data})


def error_response(
    status: int = 400, message: str = "Something went wrong"
) -> HTTPException:
    raise HTTPException(status_code=status, detail=message)
