import altair as alt
alt.renderers.enable('altair_viewer')


source = alt.pd.DataFrame([
      {
        "question": "Question 1",
        "type": "Strongly disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 1",
        "type": "Disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 1",
        "type": "Neither agree nor disagree",
        "value": 1,
        "percentage": 16,
        "percentage_start": -8,
        "percentage_end": 8
      },
      {
        "question": "Question 1",
        "type": "Agree",
        "value": 5,
        "percentage": 83,
        "percentage_start": 8,
        "percentage_end": 91
      },
      {
        "question": "Question 1",
        "type": "Strongly agree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 91,
        "percentage_end": 91
      },

      {
        "question": "Question 2",
        "type": "Strongly disagree",
        "value": 1,
        "percentage": 16,
        "percentage_start": -49,
        "percentage_end": -33
      },
      {
        "question": "Question 2",
        "type": "Disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": -33,
        "percentage_end": -33
      },
      {
        "question": "Question 2",
        "type": "Neither agree nor disagree",
        "value": 4,
        "percentage": 66,
        "percentage_start": -33,
        "percentage_end": 33
      },
      {
        "question": "Question 2",
        "type": "Agree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 33,
        "percentage_end": 33
      },
      {
        "question": "Question 2",
        "type": "Strongly agree",
        "value": 1,
        "percentage": 16,
        "percentage_start": 33,
        "percentage_end": 49
      },

      {
        "question": "Question 3",
        "type": "Strongly disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 3",
        "type": "Disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 3",
        "type": "Neither agree nor disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 3",
        "type": "Agree",
        "value": 5,
        "percentage": 83,
        "percentage_start": 0,
        "percentage_end": 83
      },
      {
        "question": "Question 3",
        "type": "Strongly agree",
        "value": 1,
        "percentage": 17,
        "percentage_start": 83,
        "percentage_end": 100
      },

      {
        "question": "Question 4",
        "type": "Strongly disagree",
        "value": 1,
        "percentage": 17,
        "percentage_start": -58,
        "percentage_end": -75
      },
      {
        "question": "Question 4",
        "type": "Disagree",
        "value": 2,
        "percentage": 3,
        "percentage_start": -58,
        "percentage_end": -25
      },
      {
        "question": "Question 4",
        "type": "Neither agree nor disagree",
        "value": 3,
        "percentage": 50,
        "percentage_start": -25,
        "percentage_end": 25
      },
      {
        "question": "Question 4",
        "type": "Agree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 25,
        "percentage_end": 25
      },
      {
        "question": "Question 4",
        "type": "Strongly agree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 25,
        "percentage_end": 25
      },

      {
        "question": "Question 5",
        "type": "Strongly disagree",
        "value": 1,
        "percentage": 17,
        "percentage_start": 0,
        "percentage_end": -17
      },
      {
        "question": "Question 5",
        "type": "Disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 5",
        "type": "Neither agree nor disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 5",
        "type": "Agree",
        "value": 5,
        "percentage": 83,
        "percentage_start": 0,
        "percentage_end": 83
      },
      {
        "question": "Question 5",
        "type": "Strongly agree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 83,
        "percentage_end": 83
      },

      {
        "question": "Question 6",
        "type": "Strongly disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": -17,
        "percentage_end": -17
      },
      {
        "question": "Question 6",
        "type": "Disagree",
        "value": 1,
        "percentage": 17,
        "percentage_start": 0,
        "percentage_end": -17
      },
      {
        "question": "Question 6",
        "type": "Neither agree nor disagree",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Question 6",
        "type": "Agree",
        "value": 4,
        "percentage": 66,
        "percentage_start": 0,
        "percentage_end": 66
      },
      {
        "question": "Question 6",
        "type": "Strongly agree",
        "value": 1,
        "percentage": 17,
        "percentage_start": 66,
        "percentage_end": 83
      }
])

color_scale = alt.Scale(
    domain=[
        "Strongly disagree",
        "Disagree",
        "Neither agree nor disagree",
        "Agree",
        "Strongly agree"
    ],
    range=["#c30d24", "#f3a583", "#cccccc", "#94c6da", "#1770ab"]
)

y_axis = alt.Axis(
    title='Question',
    offset=5,
    ticks=False,
    minExtent=60,
    domain=False
)


chart =alt.Chart(source,width=600,height=300).mark_bar().encode(
    x='percentage_start:Q',
    x2='percentage_end:Q',
    y=alt.Y('question:N', axis=y_axis),
    color=alt.Color(
        'type:N',
        legend=alt.Legend(title='Response',orient='top'),
        scale=color_scale,
    )
).configure_view(strokeWidth=0)

chart.show()
# chart.save('filename.pdf')