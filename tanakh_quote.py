#!/usr/bin/env python3
"""
tanakh_quote.py
Displays a Tanakh quote of the day on terminal open.
Quote rotates daily. New one each morning.
"""
 
import datetime
import textwrap
from quotes import quote 
 
def get_quote_of_the_day() -> tuple[str, str]:
    day_of_year = datetime.date.today().timetuple().tm_yday
    index = day_of_year % len(QUOTES)
    return QUOTES[index]
 
def display():
    ref, text = get_quote_of_the_day()
    today = datetime.date.today().strftime("%A, %B %d")
    width = 60
 
    wrapped = textwrap.fill(text, width=width - 4)
    lines = wrapped.split("\n")
 
    print()
    print("  ┌" + "─" * (width - 2) + "┐")
    print(f"  │{'Tanakh — ' + today:^{width - 2}}│")
    print("  ├" + "─" * (width - 2) + "┤")
    for line in lines:
        print(f"  │  {line:<{width - 4}}│")
    print("  ├" + "─" * (width - 2) + "┤")
    print(f"  │  {ref:<{width - 4}}│")
    print("  └" + "─" * (width - 2) + "┘")
    print()
 
if __name__ == "__main__":
    display()
