from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Div
from bokeh.layouts import column
from bokeh.io import output_notebook

# Prepare some data
x = ["2024-09-09 16:32:07", "2024-09-09 16:33:07", "2024-09-09 16:34:07", "2024-09-09 16:35:07", "2024-09-09 16:36:07"]
y = [1, 0, 0, 1, 1]

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a figure
p = figure(title="Server Verfügbarkeit", x_range=x, y_range=(-0.5, 1.5), height=300, width=800,
           x_axis_label='Time', y_axis_label='State', tools="")

# Add a line and circle markers
p.line('x', 'y', source=source, line_width=2, color="navy", alpha=0.5)
p.circle('x', 'y', size=10, source=source, color="navy", alpha=0.5)

# Add descriptive text fields using Div
intro_text = Div(text='<h2>Hello, here is my report:</h2>', width=800)
description_text = Div(text='<p>This diagram displays the server availability over time.</p>', width=800)

# Arrange the layout: intro text, plot, description text
layout = column(intro_text, p, description_text)



# Display the plot
show(layout)
