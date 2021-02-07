from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy_utils.types.password import PasswordType
from app.db.base_class import Base


class LabelUser(Base):
    """Primary api user

    :attr int id: row id, unique
    :attr str username: first name of user
    :attr str full_name: last name of user
    :attr str email: user email
    :attr password password: hashed user password
    :attr bool is_superuser: boolean denoting superuser, false by default

    """

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    full_name = Column(String)
    email = Column(String)
    password = Column(
        PasswordType(schemes=["pbkdf2_sha512", "md5_crypt"], deprecated=["md5_crypt"])
    )
    is_superuser = Column(Boolean(), default=False)
