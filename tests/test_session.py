"""Unit tests for SessionStore."""
import unittest
from mcp_stateful_session.session import SessionStore

class TestSessionStore(unittest.TestCase):
    def test_session_lifecycle(self):
        store = SessionStore()
        store.create_session("s1", {"count": 1})
        self.assertEqual(store.get_value("s1", "count"), 1)
        store.set_value("s1", "count", 2)
        self.assertEqual(store.get_value("s1", "count"), 2)

    def test_rollback(self):
        store = SessionStore()
        store.create_session("s2", {"x": 10})
        sid = store.snapshot("s2", "init")
        store.set_value("s2", "x", 50)
        self.assertEqual(store.get_value("s2", "x"), 50)
        self.assertTrue(store.rollback("s2", sid))
        self.assertEqual(store.get_value("s2", "x"), 10)

    def test_invalid_rollback(self):
        store = SessionStore()
        store.create_session("s3")
        self.assertFalse(store.rollback("s3", 99))

if __name__ == "__main__":
    unittest.main()
