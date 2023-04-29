from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker,declarative_base

Base = declarative_base()

class sample(Base):
    __tablename__ = "samples"
    id = Column(Integer, primary_key=True)
    user_name = Column("username", String)
    sample_name = Column("sample_name", String)
    substrate = Column("substrate", String)
    element = Column("element", String)

    def __init__(self,  id, sample_name, user_name = "None", element = "None", substrate = "None"):
        self.id = id
        self.user_name = user_name
        self.sample_name = sample_name
        self.element = element
        self.substrate = substrate
        # self.pictures = picture()
        # self.pictures.type = "REM"

class picture:
    def __init__(self):
        self.path = None
        self.type = None
        self.magnification = None
        self.comments = None
        self.date = None
        self.tags = []
        self.values = []

class xrddata:
    def __init__(self):
        self.xrd_file_path = None
        self.peaks = None
        self.scratched_edge = None

class deposition_process:
        def __init__(self):
            self.batch_pyrolysis = None
            self.batch_crystallization = None
            self.batch_annealing = None
            self.data_pyrolysis = None
            self.data_crystallization = None
            self.data_annealing = None
            self.date_pyrolysis = None
            self.date_crystallization = None
            self.date_annealing = None

class jc_cryoscan:
        def __init__(self):
            self.file_path = None
            self.points = []

class tc_ppms:
        def __init__(self):
            self.file_path = None
            self.tc50 = None
            self.tc10 = None
            self.tc90 = None

engine = create_engine("sqlite:///mydb.db", echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
y1 = sample(1, "Y1a1")

session.add(y1)
session.commit()
