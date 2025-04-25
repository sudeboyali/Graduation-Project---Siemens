from .database import session, init_db
from .models import TestCase, TestSuite, Project
import uuid
from datetime import datetime

# ✅ This is required to initialize the database connection
def pytest_configure(config):
    print("\n✅ pytest_configure: Initializing database...")
    init_db()

# ✅ This handles logging of test results
def pytest_runtest_logreport(report):
    if report.when == "call":
        case_id = str(uuid.uuid4())
        suite_id = str(uuid.uuid4())
        full_name = report.nodeid
        status = "passed" if report.passed else "failed"
        start_time = datetime.utcnow()
        end_time = datetime.utcnow()
        duration = (end_time - start_time).seconds
        error_message = None if report.passed else report.longreprtext

        # Example of retry count and criticality
        retry_count = 2
        is_critical = True if "critical" in full_name else False

        # ✅ Create a test case entry
        test_case = TestCase(
            case_id=case_id,
            suite_id=suite_id,
            full_name=full_name,
            status=status,
            start_time=start_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
            end_time=end_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
            duration=duration,
            error_message=error_message,
            is_critical=is_critical,
            retry_count=retry_count
        )

        # ✅ Add to session and commit
        session.add(test_case)
        session.commit()
        print(f"\n✅ Test logged: {full_name}, Status: {status}")

# ✅ This is required to close the session after testing
def pytest_sessionfinish(session, exitstatus):
    session.close()
    print("\n✅ pytest_sessionfinish: DB bağlantısı kapatıldı.")
