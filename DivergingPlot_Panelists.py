import altair as alt
alt.renderers.enable('altair_viewer')

# Poor = [0.0,8.9,12.5,12.5,0.0,10.7]
# Fair =[25.0,12.5,12.5,12.5,0.0,21.4]
# Satisfactory = [0.0,30.4,0.0,17.9,37.5,28.6]
# Very_Good = [62.5,25.0,50.0,32.1,50.0,19.6]
# Excellent =[12.5,23.2,25.0,25.0,12.5,19.6]

# 	                                            	Poor =1	Fair =2	Satisfactory =3	Very good =4	Excellent=5
# Control	Clerity of Codebase of regular developement	10.7	21.4	28.6	19.6	19.6
# Microasking	Clerity of codebase of microtask programming	0.0	0.0	37.5	50.0	12.5

# 	Simplicity of Codebase of regular developement	8.9	12.5	30.4	25.0	23.2
# 	Simplicity of codebase of microtask programming	0.0	25.0	0.0	62.5	12.5

# 	Consistency of Codebase of regular developement	12.5	12.5	17.9	32.1	25.0
# 	Consistency  of codebase of microtask programming	12.5	12.5	0.0	50.0	25.0
# { "order": 1,
#     "question": "-",
#     "type": "Poor",
#     "value": 0,
#     "percentage": 0,
#     "percentage_start": 0,
#     "percentage_end": 0
# },
# { "order": 1,
#     "question": "-",
#     "type": "Fair",
#     "value": 0,
#     "percentage": 0,
#     "percentage_start": 0,
#     "percentage_end": 0
# },
# { "order": 1,
#     "question": "-",
#     "type": "Satisfactory",
#     "value": 0,
#     "percentage": 0,
#     "percentage_start": 0,
#     "percentage_end": 0
# },
# { "order": 1,
#     "question": "-",
#     "type": "Very Good",
#     "value": 0,
#     "percentage": 0,
#     "percentage_start": 0,
#     "percentage_end": 0
# },
# { "order": 1,
#     "question": "-",
#     "type": "Excellent",
#     "value": 0,
#     "percentage": 0,
#     "percentage_start": 0,
#     "percentage_end": 0
# },

source = alt.pd.DataFrame([

      { "order": 1,
        "question": "Clarity (C)",
        "type": "Poor",
        "value": 10.7,
        "percentage": 10.7,
        "percentage_start": -32.1,
        "percentage_end": -21.4
      },
      { "order": 1, "order": 1,
        "question": "Clarity (C)",
        "type": "Fair",
        "value": 21.4,
        "percentage": 21.4,
        "percentage_start": -21.4,
        "percentage_end": 0
      },
      { "order": 1, "order": 1,
        "question": "Clarity (C)",
        "type": "Satisfactory",
        "value": 28.6,
        "percentage":28.6,
        "percentage_start": 0,
        "percentage_end": 28.6
      },
      { "order": 1,
        "question": "Clarity (C)",
        "type": "Very Good",
        "value": 19.6,
        "percentage": 19.6,
        "percentage_start": 28.6,
        "percentage_end": 48.2
      },
      { "order": 1,
        "question": "Clarity (C)",
        "type": "Excellent",
        "value": 19.6,
        "percentage": 19.6,
        "percentage_start": 48.2,
        "percentage_end": 67.8
      },

      { "order": 1,
        "question": "Clarity (E)",
        "type": "Poor",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      { "order": 1,
        "question": "Clarity (E)",
        "type": "Fair",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      { "order": 1,
        "question": "Clarity (E)",
        "type": "Satisfactory",
        "value": 37.5,
        "percentage": 37.5,
        "percentage_start": 0,
        "percentage_end": 37.5
      },
      { "order": 1,
        "question": "Clarity (E)",
        "type": "Very Good",
        "value": 50,
        "percentage": 50,
        "percentage_start": 37.5,
        "percentage_end": 87.5
      },
      { "order": 1,
        "question": "Clarity (E)",
        "type": "Excellent",
        "value": 12.5,
        "percentage": 12.5,
        "percentage_start": 87.5,
        "percentage_end": 100
      },



      { "order": 1,
        "question": "Consistency (C)",
        "type": "Poor",
        "value": 12.5,
        "percentage": 12.5,
        "percentage_start": -12.5,
        "percentage_end": -25
      },
      { "order": 1,
        "question": "Consistency (C)",
        "type": "Fair",
        "value": 12.5,
        "percentage": 12.5,
        "percentage_start": 0,
        "percentage_end": -12.5
      },
      { "order": 1,
        "question": "Consistency (C)",
        "type": "Satisfactory",
        "value": 17.9,
        "percentage": 17.9,
        "percentage_start": 0,
        "percentage_end": 17.9
      },
      { "order": 1,
        "question": "Consistency (C)",
        "type": "Very Good",
        "value": 32.1,
        "percentage": 32.1,
        "percentage_start": 17.9,
        "percentage_end": 50
      },
      { "order": 1,
        "question": "Consistency (C)",
        "type": "Excellent",
        "value": 25,
        "percentage": 25,
        "percentage_start": 50,
        "percentage_end": 75
      },

      { "order": 2,
        "question": "Consistency (E)",
        "type": "Poor",
        "value": 12.5,
        "percentage":  12.5,
        "percentage_start": - 12.5,
        "percentage_end": -25
      },
      { "order": 2,
        "question": "Consistency (E)",
        "type": "Fair",
        "value":  12.5,
        "percentage":  12.5,
        "percentage_start": 0,
        "percentage_end": -12.5
      },
      { "order": 2,
        "question": "Consistency (E)",
        "type": "Satisfactory",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      { "order": 2,
        "question": "Consistency (E)",
        "type": "Very Good",
        "value": 50,
        "percentage": 50,
        "percentage_start": 0,
        "percentage_end": 50
      },
      { "order": 2,
        "question": "Consistency (E)",
        "type": "Excellent",
        "value": 25,
        "percentage": 25,
        "percentage_start": 50,
        "percentage_end": 75
      },

      { "order": 1,
        "question": "Simplicity (C)",
        "type": "Poor",
        "value": 8.9,
        "percentage": 8.9,
        "percentage_start": -12.5,
        "percentage_end": -21.4
      },
      { "order": 1,
        "question": "Simplicity (C)",
        "type": "Fair",
        "value": 12.5,
        "percentage": 12.5,
        "percentage_start": 0,
        "percentage_end": -12.5
      },
      { "order": 1,
        "question": "Simplicity (C)",
        "type": "Satisfactory",
        "value": 30.4,
        "percentage": 30.4,
        "percentage_start": 0,
        "percentage_end": 30.4
      },
      { "order": 1,
        "question": "Simplicity (C)",
        "type": "Very Good",
        "value": 25,
        "percentage": 25,
        "percentage_start": 30.4,
        "percentage_end": 55.4
      },
      { "order": 1,
        "question": "Simplicity (C)",
        "type": "Excellent",
        "value": 23.2,
        "percentage": 23.2,
        "percentage_start": 55.4,
        "percentage_end":78.6
      },

      { "order": 1,
        "question": "Simplicity (E)",
        "type": "Poor",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      { "order": 1,
        "question": "Simplicity (E)",
        "type": "Fair",
        "value": 25,
        "percentage": 25,
        "percentage_start": 0,
        "percentage_end": -25
      },
      { "order": 1,
        "question": "Simplicity (E)",
        "type": "Satisfactory",
        "value": 0,
        "percentage": 0,
        "percentage_start": 0,
        "percentage_end": 0
      },
      { "order": 1,
        "question": "Simplicity (E)",
        "type": "Very Good",
        "value": 62.5,
        "percentage": 62.5,
        "percentage_start": 0,
        "percentage_end": 62.5
      },
      { "order": 1,
        "question": "Simplicity (E)",
        "type": "Excellent",
        "value": 12.5,
        "percentage": 12.5,
        "percentage_start": 62.5,
        "percentage_end": 75
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
    range=["#ff6361", "#ffa600", "#bc5090", "#58508d", "#003f5c"]
)

y_axis = alt.Axis( title='', offset=5, ticks=False,  minExtent=60,    domain=False)


chart =alt.Chart(source,width=600,height=300).mark_bar().encode(x='percentage_start:Q',x2='percentage_end:Q', y=alt.Y('question:N', axis=y_axis),
                                                                color=alt.Color( 'type:N', legend=alt.Legend(title='',orient='top'), scale=color_scale,
                                                                                 )).properties(title='Quality of code of control (C) and experimental (E) groups').configure_view(strokeWidth=0)
    # .configure_axis(labelFontSize=20,  titleFontSize=20).configure_title(fontSize=20)

chart.show()
# chart.save('filename.pdf')