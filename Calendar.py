calendar_of_events = []


def events():

    def add_event(event):
        calendar_of_events.append(event)
        print(f'Подія {event} додана.')

    def remove_event(event):
        if event in calendar_of_events:
            calendar_of_events.remove(event)
            print(f'Подія {event} видалена')
        else:
            print(f'Подія {event} не знайдена')

    def see_event():
        if calendar_of_events:
            print("Події: \n")
            for event in enumerate(calendar_of_events, 1):
                print(f'{event}')
        else:
            print("Подій не знайдено!")
    return see_event, remove_event, add_event


see_event, remove_event, add_event = events()
add_event("День народження 8 травня")
add_event("Зустріч 5 вересня!")
see_event()
