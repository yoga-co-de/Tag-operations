from database import Base
from sqlalchemy import Column,Integer,String,Text,Boolean,SMALLINT,ForeignKey,VARCHAR #,func fot timestamp,
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship





class Studio(Base):
    __tablename__="studio"
    studio_id=Column(Integer,primary_key=True,nullable=False)
    studio_name=Column(String,nullable=False)
    
    users = relationship("User", back_populates="studio")
    shots = relationship("Shot", back_populates="studio")
    tags = relationship("Tag", back_populates="studio")

class User(Base):
    __tablename__="user"
    user_id=Column(Integer,primary_key=True)
    studio_id=Column(Integer,ForeignKey("studio.studio_id"),nullable=False)
    first_name=Column(String,nullable=True)
    last_name=Column(String,nullable=False)
    email=Column(String,nullable=True)
    password=Column(String,nullable=True)
    is_active=Column(SMALLINT,nullable=True,server_default=text("1"))
    is_delete=Column(SMALLINT,nullable=True,server_default=text("1"))
    studio = relationship("Studio", back_populates="users")
    tags_updated = relationship("Tag", back_populates="updated_user")



class Shot(Base):
    __tablename__="shot"
    shot_id =Column(Integer,primary_key=True,nullable=False)
    Studio_id =Column(Integer,ForeignKey("studio.studio_id"),nullable=False)   
    tag_id=Column(Integer,nullable=False)
    shot_code=Column(Integer,nullable=False)
    shot_path=Column(VARCHAR(250),nullable=False)
    frame_range=Column(Integer,nullable=False)
    is_deleted=Column(SMALLINT, server_default=text("0"))
    created_by=Column(Integer,nullable=False)
    created_date =Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    updated_by=Column(Integer,nullable=False)
    updated_date =Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    last_updated_date=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    studio = relationship("Studio", back_populates="shots")
    tags = relationship("Tag", back_populates="shot")


class Tag(Base):
    __tablename__="tag"

    tag_id= Column(Integer,primary_key=True,nullable=False)
    studio_id=Column(Integer,ForeignKey("studio.studio_id"),nullable=False)
    shot_id=Column(Integer,ForeignKey("shot.shot_id"),nullable=False)
    tag_name=Column(String,nullable=False)
    description=Column(Text,nullable=False)
    is_deleted = Column(Boolean, server_default=text('false'))
   # is_deleted=Column(Boolean, server_default=False)
    created_date =Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    # created_by= Column(Integer,nullable=False,default=0)
    updated_date =Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    updated_by = Column(Integer, ForeignKey("user.user_id"),nullable=False)
    studio = relationship("Studio", back_populates="tags")
    shot = relationship("Shot", back_populates="tags")
    updated_user = relationship("User", back_populates="tags_updated")