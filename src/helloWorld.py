from flask import Blueprint
from flask_restful import Api, Resource

from src.extensions import ma
from src.extensions.db import db
from sqlalchemy import Column, Integer, String

class HelloWorld(db.Model):
    __tablename__ = "hello_world"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hello = Column(String(10))
    world = Column(String(10))

class HelloWorldSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Integer(
        attribute="id",
        dump_only=True,
        metadata=dict(
            type="integer",
            example="1",
            description="The id of this class",
        ),
    )

    hello = ma.String(
        attribute="hello",
        metadata=dict(
            type="string",
            example="hello",
            description="The hello of this class",
        ),
    )

    world = ma.String(
        attribute="world",
        metadata=dict(
            type="string",
            example="world",
            description="The world of this class",
        ),
    )

    class Meta:
        model = HelloWorld
        extend_existing=True
        sqla_session = db.session
        load_instance = True



class HelloWorldController(Resource):
    def get(self):
        schema = HelloWorldSchema()
        helloWorld = HelloWorld.query.one()
        return schema.dump(helloWorld)


hello_world_blueprint = Blueprint('user', __name__)
hello_world_blueprint_api = Api(hello_world_blueprint)

hello_world_blueprint_api.add_resource(HelloWorldController, '/hello-world')
