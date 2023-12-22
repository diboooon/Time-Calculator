
def add_time(start, time, day=''):
    split_start = start.split(':')
    minutes_ampm = split_start[1].split()
    split_length = time.split(':')

    hours = int(split_start[0]) + int(split_length[0])
    minutes = int(minutes_ampm[0]) + int(split_length[1])

    extra_hours = minutes // 60
    for x in range(extra_hours):
        hours += 1
        minutes -= 60

    twelves = hours // 12
    for clock in range(twelves):
        hours -= 12

    ampm = minutes_ampm[1]
    extra_days = twelves // 2




    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_day = ''
    comment = ''
    # if minutes > 10:
    #     minutes = minutes.zfill(2)


    if ampm == 'AM':
        if int(split_start[0]) < 12 and hours >= 12:
            ampm = 'PM'
        elif twelves % 2 == 0:
            ampm = 'AM'
        else:
            ampm = 'PM'


        if extra_days == 1:
            comment = "(next day)"
        elif extra_days > 1:
            comment = f"({extra_days} days later)"


        if day:
            weekday = day.title()
            day_index = day_list.index(weekday)

            new_day_index = day_index

            for i in range(0, extra_days):
                new_day_index += 1
                if new_day_index >= 6:
                    new_day_index -= 7




            new_day = day_list[new_day_index]
            # print(new_day)
            # return f"{hours}:{minutes} {ampm},{new_day} {comment}"
            print(f"{hours}:{minutes:02d} {ampm}, {new_day} {comment}")

        else:
            # return f"{hours}:{minutes} {ampm} {comment}"
            print(f"{hours}:{minutes:02d} {ampm} {comment}")




    elif ampm == 'PM':
        if twelves % 2 == 1:
             ampm = 'AM'
        else:
            ampm = 'PM'




        if twelves == 1 or twelves == 2 :
            comment = "(next day)"
        elif twelves >= 3:
            extra_days = (twelves // 2) + 1
            comment = f"({extra_days} days later)"

        if day:
            weekday = day.title()
            day_index = day_list.index(weekday)

            new_day_index = day_index

            for i in range(0, extra_days):
                new_day_index += 1
                if new_day_index >= 6:
                    new_day_index -= 7


            new_day = day_list[new_day_index]
            # return f"{hours}:{minutes} {ampm},{new_day} {comment}"
            print(f"{hours}:{minutes:02d} {ampm}, {new_day} {comment}")

        else:
            print(f"{hours}:{minutes:02d} {ampm} {comment}")




add_time("6:30 PM", "205:12")
