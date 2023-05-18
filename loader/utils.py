from exception import PictureWrongTypeError


def upload_photo(picture):
    """Загружает фото"""
    filename = picture.filename
    file_type = filename.split(".")[-1].lower()
    if file_type not in ["jpg", "jpeg", "png", "svg"]:
        raise PictureWrongTypeError

    picture.save(f"./uploads/images/{filename}")

    return f"./uploads/images/{filename}"
