# package samples

from enum import Enum
from random import choice

# This sample defines a workaround for a switch statement a la Java.
# If you don't know what that is, don't worry, it's not required.


class WeekDay(Enum):
    MONDAY    = 1
    TUESDAY   = 2
    WEDNESDAY = 3
    THURSDAY  = 4
    FRIDAY    = 5
    SATURDAY  = 6
    SUNDAY    = 7


def switch_emulation_program():
    day = get_random_day()
    # Many languages (for instance Java, C#, C) have a 'switch' statement
    # that allows us to write code like the following:
    # List<Chore> chores;
    # switch (day) {
    # case MONDAY: monday_chores(); break;
    # case TUESDAY: tuesday_chores(); break;
    # ... }
    # Python does not have a switch statement, and using an if statement quickly
    # becomes tedious:
    # if day is WeekDay.MONDAY:
    #     lessons = [8, 13]
    # elif day is WeekDay.TUESDAY:
    #     lessons = [8, 10, 13]
    # ... and so on. We need to write the name of the variable (day)
    # and the test (is) for every case we're testing.
    # But there are some elegant workarounds. My favorite uses a *dictionary* to define
    # the switcher itself:
    switcher = {
        WeekDay.MONDAY: [8, 13],
        WeekDay.TUESDAY: [8, 10, 13],
        WeekDay.WEDNESDAY: [13, 15],
        WeekDay.THURSDAY: [8, 10, 15],
        WeekDay.FRIDAY: [8, 10, 13]
    }
    # We can now use this switcher to 'get' the right value given the variable:
    lessons = switcher.get(day)
    # Question: What happens if day is SATURDAY or SUNDAY?

    print(f"{day}: {lessons}")


def get_random_day() -> WeekDay:
    all_days = list(WeekDay)
    return choice(all_days)


if __name__ == "__main__":
    switch_emulation_program()
