from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="ð Ses Kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="ð Ses DÃ¼zeyi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="â¢ Êá´á´á´ÉªÊÉª á´á´ÊÊá´É´Éªá´Éª", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="â¢ É¢á´sá´á´ÊÉ¢á´ á´á´É´á´ÊÉª", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="â¢ á´á´á´á´á´", callback_data="close"),
        ],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} ððð®ð¿ð¹ð®ð¿ð¶**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð á´á´á´ á´á´á´á´á´Êá´Ê", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="âï¸ á´Êá´ÊÊá´Ê á´á´É´á´sá´", callback_data="settingm"
                )
            ],
        ]
        return f"ð  **ðð {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð á´á´á´ á´á´á´á´á´Êá´Ê", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="âï¸ á´Êá´ÊÊá´Ê á´á´É´á´sá´", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð á´á´sá´á´á´ É¢Êá´Êá´", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **ðð {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð á´á´á´ á´á´á´á´á´Êá´Ê", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="âï¸ á´Êá´ÊÊá´Ê á´á´É´á´sá´", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¹ð· á´á´sá´á´á´ á´á´É´á´ÊÉª", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"ð  **ðð {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð á´á´á´ á´á´á´á´á´Êá´Ê", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="âï¸ á´Êá´ÊÊá´Ê á´á´É´á´sá´", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¹ð· á´á´sá´á´á´ á´á´É´á´ÊÉª", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="ð á´á´sá´á´á´ É¢Êá´Êá´", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **ðð {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð á´á´á´ á´á´á´á´á´Êá´Ê", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Êá´É´Éª É¢Êá´Êá´ á´á´Êá´ â",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"ð  **ðð {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð á´á´á´ á´á´á´á´á´Êá´Ê", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Êá´É´Éª É¢Êá´Êá´ á´á´Êá´ â",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð á´á´sá´á´á´ É¢Êá´Êá´", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **ðð {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð á´á´á´ á´á´á´á´á´Êá´Ê", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Êá´É´Éª É¢Êá´Êá´ á´á´Êá´ â",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¹ð· á´á´sá´á´á´ á´á´É´á´ÊÉª", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"ð  **ðð {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð á´á´á´ á´á´á´á´á´Êá´Ê", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Êá´É´Éª É¢Êá´Êá´ á´á´Êá´ â",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¹ð· á´á´sá´á´á´ á´á´É´á´ÊÉª", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="ð á´á´sá´á´á´ É¢Êá´Êá´", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **ðð {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="ð Ses Kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="ð Ses DÃ¼zeyi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="â¢ Êá´á´á´ÉªÊÉª á´á´ÊÊá´É´Éªá´Éª", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="â¢ É¢á´sá´á´ÊÉ¢á´ á´á´É´á´ÊÉª", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="â¢ á´á´á´á´á´", callback_data="close"),
            InlineKeyboardButton(text="â¢ É¢á´ÊÉª", callback_data="okaybhai"),
        ],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} ððð®ð¿ð¹ð®ð¿ð¶**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="ð Ses Seviyesini SÄ±fÄ±rla ð", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="ð DÃ¼ÅÃ¼k Ses", callback_data="LV"),
            InlineKeyboardButton(text="ð Orta Ses", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="ð YÃ¼ksek Ses", callback_data="HV"),
            InlineKeyboardButton(text="ð GÃ¼Ã§lendirilmiÅ Ses", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="âï¸ Ãzel Birim âï¸", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="â¢ É¢á´ÊÉª", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} ððð®ð¿ð¹ð®ð¿ð¶**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="âï¸ Ãzel Birim âï¸", callback_data="AV")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} ððð®ð¿ð¹ð®ð¿ð¶**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="ð¥ Herkes", callback_data="EVE"),
            InlineKeyboardButton(text="ð YÃ¶neticiler", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="ð Yetkili KullanÄ±cÄ± Listesi", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="â¢ É¢á´ÊÉª", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} ððð®ð¿ð¹ð®ð¿ð¶**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="âï¸ ÃalÄ±Åma ZamanÄ±", callback_data="UPT"),
            InlineKeyboardButton(text="ð¾ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="ð» Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="ð½ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="ð Geri Git", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} ððð®ð¿ð¹ð®ð¿ð¶**", buttons
