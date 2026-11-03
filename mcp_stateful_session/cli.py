"""Command-line interface for MCP Stateful Session."""
import argparse
from .session import SessionStore

def main():
    parser = argparse.ArgumentParser(description="MCP Stateful Session CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate session snapshots and rollback")
    args = parser.parse_args()

    store = SessionStore()
    store.create_session("sess_01", {"file_count": 0})
    store.set_value("sess_01", "file_count", 5)
    snap0 = store.snapshot("sess_01", "created_5_files")
    store.set_value("sess_01", "file_count", 99)
    print("Corrupted state value:", store.get_value("sess_01", "file_count"))
    store.rollback("sess_01", snap0)
    print("State value after rollback:", store.get_value("sess_01", "file_count"))

if __name__ == "__main__":
    main()
