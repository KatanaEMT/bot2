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
    reference_menu_button = InlineKeyboardButton(
        text="Reference menu ヽ(✿ﾟ▽ﾟ)ノ",
        callback_data="reference_menu"
    )
    news_button = InlineKeyboardButton(
        "Latest News",
        callback_data="news"
    )
    my_news_button = InlineKeyboardButton(
        "My Favourite News",
        callback_data="favourite_news"
    )
    markup.add(news_button)
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profile_button)
    markup.add(reference_menu_button)
    markup.add(my_news_button)
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


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_button = InlineKeyboardButton(
        "Reference Link 🔗",
        callback_data="reference_link"
    )
    reference_profile_button = InlineKeyboardButton(
        "Referral Profile 🤭",
        callback_data="referral_profile"
    )
    markup.add(reference_button)
    markup.add(reference_profile_button)
    return markup


async def save_favourite(id):
    markup = InlineKeyboardMarkup()
    save_favourite = InlineKeyboardButton(
        "Save",
        callback_data=f"save_{id}"
    )
    markup.add(save_favourite)
    return markup

