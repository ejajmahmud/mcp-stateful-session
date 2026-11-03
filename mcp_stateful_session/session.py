"""Stateful session persistence and snapshot rollback manager."""
import copy
import time
from typing import Dict, Any, List, Optional


class SessionStore:
    def __init__(self):
        self._sessions: Dict[str, Dict[str, Any]] = {}

    def create_session(self, session_id: str, initial_state: Optional[Dict[str, Any]] = None) -> None:
        self._sessions[session_id] = {
            "state": copy.deepcopy(initial_state or {}),
            "snapshots": [],
            "created_at": time.time(),
            "updated_at": time.time()
        }

    def set_value(self, session_id: str, key: str, value: Any) -> None:
        session = self._sessions[session_id]
        session["state"][key] = copy.deepcopy(value)
        session["updated_at"] = time.time()

    def get_value(self, session_id: str, key: str, default: Any = None) -> Any:
        return self._sessions[session_id]["state"].get(key, default)

    def snapshot(self, session_id: str, tag: str) -> int:
        session = self._sessions[session_id]
        snap_id = len(session["snapshots"])
        session["snapshots"].append({
            "snap_id": snap_id,
            "tag": tag,
            "state": copy.deepcopy(session["state"]),
            "timestamp": time.time()
        })
        return snap_id

    def rollback(self, session_id: str, snap_id: int) -> bool:
        session = self._sessions[session_id]
        if 0 <= snap_id < len(session["snapshots"]):
            session["state"] = copy.deepcopy(session["snapshots"][snap_id]["state"])
            # Trim subsequent snapshots
            session["snapshots"] = session["snapshots"][:snap_id + 1]
            session["updated_at"] = time.time()
            return True
        return False

    def get_snapshots(self, session_id: str) -> List[Dict[str, Any]]:
        return [{"id": s["snap_id"], "tag": s["tag"], "timestamp": s["timestamp"]} for s in self._sessions[session_id]["snapshots"]]
