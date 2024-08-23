import random
import time
from config import TOKEN
from constants import *
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)
from pet_module import Pet, SaveState

pet = Pet()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [
        [InlineKeyboardButton(LOVE, callback_data=LOVE_ID)],
        [InlineKeyboardButton(EAT, callback_data=EAT_ID)],
        [InlineKeyboardButton(PLAY, callback_data=PLAY_ID)],
        [InlineKeyboardButton(DEAD, callback_data=DEAD_ID)],
        [InlineKeyboardButton(SLEEP, callback_data=SLEEP_ID)],
        [InlineKeyboardButton(STATUS, callback_data=STATUS_ID)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    state = SaveState(update.effective_user.username)
    save_data = state.read_data()
    if save_data:
        pet.__dict__ = save_data
    sticker, bot_message = pet.hello()
    await delete_rubbish(update, context)
    await context.bot.send_sticker(update.effective_chat.id, sticker)
    await context.bot.send_message(
        update.effective_chat.id,
        bot_message,
        reply_markup=reply_markup,
    )
    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    chat_id = update.effective_message.chat_id
    await query.answer()
    keyboard = [
        [InlineKeyboardButton(LOVE, callback_data=LOVE_ID)],
        [InlineKeyboardButton(EAT, callback_data=EAT_ID)],
        [InlineKeyboardButton(PLAY, callback_data=PLAY_ID)],
        [InlineKeyboardButton(DEAD, callback_data=DEAD_ID)],
        [InlineKeyboardButton(SLEEP, callback_data=SLEEP_ID)],
        [InlineKeyboardButton(STATUS, callback_data=STATUS_ID)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    state = SaveState(update.effective_user.username)
    state.save_data(pet)
    sticker, bot_message = pet.hello()
    await delete_rubbish(update, context)
    await context.bot.send_sticker(chat_id, sticker)
    await context.bot.send_message(chat_id,
        text=bot_message,
        reply_markup=reply_markup,
    )
    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_once(miss_you, TIME_TO_MISS, chat_id=chat_id, name=str(chat_id))
    return START_ROUTES


async def make_love(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Назад в меню", callback_data=MENU)],
        [InlineKeyboardButton("Еще погладить", callback_data=LOVE_ID)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    sticker, bot_message = pet.increase_love()
    bot_message += f" Уровень любви повышен: {pet.love}"
    if bot_message != query.message.text:
        await delete_rubbish(update, context)
        await context.bot.send_sticker(update.effective_chat.id, sticker)
        await context.bot.send_message(update.effective_chat.id,
            text=bot_message, reply_markup=reply_markup
        )
    return START_ROUTES



async def delete_rubbish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.effective_chat.delete_message(update.effective_message.message_id)
        await update.effective_chat.delete_message(update.effective_message.message_id-1)
    except:
        pass




async def feed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Действие кнопки Положить корм"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Назад в меню", callback_data=MENU)
        ],
        [
            InlineKeyboardButton("Еще покормить", callback_data=EAT_ID)
        ]
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    sticker, bot_message = pet.increase_satiety()
    bot_message += f" Уровень сытости повышен: {pet.satiety}"
    if bot_message != query.message.text:
        await delete_rubbish(update, context)
        await context.bot.send_sticker(update.effective_chat.id, sticker)
        await context.bot.send_message(update.effective_chat.id, bot_message, reply_markup=reply_markup)
    return START_ROUTES


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Действие кнопки "Играть" """
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Назад в меню", callback_data=MENU)
        ],
        [
            InlineKeyboardButton("Еще поиграть", callback_data=PLAY_ID)
        ]
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    sticker, bot_message = pet.increase_happiness()
    bot_message += f" Уровень счастья повышен: {pet.happiness}"
    if bot_message != query.message.text:
        await delete_rubbish(update, context)
        await context.bot.send_sticker(update.effective_chat.id, sticker)
        await context.bot.send_message(update.effective_chat.id, bot_message, reply_markup=reply_markup)
    return START_ROUTES

async def sleep(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Действие кнопки "Уложить спать" """
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Назад в меню", callback_data=MENU)
        ],
        [
            InlineKeyboardButton("Еще погладить", callback_data=SLEEP_ID)
        ]
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    sticker, bot_message = pet.increase_energy()
    if bot_message != query.message.text:
        await delete_rubbish(update, context)
        await context.bot.send_sticker(update.effective_chat.id, sticker)
        await context.bot.send_message(update.effective_chat.id,bot_message)
        time.sleep(TIME_TO_SLEEP)
        await context.bot.send_message(update.effective_chat.id,bot_message, reply_markup=reply_markup)
    return START_ROUTES

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    bot_message = "Возвращайся скорее, я буду ждать тебя. Твой Тамагочи"
    await context.bot.send_sticker(update.effective_chat.id, REST_STICK)
    await context.bot.send_message(update.effective_chat.id,bot_message)
    return ConversationHandler.END

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Назад в меню", callback_data=MENU)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.delete_message()
    bot_message = f"Мои статы:\nЛюбовь: {pet.love}\nСытость: {pet.satiety}\nСчастье: {pet.happiness}\nЭнергия: {pet.energy}"
    await delete_rubbish(update, context)
    await context.bot.send_sticker(update.effective_chat.id, BIRTHDAY_STICK)
    await context.bot.send_message(update.effective_chat.id,bot_message, reply_markup=reply_markup)
    return START_ROUTES


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Удалить"""
    state = SaveState(update.effective_user.username)
    state.be_dead()
    pet.__init__()
    await context.bot.send_sticker(update.effective_chat.id, NOT_GOOD_STICK)
    await context.bot.send_message(update.effective_chat.id, "За что, хозяин? Я ведь лишь старался быть любимым...")
    return ConversationHandler.END

def remove_job_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

async def miss_you(context: ContextTypes.DEFAULT_TYPE):
    """Скучает"""
    job = context.job
    bot_message = random.choice(MISS_PHRASES)
    pet.decrease_stats()
    keyboard = [
        [InlineKeyboardButton("Назад в меню", callback_data=MENU)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_sticker(job.chat_id, NOT_GOOD_STICK)
    await context.bot.send_message(job.chat_id, bot_message, reply_markup=reply_markup)
    return MENU


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(make_love, pattern=f"^{LOVE_ID}$"),
                CallbackQueryHandler(feed, pattern=f"^{EAT_ID}$"),
                CallbackQueryHandler(play, pattern=f"^{PLAY_ID}$"),
                CallbackQueryHandler(sleep, pattern=f"^{SLEEP_ID}$"),
                CallbackQueryHandler(stats, pattern=f"^{STATUS_ID}$"),
                CallbackQueryHandler(delete, pattern="^" + str(DEAD_ID) + "$"),  
                CallbackQueryHandler(start_over, pattern="^" + str(MENU) + "$"),
            ],
            END_ROUTES: [
                CallbackQueryHandler(end, pattern="^" + str(TWO) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )


    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
