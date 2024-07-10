import shutil
from datetime import datetime
from typing import Optional, TypedDict

from fastapi import UploadFile


class FileResponse(TypedDict):
    message: str
    filename: Optional[str]


def create_file(file: UploadFile) -> FileResponse:
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        file_location = f"uploads/{timestamp}.png"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as error:
        return {
            "message": f"There was an error uploading the file: {error}",
            "filename": None,
        }
    finally:
        file.file.close()
    return {
        "message": f"Successfully uploaded {file.filename}",
        "filename": f"{timestamp}.png",
    }
