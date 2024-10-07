from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Div
from bokeh.layouts import column
from bokeh.io import output_notebook

# Prepare some data for the first diagram (Server Availability)
x1 = ["2024-09-09 16:32:07", "2024-09-09 16:33:07", "2024-09-09 16:34:07", "2024-09-09 16:35:07", "2024-09-09 16:36:07"]
y1 = [1, 0, 0, 1, 1]

# Create a ColumnDataSource for the first diagram
source1 = ColumnDataSource(data=dict(x=x1, y=y1))

# Create the first figure
p1 = figure(title="System Verfügbarkeit", x_range=x1, y_range=(-0.5, 1.5), height=300, width=800,
            x_axis_label='Time', y_axis_label='State', tools="")

# Add a line and circle markers to the first plot
p1.line('x', 'y', source=source1, line_width=2, color="navy", alpha=0.5)
p1.circle('x', 'y', size=10, source=source1, color="navy", alpha=0.5)

# Prepare some data for the second diagram (Sample Data 2)
x2 = ["2024-09-09 16:32:07", "2024-09-09 16:33:07", "2024-09-09 16:34:07", "2024-09-09 16:35:07", "2024-09-09 16:36:07"]
y2 = [0, 1, 1, 0, 0]

# Create a ColumnDataSource for the second diagram
source2 = ColumnDataSource(data=dict(x=x2, y=y2))

# Create the second figure
p2 = figure(title="Server Verfügbarkeit", x_range=x2, y_range=(-0.5, 1.5), height=300, width=800,
            x_axis_label='Time', y_axis_label='State', tools="")

# Add a line and circle markers to the second plot
p2.line('x', 'y', source=source2, line_width=2, color="green", alpha=0.5)
p2.circle('x', 'y', size=10, source=source2, color="green", alpha=0.5)

# Add descriptive text fields using Div
intro_text = Div(text='<h2>Hello, here is my report:</h2>', width=800)
description_text = Div(text='<p>This diagram displays the server availability over time.</p>', width=800)
description_text2 = Div(text='<p>This is a second sample diagram with different data.</p>', width=800)

# Arrange the layout: intro text, first plot, description text, second plot, second description text
layout = column(intro_text, p1, description_text, p2, description_text2)

# Display the plot
show(layout)
