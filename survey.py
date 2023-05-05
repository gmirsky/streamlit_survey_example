import streamlit as st
import streamlit_survey as ss

# set up the session state
if 'num' not in st.session_state:
    st.session_state.num = 0
# remove the hamburger in the upper right hand corner and the Made with Streamlit footer
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Survey Example Using Streamlit")
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Online_Survey_Icon_or_logo.svg/256px-Online_Survey_Icon_or_logo.svg.png")
# set up the questions and choices
#
# This data could be read in from a file or database, but for this example
# we'll just hard code it.
q = [
    (
        'multiselect',
        'What brands of toothpaste have you used? (You can choose more than one.)',
        [
            'Crest',
            'Colgate',
            'Aim',
            'Aquafresh',
            'Close-Up',
            'Crest',
            'Mentadent',
            'Pepsodent',
            'Sensodyne',
            'Tom\'s of Maine',
            'Ultrabrite',
            'Arm & Hammer',
            'Rembrandt',
            'Natural White',
            'Tartar Control',
            'Other'
        ]
    ),
    (
        'selectbox',
        'What is your favorite brand of mouthwash?',
        [
            'None',
            'Listerine',
            'Scope',
            'Act',
            'Crest',
            'Plax',
            'Another brand not listed here'
        ]
    ),
    (
        'slider',
        'How many times a year do you vist the dentist year?',
        0,
        52,
        0
    ),
    (
        'radio',
        'Do you have dental insurance?',
        ['Yes', 'No']
    ),
    (
        'dateinput',
        'What was the date of your last dental visit?'
    ),
    (
        'checkbox',
        'I acknowledge my responses are true.'
    )
]


# main function
#
# The nested if can be replaced with a function that returns the appropriate
# question value but I didn't want to add another layer of complexity to the
# example code where there was a dependent question.
#


def main():
    # create the survey object
    survey = ss.StreamlitSurvey("Survey example using Streamlit")
    # create the pages
    pages = survey.pages(3, on_submit=lambda:
                         st.success(
                             "Your responses have been recorded. Thank you!"
                         )
                         )
    # loop through the pages
    with pages:
        if pages.current == 0:  # first page presented to the user
            # question one on the first page presented to the user
            if q[0][0] == 'radio':
                p0q1 = survey.radio(q[0][1], options=q[0][2])
            elif q[0][0] == 'multiselect':
                p0q1 = survey.multiselect(
                    q[0][1], options=q[0][2]
                )
            elif q[0][0] == 'selectbox':
                p0q1 = survey.selectbox(
                    q[0][1], options=q[0][2])
            elif q[0][0] == 'checkbox':
                p0q1 = survey.checkbox(q[0][1])
            elif q[0][0] == 'text_input':
                p0q1 = survey.text_input(q[0][1])
            elif q[0][0] == 'number_input':
                p0q1 = survey.number_input(
                    q[0][1], min_value=q[0][2], max_value=q[0][3], value=q[0][4])
            elif q[0][0] == 'slider':
                p0q1 = survey.slider(
                    q[0][1], min_value=q[0][2], max_value=q[0][3], value=q[0][4])
            elif q[0][0] == 'dateinput':
                p0q1 = survey.dateinput(q[0][1])

            # question two on the first page presented to the user
            if q[1][0] == 'radio':
                p0q2 = survey.radio(q[1][1], options=q[1][2])
            elif q[1][0] == 'multiselect':
                p0q2 = survey.multiselect(
                    q[1][1], options=q[1][2])
            elif q[1][0] == 'selectbox':
                p0q2 = survey.selectbox(
                    q[1][1], options=q[1][2])
            elif q[1][0] == 'checkbox':
                p0q2 = survey.checkbox(q[1][1])
            elif q[1][0] == 'text_input':
                p0q2 = survey.text_input(q[1][1])
            elif q[1][0] == 'number_input':
                p0q2 = survey.number_input(
                    q[1][1], min_value=q[1][2], max_value=q[1][3], value=q[1][4])
            elif q[1][0] == 'slider':
                p0q2 = survey.slider(
                    q[1][1], min_value=q[1][2], max_value=q[1][3], value=q[1][4])
            elif q[1][0] == 'dateinput':
                p0q2 = survey.dateinput(q[1][1])

        elif pages.current == 1:  # second page presented to the user
            # question one on the second page presented to the user
            if q[2][0] == 'radio':
                p1q1 = survey.radio(q[1][1], options=q[2][2])
            elif q[2][0] == 'multiselect':
                p1q1 = survey.multiselect(
                    q[2][1], options=q[2][2])
            elif q[2][0] == 'selectbox':
                p1q1 = survey.selectbox(
                    q[2][1], options=q[2][2])
            elif q[2][0] == 'checkbox':
                p1q1 = survey.checkbox(q[2][1])
            elif q[2][0] == 'text_input':
                p1q1 = survey.text_input(q[2][1])
            elif q[2][0] == 'number_input':
                p1q1 = survey.number_input(
                    q[2][1], min_value=q[2][2], max_value=q[2][3], value=q[2][4])
            elif q[2][0] == 'slider':
                p1q1 = survey.slider(
                    q[2][1], min_value=q[2][2], max_value=q[2][3], value=q[2][4])
                if p1q1 > 0:
                    # Let's ask the user about their last dental visit if they
                    # answered that they had a dental visit in the last year.
                    #
                    # This is a demonstration of a dependent question
                    p1q3 = survey.dateinput(q[4][1])
            elif q[2][0] == 'dateinput':
                p1q1 = survey.dateinput(q[2][1], )

            # question two on the second page presented to the user
            if q[3][0] == 'radio':
                p1q2 = survey.radio(q[3][1], options=q[3][2])
            elif q[3][0] == 'multiselect':
                p1q2 = survey.multiselect(q[3][1], options=q[3][2])
            elif q[3][0] == 'selectbox':
                p1q2 = survey.selectbox(
                    q[3][1], options=q[3][2])
            elif q[3][0] == 'checkbox':
                p1q2 = survey.checkbox(q[3][1])
            elif q[3][0] == 'text_input':
                p1q2 = survey.text_input(q[3][1])
            elif q[3][0] == 'number_input':
                p1q2 = survey.number_input(
                    q[3][1], min_value=q[3][2], max_value=q[3][3], value=q[3][4])
            elif q[3][0] == 'slider':
                p1q2 = survey.slider(
                    q[3][1], min_value=q[3][2], max_value=q[3][3], value=q[3][4])
            elif q[3][0] == 'dateinput':
                p1q2 = survey.dateinput(q[3][1])

        elif pages.current == 2:  # third page presented to the user
            # question one on the third page presented to the user
            if q[5][0] == 'radio':
                p2q1 = survey.radio(q[5][1], options=q[5][2])
            elif q[5][0] == 'multiselect':
                p2q1 = survey.multiselect(
                    q[5][1], options=q[5][2])
            elif q[5][0] == 'selectbox':
                p2q1 = survey.selectbox(
                    q[5][1], options=q[5][2])
            elif q[5][0] == 'checkbox':
                p2q1 = survey.checkbox(q[5][1])
            elif q[5][0] == 'text_input':
                p2q1 = survey.text_input(q[5][1])
            elif q[5][0] == 'number_input':
                p2q1 = survey.number_input(
                    q[5][1], min_value=q[5][2], max_value=q[5][3], value=q[5][4])
            elif q[5][0] == 'slider':
                p2q1 = survey.slider(
                    q[5][1], min_value=q[5][2], max_value=q[5][3], value=q[5][4])
            elif q[5][0] == 'dateinput':
                p2q1 = survey.dateinput(q[5][1])

    # Disolay the data captured from the survey
    st.write("This is the data captured from the survey")
    st.json(survey.to_json())


if __name__ == "__main__":
    main()
