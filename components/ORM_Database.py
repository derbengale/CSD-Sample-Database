from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, declarative_base
try:
    from components.helpers import *
except:
    from helpers import *

import re
Base = declarative_base()



class Picture_DB(Base):
    __tablename__ = 'pictures'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    type = Column(String)
    magnification = Column(String)
    comments = Column(String)
    date = Column(String)
    sample_id = Column(Integer, ForeignKey('samples.id'))


class XRD_DB(Base):
    __tablename__ = 'xrddata'

    id = Column(Integer, primary_key=True)
    xrd_file_path = Column(String)
    peaks = Column(String)
    scratched_edge = Column(String)
    lattice_parameter = Column(Float)
    sample_id = Column(Integer, ForeignKey('samples.id'))


class CSD_DB(Base):
    __tablename__ = 'deposition_process'

    id = Column(Integer, primary_key=True)
    batch_pyrolysis = Column(String)
    batch_crystallization = Column(String)
    batch_annealing = Column(String)
    data_pyrolysis = Column(String)
    data_crystallization = Column(String)
    data_annealing = Column(String)
    date_pyrolysis = Column(String)
    date_crystallization = Column(String)
    date_annealing = Column(String)
    sample_id = Column(Integer, ForeignKey('samples.id'))

class TC_DB(Base):
    __tablename__ = 'tc_ppms'

    id = Column(Integer, primary_key=True)
    file_path = Column(String)
    tc50 = Column(String)
    tc10 = Column(String)
    tc90 = Column(String)
    sample_id = Column(Integer, ForeignKey('samples.id'))

class Jc_DB(Base):
    __tablename__ = 'jccryoscan'

    id = Column(Integer, primary_key=True)
    file_path = Column(String)
    points = Column(Integer)
    total_superconducting_points = Column(Integer)
    thickness = Column(Float)
    coil_factor = Column(Float)
    sample_id = Column(Integer, ForeignKey('samples.id'))

class CryoscanPoints_DB(Base):
    __tablename__ = 'jccryoscan_points'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    position = Column(Float)
    position_relative = Column(Float)
    superconducting = Column(Boolean)
    jc = Column(Float)
    n_factor = Column(Float)
    r_squared = Column(Float)
    currents = Column(String)
    voltages = Column(String)
    sample_id = Column(Integer, ForeignKey('samples.id'))

class Sample_DB(Base):
    __tablename__ = 'samples'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    sample_name = Column(String)
    series = Column(String)
    element = Column(String)
    substrate = Column(String)

    pictures = relationship("Picture_DB", backref="sample")
    xrd = relationship("XRD_DB", backref="sample")
    csd = relationship("CSD_DB", backref="sample")
    jcsf = relationship("Jc_DB", backref="sample")
    jcsf_points = relationship("CryoscanPoints_DB", backref="sample")
    tc = relationship("TC_DB", backref="sample")


def create_sample(session, user_name, sample_name, element='None', substrate='None', series='None'):
    # Create a new Sample instance
    sample = Sample_DB(id=None,user_name=user_name, sample_name=sample_name, element=element, substrate=substrate, series=series)

    # Add the sample to the session
    session.add(sample)

    # Commit the changes to the database
    session.commit()

    return sample


def add_tc_ppms(session, sample, file_path=None, tc50=None, tc10=None, tc90=None):
    sample.tc.append(TC_DB(file_path=file_path, tc50=tc50, tc10=tc10, tc90=tc90))
    session.commit()
    return sample

def add_picture(session, sample, path=None, type=None, magnification=None, comments=None, date=None):
    sample.pictures.append(Picture_DB(path=path, type=type, magnification=magnification, comments=comments, date=date))
    session.commit()
    return sample


def add_xrd_data(session, sample, xrd_file_path=None, peaks=None, scratched_edge=None):
    sample.xrd.append(XRD_DB(xrd_file_path=xrd_file_path, peaks=peaks, scratched_edge=scratched_edge))
    session.commit()
    return sample


def add_deposition_process(session, sample, batch_pyrolysis=None, batch_crystallization=None, batch_annealing=None, data_pyrolysis=None, data_crystallization=None, data_annealing=None, date_pyrolysis=None, date_crystallization=None, date_annealing=None):
    sample.csd.append(CSD_DB(batch_pyrolysis=batch_pyrolysis, batch_crystallization=batch_crystallization, batch_annealing=batch_annealing, data_pyrolysis=data_pyrolysis, data_crystallization=data_crystallization, data_annealing=data_annealing, date_pyrolysis=date_pyrolysis, date_crystallization=date_crystallization, date_annealing=date_annealing))
    session.commit()
    return sample


def add_cryoscan(session, sample, file_path=None, points=None, total_superconducting_points=None, thickness=None, coil_factor=None):
    sample.jcsf.append(Jc_DB(file_path=file_path, points=points, total_superconducting_points=total_superconducting_points, thickness=thickness, coil_factor=coil_factor))
    session.commit()
    return sample


def add_cryoscan_point(session, sample, number=None, position=None, position_relative=None, superconducting=None, jc=None, n_factor=None, r_squared=None, currents=None, voltages=None):
    sample.jcsf_points.append(CryoscanPoints_DB(number=number, position=position, position_relative=position_relative, superconducting=superconducting, jc=jc, n_factor=n_factor, r_squared=r_squared, currents=currents, voltages=voltages))
    session.commit()
    return sample

def scan_folder_add_samples(session, folder_path, strings_to_remove, extension=".jpg", username = None):
    user = input("Username? ") if username != "Yassin" else "Yassin"

    file_names = os.listdir(folder_path)
    valid_files = [f for f in file_names if f.endswith(extension)]
    updated_names = []
    for file in valid_files:
        updated_name = os.path.splitext(os.path.basename(file))[0]
        for string in strings_to_remove:
            updated_name = updated_name.replace(string, "")
        updated_names.append(updated_name)
    
    print("Updated sample names:")
    print(updated_names)
    
    answer = input("Do you want to accept these names? (y/n) ") if username != "Yassin" else "y"
    if answer == "y":
        for sample_name in updated_names:
            element_ = None
            substrate_ = None
            if user == "Yassin":
                element_ = re.sub(r'\d.*', '', sample_name)
                substrate_="1x1cm LAO"
                series_="Solution Tests"
            create_sample(session, user, sample_name, element=element_, substrate=substrate_, series = series_)
                
            print(f"{element_}-{substrate_}-Sample {sample_name} has been added to the Database.")
    else:
        print("Sample have not been added.")
        

def scan_folder_add_overviews(session : sessionmaker, folder_path, extension=".jpg"):

    samples = session.query(Sample_DB).all()
    sample_names = [sample.sample_name for sample in samples]
    file_names = os.listdir(folder_path)
    valid_files = [f for f in file_names if f.endswith(extension)]
    
    for filename in valid_files:
        for index, samplename in enumerate(sample_names):
            if samplename in filename:
                

                add_picture(session, samples[index], os.path.join(folder_path, filename),"Overview", 20, "","")
                print(f"[Overview] Added {filename} to {samplename}")

def scan_folder_add_xrd(session : sessionmaker, folder_path, extension=".xy"):

    samples = session.query(Sample_DB).all()
    sample_names = [sample.sample_name for sample in samples]
    file_names = os.listdir(folder_path)
    valid_files = [f for f in file_names if f.endswith(extension)]
    
    for filename in valid_files:
        for index, samplename in enumerate(sample_names):
            if samplename in filename:
                add_xrd_data(session, samples[index], os.path.join(folder_path, filename))
                print(f"[XRD] Added {filename} to {samplename}")

def scan_folder_add_cryoscan(session : sessionmaker, folder_path, extension=".csw"):

    samples = session.query(Sample_DB).all()
    sample_names = [sample.sample_name for sample in samples]
    file_names = os.listdir(folder_path)
    valid_files = [f for f in file_names if f.endswith(extension)]
    
    for filename in valid_files:
        for index, samplename in enumerate(sample_names):
            if samplename in filename:
                add_cryoscan(session, samples[index], os.path.join(folder_path, filename))
                print(f"[Cryoscan] Added {filename} to {samplename}")

def scan_folder_add_tc_ppms(session : sessionmaker, folder_path, extension=".csw"):

    samples = session.query(Sample_DB).all()
    sample_names = [sample.sample_name for sample in samples]
    file_names = os.listdir(folder_path)
    valid_files = [f for f in file_names if f.endswith(extension)]
    
    for filename in valid_files:
        for index, samplename in enumerate(sample_names):
            if samplename in filename:
                add_tc_ppms(session, samples[index], os.path.join(folder_path, filename))
                print(f"[Tc PPMS] Added {filename} to {samplename}")

 
     
if __name__ == "__main__":
    import os
    os.system('taskkill -f -im "DB Browser for SQLite.exe"')
    # basepath = r"C:/Users/yassi/OneDrive/Dokumente/GitHub/Masterarbeit/"
    basepath = r"Y:/Masterarbeit/"
    basepath = r"C:/Users/yassi/OneDrive/Dokumente/GitHub/Masterarbeit"
    dbpath = basepath + r"/Skripte/SampleViewer/components/samples.db"
    
    ov_images_path = basepath + r"/Dokumente/Messdaten/Keyencejpg"
    # dbpath = r"C:/Users/yassi/OneDrive/Dokumente/GitHub/Masterarbeit/Skripte/Sample Viewer/components/samples.db"
    
    os.remove(dbpath)
    engine = create_engine(f'sqlite:///{dbpath}')
    
    #All classes were assigned to base class
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    #Add Samples
    scan_folder_add_samples(session, folder_path=basepath + r"/Dokumente/Messdaten/Keyencejpg", strings_to_remove=["YR", "_overview"], extension=".jpg", username="Yassin")
    samples = session.query(Sample_DB).all()
    sample_namess = [sample.sample_name for sample in samples]
    #Add Data
    scan_folder_add_overviews(session, folder_path=basepath + r"/Dokumente/Messdaten/Keyencejpg", extension=".jpg")
    scan_folder_add_xrd(session, basepath + r"/Dokumente/Messdaten/XRD", extension=".dat")
    scan_folder_add_cryoscan(session, basepath + r"/Dokumente/Messdaten/Jc_self", extension=".csw" )
    scan_folder_add_tc_ppms(session, basepath + r"/Dokumente/Messdaten/Tc_ind", extension=".txt" )

    openfile(dbpath)