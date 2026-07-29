import json
import os


FILE = "users.json"


def load_users():

    if not os.path.exists(FILE):
        return {}

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)



def save_users(users):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            users,
            f,
            indent=4,
            ensure_ascii=False
        )



def create_user(user_id, username):

    users = load_users()

    uid = str(user_id)


    if uid not in users:

        users[uid] = {
            "username": username,
            "xp": 0,
            "level": 1,
            "lessons": []
        }

        save_users(users)


    return users[uid]



def complete_lesson(
        user_id,
        username,
        lesson_id
):

    users = load_users()

    uid = str(user_id)


    if uid not in users:

        create_user(
            user_id,
            username
        )

        users = load_users()


    user = users[uid]


    if lesson_id not in user["lessons"]:

        user["lessons"].append(
            lesson_id
        )

        user["xp"] += 10

        user["level"] = (
            user["xp"] // 100
        ) + 1


        save_users(users)

        return True, user


    return False, user



def get_profile(user_id):

    users = load_users()

    return users.get(
        str(user_id)
    )