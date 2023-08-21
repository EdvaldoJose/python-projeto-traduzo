# from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


from src.models.history_model import HistoryModel


def test_history_delete(app_test):
    translation_history_one = HistoryModel(
        {
            "text-to-translate": "Do you love music?",
            "translate-from": "en",
            "translate-to": "pt",
        }
    ).save()

    UserModel({"name": "Edvaldo", "token": "12345"}).save()
    user = UserModel.find_one({"name": "Edvaldo"})

    app_test.delete(
        f"/admin/history/{translation_history_one.data['_id']}",
        headers={"Authorization": user.data['token'],
                 "User": user.data['name']}
    )
