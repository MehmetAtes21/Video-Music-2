from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
        InlineKeyboardButton("πͺ§ πͺπΊππΊπ ", url="t.me/StarBotKanal"),
        InlineKeyboardButton("πΉπ· π£πΎπππΎπ ", url="t.me/Sohbetfanonlinee"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ sα΄Κα΄Ιͺ | α΄ Ιͺα΄α΄α΄ π₯",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="β’ Ι’α΄ΚΙͺ",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="β’ α΄α΄α΄α΄α΄",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="π sα΄Κα΄Ιͺ ΙͺΙ΄α΄ΙͺΚ",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="π α΄ Ιͺα΄α΄α΄ ΙͺΙ΄α΄ΙͺΚ",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="β’ Ι’α΄ΚΙͺ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="β’ α΄α΄α΄α΄α΄", callback_data=f"close"),
        ],
    ]
    return buttons

