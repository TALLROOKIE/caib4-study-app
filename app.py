import streamlit as st
import random

# Combined Flashcards data
flashcards = [
    ('Planning Process', 'The method of setting desired results and formulating ways to achieve them, combining top-down and bottom-up approaches.'),
    ('Top-down Approach', 'Management decides the mission, strategies, and objectives and informs business units to follow.'),
    ('Bottom-up Approach', 'Business units develop objectives and goals under the broad mission and strategy provided by management.'),
    ('Characteristics of a Plan', 'Four key characteristics: Simplicity, Practicality, Severability, Flexibility.'),
    ('Strategic Planning', 'A long-term plan to assess future impact, deal with business risks, and set strategies for 3-5 years.'),
    ('SWOT Analysis', 'A tool to match a business’s internal strengths and weaknesses to external opportunities and threats.'),
    ('Simplicity of a Plan', 'A plan should be easy to understand and communicate to ensure everyone can follow it.'),
    ('Practicality of a Plan', 'The plan should be realistic and achievable with the resources available.'),
    ('Severability of a Plan', 'A plan can be broken down into smaller, manageable sections that can be acted on independently.'),
    ('Flexibility of a Plan', 'A plan should be adaptable to changes in circumstances.')
]

# Combined Quiz Questions data
quiz_questions = [
    {
        'question': 'What are the four characteristics of a plan?',
        'options': ['Simplicity, Practicality, Innovation, Stability', 
                    'Simplicity, Practicality, Severability, Flexibility', 
                    'Flexibility, Complexity, Stability, Practicality'],
        'answer': 'Simplicity, Practicality, Severability, Flexibility'
    },
    {
        'question': 'What is the difference between a strategic plan and an action plan?',
        'options': ['Strategic plan is long-term, action plan is short-term', 
                    'Action plan is long-term, strategic plan is short-term', 
                    'They are the same'],
        'answer': 'Strategic plan is long-term, action plan is short-term'
    },
    {
        'question': 'What does a SWOT analysis stand for?',
        'options': ['Strengths, Weaknesses, Opportunities, Threats', 
                    'Strategies, Weaknesses, Objectives, Targets', 
                    'Successes, Weaknesses, Opportunities, Trends'],
        'answer': 'Strengths, Weaknesses, Opportunities, Threats'
    },
    {
        'question': 'What is meant by the simplicity of a plan?',
        'options': ['It should be easy to understand and communicate', 
                    'It should be complicated and detailed', 
                    'It should focus on long-term objectives only'],
        'answer': 'It should be easy to understand and communicate'
    },
    {
        'question': 'What is meant by the practicality of a plan?',
        'options': ['It should be achievable with the resources available', 
                    'It should be idealistic and visionary', 
                    'It should be focused on profit only'],
        'answer': 'It should be achievable with the resources available'
    },
    {
        'question': 'Identify one advantage of the top-down approach.',
        'options': ['Clear decision-making from management', 
                    'Encourages employee input', 
                    'Increases flexibility and creativity'],
        'answer': 'Clear decision-making from management'
    },
    {
        'question': 'Identify one advantage of the bottom-up approach.',
        'options': ['Employee involvement in decision-making', 
                    'Efficient and fast decisions', 
                    'Clear direction from management'],
        'answer': 'Employee involvement in decision-making'
    }
]

def main():
    st.title("CAIB 4 Interactive Study App")

    menu = ["Flashcards", "Quiz"]
    choice = st.sidebar.selectbox("Select Activity", menu)

    if choice == "Flashcards":
        st.header("Flashcards")
        if 'flashcard_index' not in st.session_state:
            st.session_state['flashcard_index'] = random.randint(0, len(flashcards) - 1)
            st.session_state['show_definition'] = False

        term, definition = flashcards[st.session_state['flashcard_index']]
        st.subheader(f"Term: {term}")

        if st.button("Show Definition"):
            st.session_state['show_definition'] = True

        if st.session_state['show_definition']:
            st.write(f"**Definition:** {definition}")

        if st.button("Next Flashcard"):
            st.session_state['flashcard_index'] = random.randint(0, len(flashcards) - 1)
            st.session_state['show_definition'] = False
            st.experimental_rerun()

    elif choice == "Quiz":
        st.header("Quiz")
        if 'quiz_index' not in st.session_state:
            st.session_state['quiz_index'] = random.randint(0, len(quiz_questions) - 1)
            st.session_state['answered'] = False

        quiz = quiz_questions[st.session_state['quiz_index']]
        question = quiz['question']
        options = quiz['options']
        answer = quiz['answer']
        st.subheader(f"Question: {question}")

        selected_option = st.radio("Options", options)

        if st.button("Submit Answer"):
            if selected_option == answer:
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer was: {answer}")
            st.session_state['answered'] = True

        if st.session_state.get('answered', False):
            if st.button("Next Question"):
                st.session_state['quiz_index'] = random.randint(0, len(quiz_questions) - 1)
                st.session_state['answered'] = False
                st.experimental_rerun()

if __name__ == '__main__':
    main()
Add Streamlit app code
