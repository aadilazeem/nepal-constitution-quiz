import streamlit as st
import pandas as pd
import random

# ===========================
# CONFIGURATION & CONSTANTS
# ===========================

class SYLLABUS_SECTIONS:
    LAW = "Law & Justice"
    ADMIN = "Public Administration"
    CONST = "Constitution"

LEVELS = ["Basic", "Medium", "Hard"]

# ===========================
# DATA: MCQ QUESTIONS
# ===========================

mcq_dataset = [
    # BASIC LEVEL
    {"id": 1, "section": SYLLABUS_SECTIONS.CONST, "question": "In whom is the sovereignty and state power of Nepal vested?", "options": {"A": "The President", "B": "The Parliament", "C": "The Nepali People", "D": "The Council of Ministers"}, "answer": "C", "details": "Article 2 of the Constitution states sovereignty is vested in the Nepali people.", "level": "Basic"},
    {"id": 2, "section": SYLLABUS_SECTIONS.CONST, "question": "What is the National Animal of Nepal according to the Constitution?", "options": {"A": "Tiger", "B": "Rhino", "C": "Cow (Gai)", "D": "Musk Deer"}, "answer": "C", "details": "Article 9(3) / Schedule-3.", "level": "Basic"},
    {"id": 3, "section": SYLLABUS_SECTIONS.CONST, "question": "Which Article guarantees the Right to Information (RTI)?", "options": {"A": "Article 16", "B": "Article 27", "C": "Article 33", "D": "Article 46"}, "answer": "B", "details": "Article 27 guarantees the right to demand and receive information.", "level": "Basic"},
    {"id": 4, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the standard retirement age for Civil Servants in Nepal?", "options": {"A": "55 Years", "B": "58 Years", "C": "60 Years", "D": "63 Years"}, "answer": "B", "details": "According to the Civil Service Act.", "level": "Basic"},
    {"id": 5, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Writ literally means 'Show me the body'?", "options": {"A": "Mandamus", "B": "Certiorari", "C": "Quo Warranto", "D": "Habeas Corpus"}, "answer": "D", "details": "Used to secure the release of an unlawfully detained person.", "level": "Basic"},
    {"id": 6, "section": SYLLABUS_SECTIONS.CONST, "question": "What is the maximum number of Justices in the Supreme Court (excluding CJ)?", "options": {"A": "15", "B": "20", "C": "21", "D": "25"}, "answer": "B", "details": "Article 129 states a maximum of 20 Justices in addition to the Chief Justice.", "level": "Basic"},
    {"id": 7, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Who chairs the National Planning Commission (NPC) of Nepal?", "options": {"A": "Finance Minister", "B": "Chief Secretary", "C": "Prime Minister", "D": "President"}, "answer": "C", "details": "The Prime Minister is the Chairperson of the NPC.", "level": "Basic"},
    {"id": 8, "section": SYLLABUS_SECTIONS.LAW, "question": "What kind of law deals with offenses against the state and results in punishment?", "options": {"A": "Civil Law", "B": "Criminal Law", "C": "Family Law", "D": "Contract Law"}, "answer": "B", "details": "Criminal law focuses on punishment for offenses.", "level": "Basic"},
    {"id": 9, "section": SYLLABUS_SECTIONS.CONST, "question": "The Executive Power of Nepal is vested in whom?", "options": {"A": "The President", "B": "The Council of Ministers", "C": "The Parliament", "D": "The Supreme Court"}, "answer": "B", "details": "Article 75 vests executive power in the Council of Ministers.", "level": "Basic"},
    {"id": 10, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the document defining services, time limits, and fees for a public office?", "options": {"A": "Office Manual", "B": "Citizen Charter", "C": "Constitution", "D": "Annual Report"}, "answer": "B", "details": "Nagarik Badapatra (Citizen Charter) is mandated by the Good Governance Act.", "level": "Basic"},
    
    # MEDIUM LEVEL
    {"id": 41, "section": SYLLABUS_SECTIONS.CONST, "question": "For how long after the appointment of a PM can a No Confidence Motion NOT be tabled?", "options": {"A": "6 Months", "B": "1 Year", "C": "2 Years", "D": "No limit"}, "answer": "C", "details": "Article 100(4).", "level": "Medium"},
    {"id": 42, "section": SYLLABUS_SECTIONS.LAW, "question": "Which is NOT an essential element of a valid Contract?", "options": {"A": "Offer", "B": "Acceptance", "C": "Consideration", "D": "Friendship"}, "answer": "D", "details": "Intention to create legal relations is required, not friendship.", "level": "Medium"},
    {"id": 43, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Devolution differs from Delegation because Devolution is:", "options": {"A": "Temporary", "B": "Permanent transfer to autonomous bodies", "C": "Revocable at will", "D": "Administrative only"}, "answer": "B", "details": "Delegation is temporary; Devolution is statutory and permanent.", "level": "Medium"},
    {"id": 44, "section": SYLLABUS_SECTIONS.CONST, "question": "An ordinance ceases to be effective if not adopted within how many days of the House meeting?", "options": {"A": "30 Days", "B": "45 Days", "C": "60 Days", "D": "90 Days"}, "answer": "C", "details": "Article 114.", "level": "Medium"},
    {"id": 45, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Writ is issued to quash an illegal decision of a lower court?", "options": {"A": "Mandamus", "B": "Habeas Corpus", "C": "Certiorari", "D": "Quo Warranto"}, "answer": "C", "details": "Corrects jurisdictional errors.", "level": "Medium"},
    
    # HARD LEVEL
    {"id": 81, "section": SYLLABUS_SECTIONS.CONST, "question": "Which subject cannot be amended in the Constitution?", "options": {"A": "Fundamental Rights", "B": "Sovereignty & Territorial Integrity", "C": "Federalism", "D": "Secularism"}, "answer": "B", "details": "Article 274(1).", "level": "Hard"},
    {"id": 82, "section": SYLLABUS_SECTIONS.LAW, "question": "'Mens Rea' refers to:", "options": {"A": "The criminal act", "B": "The guilty mind/intent", "C": "The punishment", "D": "The victim"}, "answer": "B", "details": "Essential element of crime.", "level": "Hard"},
    {"id": 83, "section": SYLLABUS_SECTIONS.CONST, "question": "Majority required to ratify treaties on natural resources?", "options": {"A": "Simple Majority", "B": "Two-thirds of both Houses", "C": "Unanimous", "D": "Cabinet decision"}, "answer": "B", "details": "Article 279.", "level": "Hard"},
    {"id": 84, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which Committee enforces Financial Accountability?", "options": {"A": "State Affairs Committee", "B": "Public Accounts Committee (PAC)", "C": "Legislation Committee", "D": "Development Committee"}, "answer": "B", "details": "Reviews Auditor General reports.", "level": "Hard"},
    {"id": 85, "section": SYLLABUS_SECTIONS.LAW, "question": "'Pacta Sunt Servanda' means:", "options": {"A": "Agreements must be kept", "B": "Treaties are optional", "C": "War is illegal", "D": "Diplomacy first"}, "answer": "A", "details": "Fundamental treaty law principle.", "level": "Hard"},
]

# ===========================
# DATA: CURRENT AFFAIRS
# ===========================

current_affairs_news = [
    {"id": 301, "title": "Approval of Federal Civil Service Bill Draft", "summary": "The government approved the draft of the long-awaited Federal Civil Service Bill, aiming to finalize the administrative structure under the federal system.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
    {"id": 302, "title": "E-Governance Portal Integration Milestone", "summary": "The Digital Nepal Framework reached a milestone with the integration of over 50 public service portals into a single e-governance platform.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 303, "title": "Supreme Court Ruling on Ordinance Validity", "summary": "The SC delivered a landmark judgment questioning the excessive use of ordinances by the executive.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 304, "title": "Constitutional Council Appointments", "summary": "The Constitutional Council recommended new appointments to the CIAA and other constitutional bodies.", "section": SYLLABUS_SECTIONS.CONST, "level": "Basic"},
    {"id": 305, "title": "New Public Policy on Climate Resilience", "summary": "The government launched a new National Public Policy focusing on climate change adaptation.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
]

# ===========================
# HELPER FUNCTIONS
# ===========================

def filter_data(df, section, level):
    """Filter dataframe by section and difficulty level"""
    filtered = df.copy()
    if section != "All":
        filtered = filtered[filtered['section'] == section]
    if level != "All":
        filtered = filtered[filtered['level'] == level]
    return filtered

def initialize_session_state():
    """Initialize session state variables"""
    if 'mcq_sample' not in st.session_state:
        st.session_state.mcq_sample = None
    if 'mcq_checked' not in st.session_state:
        st.session_state.mcq_checked = {}

# ===========================
# UI COMPONENTS
# ===========================

def render_sidebar():
    """Render sidebar with filters"""
    st.sidebar.header("🎯 Practice Filters")
    
    practice_type = st.sidebar.radio(
        "Practice Type",
        ("MCQ", "Flashcard", "Current Affairs"),
        help="Select your learning mode"
    )
    
    section_options = ["All", SYLLABUS_SECTIONS.LAW, SYLLABUS_SECTIONS.ADMIN, SYLLABUS_SECTIONS.CONST]
    selected_section = st.sidebar.selectbox("📚 Section", section_options)
    
    difficulty_options = ["All"] + LEVELS
    selected_level = st.sidebar.selectbox("📊 Difficulty", difficulty_options)
    
    st.sidebar.markdown("---")
    st.sidebar.info("💡 Adjust filters to focus on specific topics")
    
    return practice_type, selected_section, selected_level

def render_mcq_mode(filtered_df):
    """Render MCQ practice mode"""
    if filtered_df.empty:
        st.warning("⚠️ No MCQs found for the selected filters.")
        return
    
    count = len(filtered_df)
    display_num = min(5, count)
    
    st.markdown(f"**📝 Practicing {display_num} questions** out of {count} available")
    
    # Generate new questions button
    if st.session_state.mcq_sample is None or st.button("🔄 Generate New Questions", key="refresh_mcq"):
        st.session_state.mcq_sample = filtered_df.sample(display_num).reset_index(drop=True)
        st.session_state.mcq_checked = {}
    
    sample_questions = st.session_state.mcq_sample
    
    # Render each question
    for i, row in sample_questions.iterrows():
        render_mcq_question(i, row)

def render_mcq_question(index, question_data):
    """Render a single MCQ question"""
    with st.container():
        st.markdown(f"### Question {index + 1}")
        st.markdown(f"**{question_data['question']}**")
        st.caption(f"📂 {question_data['section']} | 🎚️ {question_data['level']}")
        
        options = question_data['options']
        radio_options = [f"{k}: {v}" for k, v in options.items()]
        
        key = f"mcq_{question_data['id']}_{index}"
        checked_key = f"checked_{question_data['id']}_{index}"
        
        # Answer selection
        user_choice = st.radio("Select your answer:", radio_options, key=key)
        
        # Check answer button
        if st.button("✓ Check Answer", key=f"btn_{key}"):
            st.session_state.mcq_checked[checked_key] = user_choice
        
        # Display result if checked
        if checked_key in st.session_state.mcq_checked:
            display_mcq_result(question_data, st.session_state.mcq_checked[checked_key])
        
        st.markdown("---")

def display_mcq_result(question_data, user_choice):
    """Display MCQ answer result"""
    selected_opt = user_choice.split(":")[0].strip()
    correct_answer = question_data['answer']
    options = question_data['options']
    correct_answer_text = options[correct_answer]
    
    # Show result
    if selected_opt == correct_answer:
        st.success(f"✅ Correct! The answer is **{correct_answer}: {correct_answer_text}**")
    else:
        st.error(f"❌ Incorrect. The correct answer is **{correct_answer}: {correct_answer_text}**")
    
    # Show all options
    st.markdown("**All Options:**")
    for opt_key, opt_val in options.items():
        if opt_key == correct_answer:
            st.markdown(f"✓ **{opt_key}: {opt_val}** ← Correct Answer")
        else:
            st.write(f"{opt_key}: {opt_val}")
    
    st.info(f"**💡 Explanation:** {question_data['details']}")

def render_flashcard_mode(filtered_df):
    """Render flashcard practice mode"""
    if filtered_df.empty:
        st.warning("⚠️ No Flashcards found for the selected filters.")
        return
    
    st.markdown(f"**🗂️ Found {len(filtered_df)} flashcards**")
    
    if st.button("🔀 Shuffle Deck"):
        st.rerun()
    
    sample_card = filtered_df.sample(1).iloc[0]
    
    # Display flashcard
    st.markdown("### 📋 Question:")
    st.markdown(f"## {sample_card['question']}")
    
    with st.expander("👁️ Reveal Answer"):
        correct_option = sample_card['answer']
        answer_text = sample_card['options'][correct_option]
        st.markdown(f"### ✓ Answer: {correct_option} - {answer_text}")
        st.caption(f"**💡 Details:** {sample_card['details']}")
        st.caption(f"📂 Section: {sample_card['section']} | 🎚️ Level: {sample_card['level']}")

def render_current_affairs_mode(filtered_df):
    """Render current affairs mode"""
    if filtered_df.empty:
        st.warning("⚠️ No Current Affairs found for the selected filters.")
        return
    
    st.markdown(f"**📰 Displaying {len(filtered_df)} news items**")
    
    for i, row in filtered_df.iterrows():
        with st.expander(f"📌 {row['title']}"):
            st.write(row['summary'])
            st.caption(f"📂 {row['section']} | 🎚️ {row['level']}")

# ===========================
# MAIN APPLICATION
# ===========================

def main():
    st.set_page_config(
        page_title="Loksewa Learning Hub",
        page_icon="🇳🇵",
        layout="centered"
    )
    
    # Initialize
    initialize_session_state()
    
    # Header
    st.title("🇳🇵 Loksewa Learning Hub")
    st.markdown("*Master Governance, Law & Constitution for Public Service*")
    st.markdown("---")
    
    # Convert data to DataFrames
    mcq_df = pd.DataFrame(mcq_dataset)
    ca_df = pd.DataFrame(current_affairs_news)
    
    # Render sidebar and get selections
    practice_type, selected_section, selected_level = render_sidebar()
    
    # Display mode header
    st.header(f"📖 Mode: {practice_type}")
    st.caption(f"🎚️ Difficulty: **{selected_level}** | 📂 Section: **{selected_section}**")
    st.markdown("---")
    
    # Render appropriate mode
    if practice_type == "MCQ":
        filtered_df = filter_data(mcq_df, selected_section, selected_level)
        render_mcq_mode(filtered_df)
    
    elif practice_type == "Flashcard":
        filtered_df = filter_data(mcq_df, selected_section, selected_level)
        render_flashcard_mode(filtered_df)
    
    elif practice_type == "Current Affairs":
        filtered_df = filter_data(ca_df, selected_section, selected_level)
        render_current_affairs_mode(filtered_df)

if __name__ == "__main__":
    main()