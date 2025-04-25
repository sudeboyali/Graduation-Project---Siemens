from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from .database import Base


class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(String, primary_key=True)
    name = Column(String, unique=True)

class TestSuite(Base):
    __tablename__ = 'testsuites'
    suite_id = Column(String, primary_key=True)
    project_id = Column(String, ForeignKey('projects.project_id'))
    name = Column(String)
    created_at = Column(DateTime)
    last_updated = Column(DateTime)

class TestCase(Base):
    __tablename__ = 'testcases'
    case_id = Column(String, primary_key=True)
    suite_id = Column(String, ForeignKey('testsuites.suite_id'))
    full_name = Column(String)
    step_name = Column(String)
    status = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    duration = Column(Integer)
    error_message = Column(String)

    # ✅ Yeni Alanlar
    is_critical = Column(Boolean)            # Testin kritik olup olmadığı
    retry_count = Column(Integer)            # Test kaç kere denendi
    priority = Column(Integer)               # Testin öncelik sırası
    tags = Column(String)                    # Testle ilgili etiketler
    test_type = Column(String)               # Test türü (ör. functional, regression)
    owner = Column(String)                   # Test sorumlusu
    environment = Column(String)             # Test ortamı (ör. staging, production)
