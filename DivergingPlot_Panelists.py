import altair as alt
alt.renderers.enable('altair_viewer')

# Poor = [0.0,8.9,12.5,12.5,0.0,10.7]
# Fair =[25.0,12.5,12.5,12.5,0.0,21.4]
# Satisfactory = [0.0,30.4,0.0,17.9,37.5,28.6]
# Very_Good = [62.5,25.0,50.0,32.1,50.0,19.6]
# Excellent =[12.5,23.2,25.0,25.0,12.5,19.6]

# 		Poor =1	Fair =2	Satisfactory =3	Very good =4	Excellent=5
# Control	Clerity of Codebase of regular developement	10.7	21.4	28.6	19.6	19.6
# 	Simplicity of Codebase of regular developement	8.9	12.5	30.4	25.0	23.2
# 	Consistency of Codebase of regular developement	12.5	12.5	17.9	32.1	25.0
# Microasking	Clerity of codebase of microtask programming	0.0	0.0	37.5	50.0	12.5
# 	Simplicity of codebase of microtask programming	0.0	25.0	0.0	62.5	12.5
# 	Consistency  of codebase of microtask programming	12.5	12.5	0.0	50.0	25.0
source = alt.pd.DataFrame([
      {
        "question": "Clarity (C)",
        "type": "Poor",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Clarity (C)",
        "type": "Fair",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Clarity (C)",
        "type": "Satisfactory",
        "value": 1,
        "percentage": 16,
        "percentage_start": -8,
        "percentage_end": 8
      },
      {
        "question": "Clarity (C)",
        "type": "Very Good",
        "value": 5,
        "percentage": 83,
        "percentage_start": 8,
        "percentage_end": 91
      },
      {
        "question": "Clarity (C)",
        "type": "Excellent",
        "value": 0,
        "percentage": 0,
        "percentage_start": 91,
        "percentage_end": 91
      },

      {
        "question": "Clarity (E)",
        "type": "Poor",
        "value": 1,
        "percentage": 16,
        "percentage_start": -49,
        "percentage_end": -33
      },
      {
        "question": "Clarity (E)",
        "type": "Fair",
        "value": 0,
        "percentage": 0,
        "percentage_start": -33,
        "percentage_end": -33
      },
      {
        "question": "Clarity (E)",
        "type": "Satisfactory",
        "value": 4,
        "percentage": 66,
        "percentage_start": -33,
        "percentage_end": 33
      },
      {
        "question": "Clarity (E)",
        "type": "Very Good",
        "value": 0,
        "percentage": 0,
        "percentage_start": 33,
        "percentage_end": 33
      },
      {
        "question": "Clarity (E)",
        "type": "Excellent",
        "value": 1,
        "percentage": 16,
        "percentage_start": 33,
        "percentage_end": 49
      },

      {
        "question": "Consistency (C)",
        "type": "Poor",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Consistency (C)",
        "type": "Fair",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Consistency (C)",
        "type": "Satisfactory",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Consistency (C)",
        "type": "Very Good",
        "value": 5,
        "percentage": 83,
        "percentage_start": 0,
        "percentage_end": 83
      },
      {
        "question": "Consistency (C)",
        "type": "Excellent",
        "value": 1,
        "percentage": 17,
        "percentage_start": 83,
        "percentage_end": 100
      },

      {
        "question": "Consistency (E)",
        "type": "Poor",
        "value": 1,
        "percentage": 17,
        "percentage_start": -58,
        "percentage_end": -75
      },
      {
        "question": "Consistency (E)",
        "type": "Fair",
        "value": 2,
        "percentage": 3,
        "percentage_start": -58,
        "percentage_end": -25
      },
      {
        "question": "Consistency (E)",
        "type": "Satisfactory",
        "value": 3,
        "percentage": 50,
        "percentage_start": -25,
        "percentage_end": 25
      },
      {
        "question": "Consistency (E)",
        "type": "Very Good",
        "value": 0,
        "percentage": 0,
        "percentage_start": 25,
        "percentage_end": 25
      },
      {
        "question": "Consistency (E)",
        "type": "Excellent",
        "value": 0,
        "percentage": 0,
        "percentage_start": 25,
        "percentage_end": 25
      },

      {
        "question": "Simplicity (C)",
        "type": "Poor",
        "value": 1,
        "percentage": 17,
        "percentage_start": 0,
        "percentage_end": -17
      },
      {
        "question": "Simplicity (C)",
        "type": "Fair",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Simplicity (C)",
        "type": "Satisfactory",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Simplicity (C)",
        "type": "Very Good",
        "value": 5,
        "percentage": 83,
        "percentage_start": 0,
        "percentage_end": 83
      },
      {
        "question": "Simplicity (C)",
        "type": "Excellent",
        "value": 0,
        "percentage": 0,
        "percentage_start": 83,
        "percentage_end": 83
      },

      {
        "question": "Simplicity (E)",
        "type": "Poor",
        "value": 0,
        "percentage": 0,
        "percentage_start": -17,
        "percentage_end": -17
      },
      {
        "question": "Simplicity (E)",
        "type": "Fair",
        "value": 1,
        "percentage": 17,
        "percentage_start": 0,
        "percentage_end": -17
      },
      {
        "question": "Simplicity (E)",
        "type": "Satisfactory",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      {
        "question": "Simplicity (E)",
        "type": "Very Good",
        "value": 4,
        "percentage": 66,
        "percentage_start": 0,
        "percentage_end": 66
      },
      {
        "question": "Simplicity (E)",
        "type": "Excellent",
        "value": 1,
        "percentage": 17,
        "percentage_start": 66,
        "percentage_end": 83
      }
])

color_scale = alt.Scale(
    domain=[
        "Poor",
        "Fair",
        "Satisfactory",
        "Very Good",
        "Excellent"
    ],
    range=["#c30d24", "#f3a583", "#cccccc", "#94c6da", "#1770ab"]
)

y_axis = alt.Axis(
    title='',
    offset=5,
    ticks=False,
    minExtent=60,
    domain=False
)


chart =alt.Chart(source).mark_bar().encode(
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