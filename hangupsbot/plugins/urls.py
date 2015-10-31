import plugins
import re,asyncio

def _initialise(bot):
    plugins.register_handler(_watch_for_url,"message")
    plugins.register_user_command(["url"])

def url(bot,event,command,)

@asyncio.coroutine
def _watch_for_url(bot,event,command):
    regex = "(http:|https:|www.|ftp:){1}.*"
    url = re.search(regex,event.text)
    
    event.coro_send_message(event.conv,"Got url: {}".format(url))

