#!/usr/bin/env python3
import os

import connexion

from swagger_server import encoder, db


def main():
    connexion_app = connexion.App(__name__, specification_dir='./swagger/')
    connexion_app.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    connexion_app.app.json_encoder = encoder.JSONEncoder
    connexion_app.add_api('swagger.yaml', arguments={'title': 'Testing API'}, pythonic_params=True)
    db.init_app(connexion_app.app)
    connexion_app.run(port=8080)


if __name__ == '__main__':
    main()
