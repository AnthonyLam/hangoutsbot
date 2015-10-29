import plugins,re,calendar

def _initialise(bot):
    self.schedule = Schedule()
    plugins.register_user_command(["schedule"])


def schedule(bot,event,date=None,item=None,*args):
    yield from bot.coro_send_message(event.conf,_(calendar.HTMLCalendar().formatmonth(2015,11)))
    
    #yield from bot.coro_send_message(event.conv,_("<i>{} scheduled: {} @ {}</i>").format(event.user.full_name,))



class Schedule():

    def __init__(self):
        self.date = None

    def add(self):
        pass

    def remove(self):
        pass


