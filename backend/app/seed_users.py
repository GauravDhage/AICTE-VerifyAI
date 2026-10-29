
from ..database import SessionLocal
from ..models import DemoUser
from ..services.auth import hash_pw


DEMO_USERS = [
    {
        "username": "officer",
        "full_name": "Dr. S. K. Sharma",
        "role": "Scrutiny Officer",
        "designation": "Senior Scrutiny Officer",
        "employee_id": "AICTE-SO-101",
        "password": "Officer@123",
    },
    {
        "username": "officer2",
        "full_name": "Dr. Anita Desai",
        "role": "Scrutiny Officer",
        "designation": "Assistant Director (Approval)",
        "employee_id": "AICTE-AD-102",
        "password": "Officer@123",
    },
    {
        "username": "officer3",
        "full_name": "Prof. R. C. Verma",
        "role": "Scrutiny Officer",
        "designation": "Deputy Director (EoA)",
        "employee_id": "AICTE-DD-103",
        "password": "Officer@123",
    },
    {
        "username": "senior",
        "full_name": "Dr. K. Ramamurthy",
        "role": "Senior Reviewer",
        "designation": "Joint Director (Regional Officer)",
        "employee_id": "AICTE-RO-201",
        "password": "Senior@123",
    },
    {
        "username": "admin",
        "full_name": "Member Secretary AICTE",
        "role": "Administrator",
        "designation": "Advisor & Member Secretary",
        "employee_id": "AICTE-HQ-001",
        "password": "Admin@123",
    },
]


def seed_users():
    db = SessionLocal()
    created = 0
    existing = 0

    try:
        for item in DEMO_USERS:
            user = (
                db.query(DemoUser)
                .filter_by(username=item["username"])
                .first()
            )

            if user:
                existing += 1
                print(f"Already exists: {item['username']}")
                continue

            user = DemoUser(
                username=item["username"],
                full_name=item["full_name"],
                role=item["role"],
                designation=item["designation"],
                employee_id=item["employee_id"],
                password_hash=hash_pw(item["password"]),
            )
            db.add(user)
            created += 1

        db.commit()
        print(f"Created: {created}; already existed: {existing}")

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_users()
