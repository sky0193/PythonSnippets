from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.io import output_notebook
from bokeh.models import Label
# Prepare some data
x = ["2024-09-09 16:32:07", "2024-09-09 16:33:07", "2024-09-09 16:34:07", "2024-09-09 16:35:07", "2024-09-09 16:36:07"]
y = [1, 0, 0, 1, 1]

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a figure
p = figure(title="Server Verfügbarkeit", x_range=x, y_range=(0, 2), height=300, width=800,
           x_axis_label='Time', y_axis_label='State', tools="")


p.line('x', 'y', source=source, line_width=2, color="navy", alpha=0.5)

# Add circle markers for flow
p.circle('x', 'y', size=10, source=source, color="navy", alpha=0.5)

show(p)
