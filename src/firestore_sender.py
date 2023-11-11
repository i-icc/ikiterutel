from firebase_admin import initialize_app
from firebase_admin import firestore, credentials
from datetime import datetime
from zoneinfo import ZoneInfo


class FireStoreSender:
    def __init__(self):
        cred = credentials.Certificate('../.env/serviceAccount.json')
        initialize_app(cred)
        self._db = firestore.client()

    def send2ikiterutel(self):
        self._db.collection("ikiterutel").add(
            {
                "datetime": datetime.now(ZoneInfo("Asia/Tokyo")),
                "door_id": 1,
                "is_open": True,
            }
        )


if __name__ == "__main__":
    fss = FireStoreSender()
    fss.send2ikiterutel()
