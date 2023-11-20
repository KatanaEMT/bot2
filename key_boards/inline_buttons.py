from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration 😇",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        text="My profile 👈(ﾟヮﾟ👈))",
        callback_data="my_profile"
    )
    random_profile_button = InlineKeyboardButton(
        text="View Profiles ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°))",
        callback_data="random_profiles"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profile_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python 🐍",
        callback_data="python"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo 🔥",
        callback_data="mojo"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like 👍",
        callback_data=f"liked_profile_{owner_tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎",
        callback_data="random_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


# async def profile_rename_keyboard(owner_tg_id):
#     markup = InlineKeyboardMarkup()
#     update_button = InlineKeyboardButton(
#         "Update ❤✅",
#         callback_data="update"
#     )
#     delete_button = InlineKeyboardButton(
#         "Delete ❌",
#         callback_data="delete"
#     )
#     markup.add(update_button)
#     markup.add(delete_button)
#     return markup
