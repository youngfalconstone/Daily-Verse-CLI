
#!/usr/bin/env python3
"""
tanakh_quote.py
Displays a Tanakh quote of the day on terminal open.
Quote rotates daily — same quote all day, new one each morning.
"""
 
import datetime
import textwrap
from quotes import QUOTES
 
def get_quote_of_the_day() -> tuple[str, str]:
    day_of_year = datetime.date.today().timetuple().tm_yday
    index = day_of_year % len(QUOTES)
    return QUOTES[index]
 
def display():
    ref, text = get_quote_of_the_day()
    today = datetime.date.today().strftime("%A, %B %d")
 
    print()
    print(f"  Tanakh — {today}")
    print()
    print(f"  {textwrap.fill(text, width=60)}")
    print()
    print(f"  — {ref}")
    print()
 
if __name__ == "__main__":
    display()
