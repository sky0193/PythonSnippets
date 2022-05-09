import pandas as pd
import wikipedia as wp

html = wp.page("List_of_video_games_considered_the_best").html().encode("UTF-8")
try: 
    df = pd.read_html(html)[1]  # Try 2nd table first as most pages contain contents table first
except IndexError:
    df = pd.read_html(html)[0]
print(df.to_string())