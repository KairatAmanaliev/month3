import datetime
from aiogram import bot, Bot
from database.bot_db import sql_command_get_id_name
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from config import bot, ADMIN


async def napominalka(bot: Bot):
    users = await sql_command_get_id_name()
    for user in users:
        await bot.send_message(user[0], f"Сегодня лч! {user[1]}")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    scheduler.add_job(
        napominalka(bot),
        trigger=DateTrigger(
            run_date=datetime.datetime(
                year=2023, month=4, day=12, hour=14, minute=0, second=0
            )
        ),
        kwargs={"bot": bot}
    )

    scheduler.start()
