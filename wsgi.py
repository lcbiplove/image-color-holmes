from app import create_app
from waitress import serve

main_app = create_app()
if __name__ == "__main__":
    serve(main_app, host='0.0.0.0', port=8000, url_scheme='https')