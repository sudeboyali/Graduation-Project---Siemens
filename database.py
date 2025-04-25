from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

# Veritabanı bağlantısı
DATABASE_URL = "sqlite:///test_results.db"
engine = create_engine(DATABASE_URL, echo=True)

# Session yarat
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()  # 🔥 Bu kesinlikle olmalı

# Base sınıfı
Base = declarative_base()

# Veritabanı başlatıcı
def init_db():
    print("📢 Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized")
