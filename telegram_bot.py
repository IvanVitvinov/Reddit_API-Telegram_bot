import json
import asyncio
from telegram import Bot


class TelegramBot:

    def __init__(self):
        self. photo_path = 'Data/g1.png'

    async def telegram_send(self):
        with open('Data/good_subs.json', 'r') as f:
            data = json.load(f)

        # Get the name of the subreddits from the gs_ls list (which was generated in get_data)
        subreddits = data["gs_ls"]
        # Collecting a message to send to Telegram
        message = f"List of subbreds with low competition at the moment:\n\n"
        for subreddit in subreddits:
            message += f"- [{subreddit}] (https://www.reddit.com/r/{subreddit}/)\n"

        message += "\nDo you want your post to be number one in one of these subbreds?\nWrite -> ..."

        # Отправляем сообщение в телеграм канал
        bot = Bot(token='your_token')
        chat_id = 'your_chat_id'
        with open(self.photo_path, 'rb') as photo:
            await bot.send_photo(chat_id=chat_id, photo=photo, caption=message, parse_mode="Markdown")


async def main():
    tg = TelegramBot()
    await tg.telegram_send()

if __name__ == '__main__':
    asyncio.run(main())


