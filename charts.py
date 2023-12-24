import data_process as dp
import importlib
import altair as alt
import IPython
import pandas as pd


def draw_chart(pd,rank=None):
    # Base value for the win rate baseline
    base_value = 50
    plot_data = pd.sort_values(by='win_rate', ascending=False)
    # Create a bar chart with bars extending from the baseline
    bar_chart = alt.Chart(plot_data).mark_bar().encode(
        x=alt.X('Civilization Name:N',sort=None),
        y=alt.Y('start:Q', scale=alt.Scale(domain=[40, 60]), axis=alt.Axis(title="Win Rate")),
        y2=alt.Y2('end:Q'),
        color=alt.condition(
            alt.datum.win_rate >= base_value,
            alt.value("steelblue"),  # Color for win rates above the baseline
            alt.value("orange")  # Color for win rates below the baseline
        ),
        tooltip=[
            alt.Tooltip(field='Civilization Name', type='nominal', title="Civilization"),
            alt.Tooltip(field='win_rate', type='quantitative', title="Winrate")
        ]
    ).transform_calculate(
        start="datum.win_rate >= 50 ? 50 : datum.win_rate",
        end="datum.win_rate >= 50 ? datum.win_rate : 50"
    ).interactive()

    # Create the flag image chart using the new 'image_url' column
    flags = alt.Chart(plot_data).mark_image(
        width=15  # Adjust the width of the image as needed
    ).encode(
        alt.X('Civilization Name:N',sort=None),
        y=alt.Y('start:Q', scale=alt.Scale(domain=[40, 60]), axis=alt.Axis(title="Win Rate")),
        y2=alt.Y2('end:Q'),
        tooltip=[
            alt.Tooltip(field='Civilization Name', type='nominal', title="Civilization"),
            alt.Tooltip(field='win_rate', type='quantitative', title="Winrate")
        ],
        url='image_url:N'
    ).transform_calculate(
        start="datum.win_rate >= 50 ? 50 : datum.win_rate",
        end="datum.win_rate >= 50 ? datum.win_rate : 50"
    )

    # Combine the bar chart and flag images
    combined_chart = alt.layer(bar_chart, flags)
    combined_chart = combined_chart.properties(
    title={
        "text": ["Civilization Win Rates"],  # Chart title text
        "subtitle": [f"in rank {rank}"],  # Chart subtitle text
        "color": "black",  # Title color
        "fontSize": 20,  # Title font size
        "subtitleFontSize": 15,  # Subtitle font size
        "anchor": "start",  # Aligns text to the left
        "offset": 5  # Offset from the top of the chart
    }
        )

    return combined_chart
