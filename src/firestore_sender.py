from firebase_admin import initialize_app
from firebase_admin import firestore, credentials
from datetime import datetime
from zoneinfo import ZoneInfo


class FireStoreSender:
    def __init__(self):
        cred = credentials.Certificate('../.env/serviceAccount.json')
        initialize_app(cred)
        self._db = firestore.client()

    def send2ikiterutel(self, door_id: int, is_open: bool):
        self._db.collection("ikiterutel").add(
            {
                "datetime": datetime.now(ZoneInfo("Asia/Tokyo")),
                "door_id": door_id,
                "is_open": is_open,
            }
        )


if __name__ == "__main__":
    fss = FireStoreSender()
    fss.send2ikiterutel(1, True)
