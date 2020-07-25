from app import app
from app import db

from posts.blueprint import posts

import view

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    app.run()
