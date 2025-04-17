import streamlit as st
import time
from datetime import datetime

# Initialize session state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Questions
questions = [
    {
        "question": "What does the 'yield' keyword do in Python?",
        "options": ["Returns a value", "Creates a generator", "Throws an error", "Initializes a loop"],
        "answer": "Creates a generator"
    },
    {
        "question": "What is the output of: type(lambda x: x)?",
        "options": ["function", "<class 'function'>", "lambda", "callable"],
        "answer": "<class 'function'>"
    },
    {
        "question": "Which of these is not a valid Python data type?",
        "options": ["List", "Tuple", "Dictionary", "Array"],
        "answer": "Array"
    },
    {
        "question": "How do you create a virtual environment in Python 3?",
        "options": ["python -m venv env", "pip install virtual", "python3 venv", "create env"],
        "answer": "python -m venv env"
    },
    {
        "question": "Which built-in module can handle serialization in Python?",
        "options": ["os", "pickle", "datetime", "math"],
        "answer": "pickle"
    },
    {
        "question": "What is the correct way to open a file for writing in Python?",
        "options": ["open('file.txt')", "open('file.txt', 'r')", "open('file.txt', 'w')", "open('file.txt', 'a')"],
        "answer": "open('file.txt', 'w')"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["catch", "error", "handle", "try"],
        "answer": "try"
    },
    {
        "question": "What does the __init__() function do?",
        "options": ["Starts a loop", "Creates a new module", "Initializes a class", "Destroys an object"],
        "answer": "Initializes a class"
    },
    {
        "question": "Which module in Python is used for regular expressions?",
        "options": ["string", "re", "regex", "match"],
        "answer": "re"
    },
    {
        "question": "What is the result of 2 ** 3 ** 2?",
        "options": ["512", "64", "36", "256"],
        "answer": "512"
    },
    {
        "question": "Which of these is a mutable type?",
        "options": ["tuple", "str", "int", "list"],
        "answer": "list"
    },
    {
        "question": "Which statement is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "How do you import a module named 'math'?",
        "options": ["include math", "using math", "import math", "require math"],
        "answer": "import math"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".py", ".pt", ".pyt", ".python"],
        "answer": ".py"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["/", "//", "%", "**"],
        "answer": "//"
    },
    {
        "question": "What does len() function return?",
        "options": ["Number of elements", "Sum", "Index", "Range"],
        "answer": "Number of elements"
    },
    {
        "question": "How do you declare a comment in Python?",
        "options": ["// comment", "# comment", "/* comment */", "-- comment"],
        "answer": "# comment"
    },
    {
        "question": "Which function is used to convert a string to an integer?",
        "options": ["float()", "int()", "str()", "chr()"],
        "answer": "int()"
    },
    {
        "question": "What is a correct syntax to create a class?",
        "options": ["class MyClass()", "define MyClass", "MyClass = class", "class MyClass:"],
        "answer": "class MyClass:"
    },
    {
        "question": "Which method is used to add an element to a list?",
        "options": ["add()", "append()", "insert()", "push()"],
        "answer": "append()"
    }
]

def main():
    st.title("🎓 Personal Python Quiz")
    st.markdown("#### Advanced Python MCQ Quiz (20 Questions, 20 Minutes)")

    # Starting quiz if not started
    if not st.session_state.quiz_started:
        user_name = st.text_input("👤 Enter your name:")
        if user_name:
            st.session_state.user_name = user_name

        if st.session_state.user_name.strip() == "":
            st.warning("Please enter your name to start the quiz!")
            return

        if st.button("🚀 Start Quiz"):
            st.session_state.quiz_started = True
            st.session_state.start_time = time.time()

    # Quiz in progress
    elif st.session_state.quiz_started and not st.session_state.quiz_done:
        elapsed_time = int(time.time() - st.session_state.start_time)
        remaining_time = max(0, 1200 - elapsed_time)  # 20 minutes = 1200 seconds
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        st.info(f"⏱️ Time Left: {minutes:02d}:{seconds:02d}")

        if remaining_time <= 0:
            st.session_state.quiz_done = True

        if st.session_state.current_q < len(questions):
            q = questions[st.session_state.current_q]
            st.subheader(f"Q{st.session_state.current_q + 1}: {q['question']}")
            answer = st.radio("Select an option:", q["options"], key=f"q{st.session_state.current_q}")

            if st.button("Next"):
                if answer == q["answer"]:
                    st.session_state.score += 1
                st.session_state.current_q += 1
                if st.session_state.current_q >= len(questions):
                    st.session_state.quiz_done = True
        else:
            st.session_state.quiz_done = True

    # After quiz completion
    if st.session_state.quiz_done:
        st.success("✅ Quiz Completed!")
        st.subheader("📊 Results")
        st.write(f"**Name:** {st.session_state.user_name}")  # Here the name is displayed correctly now
        st.write(f"**Score:** {st.session_state.score} / {len(questions)}")

        elapsed_time = int(time.time() - st.session_state.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        st.write(f"**Time Taken:** {minutes:02d}:{seconds:02d}")

        st.markdown("---")
        st.subheader("🎉 Certificate of Completion")
        st.markdown(f"""
        <div style='border:2px solid #ccc; padding:20px; border-radius:10px; text-align:center;'>
            <h2>Certificate of Completion</h2>
            <p>This is to certify that</p>
            <h3>{st.session_state.user_name}</h3>
            <p>has successfully completed the</p>
            <b>Advanced Python Quiz</b>
            <p>with a score of <b>{st.session_state.score} / {len(questions)}</b> in <b>{minutes:02d}:{seconds:02d}</b>.</p>
            <p><i>Keep learning and growing! 🚀</i></p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
