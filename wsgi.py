from app import create_app
from waitress import serve

main_app = create_app()
if __name__ == "__main__":
    main_app.run()