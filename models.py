import sqlalchemy.ext.declarative

import sqlalchemy
import sqlalchemy.orm


Base = sqlalchemy.ext.declarative.declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))


class Squad(Base):
    __tablename__ = 'squad'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))


class SquadMember(Base):
    __tablename__ = 'squad_member'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('user.id'))
    user = sqlalchemy.orm.relationship('User')
    squad_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('squad.id'))
    squad = sqlalchemy.orm.relationship('Squad')
    joined = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True))
    parted = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True))
