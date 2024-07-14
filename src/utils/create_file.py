import shutil
from datetime import datetime
from typing import IO, Optional, TypedDict

import filetype
from fastapi import HTTPException, UploadFile, status


class FileResponse(TypedDict):
    message: str
    filename: Optional[str]


def create_file(file: UploadFile) -> FileResponse:
    validate_file_size_type(
        file
    )  # função que valida o file caso não esteja de acordo cai no execption dele

    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_location = f"uploads/{timestamp}.png"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as error:
        return {
            "message": f"Ocorreu um erro ao carregar o arquivo: {error}",
            "filename": None,
        }
    finally:
        file.file.close()
    return {
        "message": f"Successfully uploaded {file.filename}",
        "filename": f"{timestamp}.png",
    }


def validate_file_size_type(file: IO):
    FILE_SIZE = 2097152  # 2MB

    accepted_file_types = [
        "image/png",
        "image/jpeg",
        "image/jpg",
        "png",
        "jpeg",
        "jpg",
    ]
    file_info = filetype.guess(file.file)
    if file_info is None:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Não é possível determinar o tipo de arquivo",
        )

    detected_content_type = file_info.extension.lower()
    print(detected_content_type)
    if (
        file.content_type not in accepted_file_types
        or detected_content_type not in accepted_file_types
    ):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Tipo de arquivo não suportado",
        )

    real_file_size = 0
    for chunk in file.file:
        real_file_size += len(chunk)
        if real_file_size > FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail="Muito grande",
            )
