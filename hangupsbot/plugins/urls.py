import plugins
import re,asyncio

def _initialise(bot):
    plugins.register_handler(_watch_for_url)
    plugins.register_user_command(["url"])


def url(bot,event,command):
    # Initialise memory locations
    if not bot.memory.exists(['url']):
        bot.memory.set_by_path(['url'],{})
    if not bot.memory.exists(['ur'],event.conv_id):
        bot.memory.set_by_path(['url',event.conv_id],{})

    if command.startswith("clear"):
        bot.memory.set_by_path(['url',event.conv_id],{})
        yield from bot.coro_send_message(event.conv_id,"URLS Cleared")
    else:
        urls = bot.memory.get_by_path(['url',event.conv_id])
        html = []
        for url in enumerate(urls):
            html.append("<a href={0}>{0}</a>".format(url))
        yield from bot.coro_send_message(event.conv_id,html)

@asyncio.coroutine
def _watch_for_url(bot,event,command):
    regex = "(http:|https:|www.|ftp:){1}.*"
    url = re.search(regex,event.text)

    #bot.memory.set_by_path(['url',event.conv_id])
    if url:
        bot.memory.set_by_path(['url',event.conv_id],url.group(0))

