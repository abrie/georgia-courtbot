import os

from flask import Flask, send_from_directory


def create_app(test_config=None):
    # create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path="/",
        static_folder="static",
    )
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "db.sqlite3"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_json("secrets.json")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def serve_index():
        if app.static_folder is not None:
            return send_from_directory(app.static_folder, "index.html")

    from . import api

    app.register_blueprint(api.blueprint)

    return app
