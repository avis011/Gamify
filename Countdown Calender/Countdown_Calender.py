from tkinter import Tk, Canvas
from datetime import date, datetime

root = Tk()
root.title("Countdown Calendar")
root.maxsize(800, 800)
root.minsize(800, 600)
c = Canvas(root, width=800, height=600, bg='sky blue')
c.pack()
c.create_text(100, 50, anchor='w', fill='purple',
              font='Courier 36 bold underline', text='My Countdown Calendar')


def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            # print(line)
            current_event = line.split(',')
            # print(current_event)
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            # print(event_date)
            current_event[1] = event_date
            # print(current_event[1])
            list_events.append(current_event)
    return list_events


def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]


events = get_events()
today = date.today()

vertical_space = 100
events.sort(key=lambda x: x[1])
for event in events:
    # print(event)
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    print('\n')
    display = 'It is %s days until %s' % (days_until, event_name)
    if (int(days_until) <= 7):
        text_col = 'red'
    else:
        text_col = 'blue'
    c.create_text(100, vertical_space, anchor='w', fill=text_col, \
                  font='Arial 28 bold', text=display)
    vertical_space = vertical_space + 60

root.mainloop()
