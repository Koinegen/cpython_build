import uvicorn

from src.gateway import app


def main() -> None:
    """Entrypoint to invoke when this module is invoked on the remote server."""
    # See the official documentations on how "0.0.0.0" makes the service available on
    # the local network - https://www.uvicorn.org/settings/#socket-binding
    uvicorn.run(app, host="0.0.0.0", port=9099)


if __name__ == "__main__":
    main()