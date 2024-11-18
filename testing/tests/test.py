
from app.db import get_db

# test db.py
def test_db():
    db = get_db()
    assert db
    db.close()
test_db()