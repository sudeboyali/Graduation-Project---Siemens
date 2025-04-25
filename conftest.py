import pytest
import sys
import os
from pythonProject8.plugin.database import init_db

# Proje dizinini path'e ekleme (opsiyonel ama önerilir)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Veritabanını başlangıçta oluşturmak için fixture
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    print("📢 Initializing the database...")
    init_db()

# Test sonuçlarını yakalayan hook
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if call.when == "call":
        setattr(item, "test_outcome", result.outcome)
        setattr(item, "test_exception", str(result.longrepr) if result.failed else None)
