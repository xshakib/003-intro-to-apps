######### import libraries 
import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
shows=['Breaking Bad', 'The Boys', 'The Office', 'That 70s Show']
Comedy_values=[30.5, 10.4, 99, 70]
Drama_values=[99, 80, 40, 70]
color1='blue'
color2='darkred'
mytitle='Show Comparison'

label1='Comedy'
label2='Drama'

########### Set up the chart

def make_that_cool_barchart(shows, Comedy_values, Drama_values, color1, color2, mytitle):
    funny = go.Bar(
        x=shows,
        y=Comedy_values,
        name=label1,
        marker={'color':color1}
    )
    seriousness = go.Bar(
        x=shows,
        y=Drama_values,
        name=label2,
        marker={'color':color2}
    )

    show_data = [funny, seriousness]
    show_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    show_fig = go.Figure(data=show_data, layout=show_layout)
    return show_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(shows, Comedy_values, Drama_values, color1, color2, mytitle)
    fig.write_html('docs/barchart.html')
    print('We successfully updated the barchart!')