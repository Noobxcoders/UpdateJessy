from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"🎀 𝘾𝙡𝙤𝙨𝙚 🎀"
        )
    ]
    second = [
        InlineKeyboardButton(
            # text=_["BACK_BUTTON"],
            text="Home",
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text="More",
            url=f"t.me/Noobc0der",
        ),
        InlineKeyboardButton(
            text="𝖢𝗅𝗈𝗌𝖾", callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Admin",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Auth",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="𝖡𝖫-𝖴𝗌𝖾𝗋𝗌",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝖡𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝖦-𝖡𝖺𝗇",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="Lyrics",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝖯𝗂𝗇𝗀",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="𝖯𝗅𝖺𝗒",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="Playlist",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Videochats",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="Start",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="Sudo",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    # text=_["BACK_BUTTON"],
                    text="Back",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"🎀 𝐂𝐥𝐨𝐬𝐞 🎀"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✨ ʙᴀᴄᴋ ✨",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
