import re
import os

from bottle import route, run
from rich.console import Console


@route("/")
def response():
    s = os.getenv("SECRET")
    c = " ".join(re.sub( r"([A-Z])", r" \1", s[::-1]).split())

    console = Console()
    with console.capture() as capture:
        console.print(f":tada: {c} :tada:")
    r = capture.get()
    return r


if __name__ == "__main__":    
    run(host='0.0.0.0', port=8080, debug=True)
