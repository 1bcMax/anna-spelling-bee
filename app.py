"""
Anna's Spelling Bee Study Buddy
Presidential AI Challenge - Track II
"""

import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="Anna's Spelling Bee Buddy",
    page_icon="🐝",
    layout="centered"
)

# Anna's 50 spelling words organized by grade level
# Each word includes part of speech and language of origin (like in a real spelling bee)
WORD_LIST = [
    # 1st Grade
    {"word": "twigs", "definition": "A slender woody shoot growing from a branch or stem of a tree or shrub", "grade": "1st", "origin": "English", "part_of_speech": "noun"},
    {"word": "close", "definition": "A short distance away or apart in space or time, in close proximity", "grade": "1st", "origin": "Latin", "part_of_speech": "adjective"},
    {"word": "tackle", "definition": "Make determined efforts to deal with a problem or difficult task", "grade": "1st", "origin": "German", "part_of_speech": "verb"},
    {"word": "scrunch", "definition": "Make a loud crunching noise, crush or squeeze into a compact mass", "grade": "1st", "origin": "English", "part_of_speech": "verb"},
    {"word": "cozy", "definition": "Giving a feeling of comfort, warmth, and relaxation", "grade": "1st", "origin": "Norwegian", "part_of_speech": "adjective"},

    # 2nd Grade
    {"word": "shortcut", "definition": "A shorter alternative route, an accelerated way of doing or achieving something", "grade": "2nd", "origin": "English", "part_of_speech": "noun"},
    {"word": "minnows", "definition": "A small freshwater fish that typically forms large shoals", "grade": "2nd", "origin": "English", "part_of_speech": "noun"},
    {"word": "moment", "definition": "A very brief period of time, a particular stage in something's development", "grade": "2nd", "origin": "Latin", "part_of_speech": "noun"},
    {"word": "ajar", "definition": "Slightly open", "grade": "2nd", "origin": "English", "part_of_speech": "adjective"},
    {"word": "baffling", "definition": "Impossible to understand, perplexing", "grade": "2nd", "origin": "Scottish", "part_of_speech": "adjective"},

    # 3rd Grade
    {"word": "unicorn", "definition": "A mythical animal typically represented as a horse with a single straight horn projecting from its forehead", "grade": "3rd", "origin": "Latin", "part_of_speech": "noun"},
    {"word": "streetlights", "definition": "A light illuminating a road, typically mounted on a tall pole", "grade": "3rd", "origin": "English", "part_of_speech": "noun"},
    {"word": "journey", "definition": "An act of traveling from one place to another", "grade": "3rd", "origin": "French", "part_of_speech": "noun"},
    {"word": "attacked", "definition": "Take aggressive action against with weapons or armed force", "grade": "3rd", "origin": "French", "part_of_speech": "verb"},
    {"word": "gorgeous", "definition": "Beautiful, very attractive", "grade": "3rd", "origin": "French", "part_of_speech": "adjective"},

    # 4th Grade
    {"word": "scorcher", "definition": "A day or period of very hot weather, a remarkable or extreme example of something", "grade": "4th", "origin": "English", "part_of_speech": "noun"},
    {"word": "moustache", "definition": "A strip of hair left to grow above the upper lip", "grade": "4th", "origin": "French", "part_of_speech": "noun"},
    {"word": "artifacts", "definition": "An object made by a human being, typically an item of cultural or historical interest", "grade": "4th", "origin": "Latin", "part_of_speech": "noun"},
    {"word": "discoveries", "definition": "The action or process of discovering or being discovered", "grade": "4th", "origin": "Latin", "part_of_speech": "noun"},
    {"word": "prognosis", "definition": "The likely course of a disease or ailment", "grade": "4th", "origin": "Greek", "part_of_speech": "noun"},
    {"word": "paltry", "definition": "Small or meager, petty, trivial", "grade": "4th", "origin": "German", "part_of_speech": "adjective"},

    # 5th Grade
    {"word": "oblivion", "definition": "The state of being unaware or unconscious of what is happening, the state of being forgotten", "grade": "5th", "origin": "Latin", "part_of_speech": "noun"},
    {"word": "reprimanding", "definition": "A rebuke, especially an official one", "grade": "5th", "origin": "Latin", "part_of_speech": "verb"},
    {"word": "bracken", "definition": "A tall fern with coarse lobed fronds, which occurs worldwide and can cover large areas", "grade": "5th", "origin": "Scandinavian", "part_of_speech": "noun"},
    {"word": "conjure", "definition": "Call upon to appear, by means of a magic ritual", "grade": "5th", "origin": "Latin", "part_of_speech": "verb"},
    {"word": "hypnosis", "definition": "The induction of a state of consciousness in which a person loses the power of voluntary action", "grade": "5th", "origin": "Greek", "part_of_speech": "noun"},
    {"word": "rotunda", "definition": "A round building or room, especially one with a dome", "grade": "5th", "origin": "Latin", "part_of_speech": "noun"},

    # 6th Grade
    {"word": "tranquilizer", "definition": "A medicinal drug taken to reduce tension or anxiety", "grade": "6th", "origin": "Latin", "part_of_speech": "noun"},
    {"word": "equestrian", "definition": "Relating to horse riding, depicting or representing a person on horseback", "grade": "6th", "origin": "Latin", "part_of_speech": "adjective"},
    {"word": "stucco", "definition": "Fine plaster used for coating wall surfaces or molding into architectural decorations", "grade": "6th", "origin": "Italian", "part_of_speech": "noun"},
    {"word": "talcum", "definition": "A cosmetic or toilet preparation consisting of the mineral talc in powdered form", "grade": "6th", "origin": "Arabic", "part_of_speech": "noun"},
    {"word": "chartreuse", "definition": "A pale green or yellow liqueur made from brandy and aromatic herbs", "grade": "6th", "origin": "French", "part_of_speech": "noun"},
    {"word": "serape", "definition": "A shawl or blanket worn as a cloak in Latin America", "grade": "6th", "origin": "Spanish", "part_of_speech": "noun"},

    # 7th Grade
    {"word": "Nehru", "definition": "An Indian statesman, prime minister 1947-1964, father of Indira Gandhi", "grade": "7th", "origin": "Hindi", "part_of_speech": "proper noun"},
    {"word": "wainscoting", "definition": "Wooden paneling that lines the lower part of the walls of a room", "grade": "7th", "origin": "Dutch", "part_of_speech": "noun"},
    {"word": "compassionate", "definition": "Feeling or showing sympathy and concern for others", "grade": "7th", "origin": "Latin", "part_of_speech": "adjective"},
    {"word": "amicable", "definition": "Having a spirit of friendliness, without serious disagreement or rancor", "grade": "7th", "origin": "Latin", "part_of_speech": "adjective"},
    {"word": "discipline", "definition": "The practice of training people to obey rules or a code of behavior", "grade": "7th", "origin": "Latin", "part_of_speech": "noun"},
    {"word": "dignitaries", "definition": "A person considered to be important because of high rank or office", "grade": "7th", "origin": "Latin", "part_of_speech": "noun"},

    # 8th Grade
    {"word": "lye", "definition": "A strongly alkaline solution, especially of potassium hydroxide, used for washing or cleansing", "grade": "8th", "origin": "English", "part_of_speech": "noun"},
    {"word": "belfry", "definition": "The part of a bell tower or steeple in which bells are housed", "grade": "8th", "origin": "French", "part_of_speech": "noun"},
    {"word": "mercantile", "definition": "Relating to trade or commerce, commercial", "grade": "8th", "origin": "Italian", "part_of_speech": "adjective"},
    {"word": "ostracism", "definition": "Exclusion from a society or group", "grade": "8th", "origin": "Greek", "part_of_speech": "noun"},
    {"word": "hyperventilation", "definition": "Breathe at an abnormally rapid rate, increasing the rate of carbon dioxide loss", "grade": "8th", "origin": "Greek", "part_of_speech": "noun"},
    {"word": "au revoir", "definition": "Goodbye until we meet again", "grade": "8th", "origin": "French", "part_of_speech": "interjection"},

    # Additional Challenge Words
    {"word": "Aubusson", "definition": "A kind of French tapestry or carpet, principally from the 18th century", "grade": "Challenge", "origin": "French", "part_of_speech": "noun"},
    {"word": "Charolais", "definition": "One of a breed of large white beef cattle", "grade": "Challenge", "origin": "French", "part_of_speech": "noun"},
    {"word": "Kilimanjaro", "definition": "An extinct volcano in northern Tanzania", "grade": "Challenge", "origin": "Swahili", "part_of_speech": "proper noun"},
    {"word": "bursitis", "definition": "Inflammation of a bursa, typically one in the knee, elbow or shoulder", "grade": "Challenge", "origin": "Latin", "part_of_speech": "noun"},
    {"word": "Oswego", "definition": "An industrial port city in north central New York", "grade": "Challenge", "origin": "Iroquois", "part_of_speech": "proper noun"},
]

# Initialize session state
if "current_word" not in st.session_state:
    st.session_state.current_word = None
if "score" not in st.session_state:
    st.session_state.score = 0
if "total" not in st.session_state:
    st.session_state.total = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "wrong_words" not in st.session_state:
    st.session_state.wrong_words = []
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False
if "session_history" not in st.session_state:
    st.session_state.session_history = []
if "grade_filter" not in st.session_state:
    st.session_state.grade_filter = "All"
# Track which clues have been revealed (like in a real spelling bee)
if "show_origin" not in st.session_state:
    st.session_state.show_origin = False
if "show_part_of_speech" not in st.session_state:
    st.session_state.show_part_of_speech = False

def get_hint(word_data, hint_num):
    """Generate progressive hints"""
    word = word_data["word"]
    origin = word_data.get("origin", "unknown")

    if hint_num == 1:
        return f"Origin: {origin}"
    elif hint_num == 2:
        return f"The word has {len(word)} letters"
    elif hint_num == 3:
        # Show first and last letter
        if len(word) > 2:
            return f"Starts with '{word[0].upper()}' and ends with '{word[-1].upper()}'"
        return f"Starts with '{word[0].upper()}'"

def get_new_word():
    """Get a random word based on filter"""
    if st.session_state.grade_filter == "All":
        words = WORD_LIST
    else:
        words = [w for w in WORD_LIST if w["grade"] == st.session_state.grade_filter]

    if words:
        st.session_state.current_word = random.choice(words)
        st.session_state.attempts = 0
        st.session_state.show_answer = False
        # Reset clue states for new word
        st.session_state.show_origin = False
        st.session_state.show_part_of_speech = False

def check_answer(user_answer):
    """Check if the answer is correct"""
    if st.session_state.current_word is None:
        return

    correct_word = st.session_state.current_word["word"].lower().strip()
    user_word = user_answer.lower().strip()

    if user_word == correct_word:
        st.session_state.score += 1
        st.session_state.total += 1
        st.success(f"Correct! Great job!")
        st.balloons()
        st.session_state.current_word = None
    else:
        st.session_state.attempts += 1
        if st.session_state.attempts >= 3:
            st.error(f"The correct spelling is: **{st.session_state.current_word['word']}**")
            st.session_state.total += 1
            if st.session_state.current_word["word"] not in st.session_state.wrong_words:
                st.session_state.wrong_words.append(st.session_state.current_word["word"])
            st.session_state.show_answer = True
        else:
            remaining = 3 - st.session_state.attempts
            st.warning(f"Not quite! {remaining} tries left.")
            hint = get_hint(st.session_state.current_word, st.session_state.attempts)
            st.info(f"Hint: {hint}")

# Main UI
st.title("🐝 Anna's Spelling Bee Buddy")
st.markdown("*Presidential AI Challenge Project*")

# Sidebar
with st.sidebar:
    st.header("Settings")

    grades = ["All", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "Challenge"]
    st.session_state.grade_filter = st.selectbox("Grade Level", grades)

    st.divider()

    st.header("Your Score")
    if st.session_state.total > 0:
        accuracy = (st.session_state.score / st.session_state.total) * 100
        st.metric("Correct", f"{st.session_state.score}/{st.session_state.total}")
        st.progress(accuracy / 100)
        st.caption(f"{accuracy:.0f}% accuracy")
    else:
        st.caption("Start practicing to see your score!")

    st.divider()

    if st.session_state.wrong_words:
        st.header("Words to Practice")
        for word in st.session_state.wrong_words[-5:]:
            st.markdown(f"- {word}")

    st.divider()

    if st.button("Reset Score"):
        st.session_state.score = 0
        st.session_state.total = 0
        st.session_state.wrong_words = []
        st.rerun()

# Main area
col1, col2 = st.columns([3, 1])

with col1:
    if st.button("🎯 New Word", type="primary", use_container_width=True):
        get_new_word()
        st.rerun()

with col2:
    word_count = len(WORD_LIST) if st.session_state.grade_filter == "All" else len([w for w in WORD_LIST if w["grade"] == st.session_state.grade_filter])
    st.caption(f"{word_count} words")

# Show current word
if st.session_state.current_word:
    st.divider()

    word_data = st.session_state.current_word

    st.markdown(f"### Grade: {word_data['grade']}")
    st.markdown(f"**Definition:** {word_data['definition']}")

    # Spelling bee clue buttons (like in a real spelling bee!)
    st.markdown("**Ask for a clue:**")
    clue_col1, clue_col2 = st.columns(2)

    with clue_col1:
        if st.session_state.show_part_of_speech:
            st.info(f"📝 Part of Speech: **{word_data.get('part_of_speech', 'unknown')}**")
        else:
            if st.button("Part of Speech?", use_container_width=True):
                st.session_state.show_part_of_speech = True
                st.rerun()

    with clue_col2:
        if st.session_state.show_origin:
            st.info(f"🌍 Language of Origin: **{word_data.get('origin', 'unknown')}**")
        else:
            if st.button("Language of Origin?", use_container_width=True):
                st.session_state.show_origin = True
                st.rerun()

    st.markdown("")  # spacing

    if not st.session_state.show_answer:
        user_input = st.text_input("Spell the word:", key="spell_input", placeholder="Type your answer here...")

        if st.button("Check Answer", type="primary"):
            if user_input:
                check_answer(user_input)
                st.rerun()
            else:
                st.warning("Please type a word first!")
    else:
        if st.button("Next Word"):
            get_new_word()
            st.rerun()

else:
    st.divider()
    st.markdown("### Welcome!")
    st.markdown("Click **New Word** to start practicing your spelling!")
    st.markdown("")
    st.markdown("**How it works:**")
    st.markdown("1. Read the definition")
    st.markdown("2. Ask for clues (just like in a real spelling bee!):")
    st.markdown("   - **Part of Speech** - Is it a noun, verb, adjective?")
    st.markdown("   - **Language of Origin** - Where does the word come from?")
    st.markdown("3. Type the correct spelling")
    st.markdown("4. Get hints if you need help")
    st.markdown("5. Track your progress!")

# Footer
st.divider()
st.caption("Built by Anna for the Presidential AI Challenge 2026")
