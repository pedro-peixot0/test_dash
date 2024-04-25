from app import app
from app.main_dash import create_dash_application

create_dash_application(app)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
 