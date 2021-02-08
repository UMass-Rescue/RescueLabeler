from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
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
    username = Column(String, unique=True)
    full_name = Column(String)
    email = Column(String)
    password = Column(
        PasswordType(schemes=["pbkdf2_sha512", "md5_crypt"], deprecated=["md5_crypt"])
    )
    is_superuser = Column(Boolean(), default=False)


class LabelProject(Base):
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String)
    project_owner = Column(Integer, ForeignKey("labelusers.id"))


class LabelSettings(Base):
    id = Column(Integer, primary_key=True, index=True)
    associated_project = Column(Integer, ForeignKey("labelprojects.id"))
    allow_duplicates = Column(Boolean(), default=False)
    final_label_vote = Column(Boolean(), default=True)
    randomize = Column(Boolean(), default=True)
    authorized_admin = ForeignKey("labelusers.id")


class LabelStringData(Base):
    id = Column(Integer, primary_key=True, index=True)
    target_string = Column(String)
    associated_project = Column(Integer, ForeignKey("labelprojects.id"))


class StringLabels(Base):
    id = Column(Integer, primary_key=True, index=True)
    string_data = Column(Integer, ForeignKey("labelprojects.id"))
    labels = Column(String)
    labeler_id = Column(Integer, ForeignKey("labelusers.id"))
