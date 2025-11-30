import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Nepal Constitution Quiz",
    page_icon="🇳🇵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING (Dark Mode & Cards) ---
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    .question-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #334155;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
    }
    /* Success/Error message styling */
    .stAlert {
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- DATA SECTION (FULL 100 QUESTIONS) ---
questions_db = [
    # --- SECTION A: BASIC (1 Point) ---
    {'id': 1, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "In which year (BS) was Nepal's first written constitution promulgated?", 'options': ["2004 BS", "2007 BS", "2015 BS", "2019 BS"], 'ans': 0},
    {'id': 2, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "What was the full Nepali name of the Nepal Government Act 2004 BS?", 'options': ["Nepal Sarkar Kanoon", "Nepal Sarkar Baidhanik Kanoon", "Nepal Rajya Kanoon", "Nepal Shasan Bidhan"], 'ans': 1},
    {'id': 3, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The Interim Government Act of Nepal was promulgated in which year?", 'options': ["1948 AD", "1951 AD", "1959 AD", "1962 AD"], 'ans': 1},
    {'id': 4, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Who was Nepal's first democratically elected Prime Minister?", 'options': ["K.I. Singh", "B.P. Koirala", "Girija Prasad Koirala", "Pushpa Kamal Dahal"], 'ans': 1},
    {'id': 5, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "In which year did King Mahendra stage a royal coup?", 'options': ["1959 AD", "1960 AD", "1962 AD", "1965 AD"], 'ans': 1},
    {'id': 6, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The Panchayat system was introduced by which constitution?", 'options': ["Constitution of 1959", "Constitution of 1962", "Constitution of 1990", "Interim Constitution 2007"], 'ans': 1},
    {'id': 7, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "What was the primary feature of the Panchayat system?", 'options': ["Multiparty democracy", "Party-less democracy", "Presidential system", "Federal structure"], 'ans': 1},
    {'id': 8, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Jana Andolan I occurred in which year?", 'options': ["1985 AD", "1990 AD", "1996 AD", "2006 AD"], 'ans': 1},
    {'id': 9, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "How long did the Panchayat system last?", 'options': ["18 years", "23 years", "28 years", "33 years"], 'ans': 2},
    {'id': 10, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The Constitution of 1990 was promulgated in which BS year?", 'options': ["2045 BS", "2046 BS", "2047 BS", "2048 BS"], 'ans': 2},
    {'id': 11, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The Maoist insurgency in Nepal began in which year?", 'options': ["1990 AD", "1996 AD", "2001 AD", "2006 AD"], 'ans': 1},
    {'id': 12, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The royal family massacre occurred on which date?", 'options': ["June 1, 2001", "February 1, 2005", "April 24, 2006", "May 28, 2008"], 'ans': 0},
    {'id': 13, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "King Gyanendra assumed direct power in which year?", 'options': ["2001 AD", "2003 AD", "2005 AD", "2006 AD"], 'ans': 2},
    {'id': 14, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Jana Andolan II lasted for how many days?", 'options': ["12 days", "19 days", "30 days", "45 days"], 'ans': 1},
    {'id': 15, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The Comprehensive Peace Agreement was signed in which year?", 'options': ["2005 AD", "2006 AD", "2007 AD", "2008 AD"], 'ans': 1},
    {'id': 16, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The Interim Constitution of Nepal was promulgated on which date?", 'options': ["November 21, 2006", "January 15, 2007", "April 10, 2008", "May 28, 2008"], 'ans': 1},
    {'id': 17, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Nepal was declared a republic on which date?", 'options': ["January 15, 2007", "April 10, 2008", "May 28, 2008", "September 20, 2015"], 'ans': 2},
    {'id': 18, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The current Constitution of Nepal was promulgated in which year (BS)?", 'options': ["2070 BS", "2071 BS", "2072 BS", "2073 BS"], 'ans': 2},
    {'id': 19, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "How many provinces does Nepal have under the 2015 Constitution?", 'options': ["5", "7", "9", "11"], 'ans': 1},
    {'id': 20, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "How many fundamental rights are guaranteed by the 2015 Constitution?", 'options': ["23", "27", "31", "35"], 'ans': 2},
    {'id': 21, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The Nepal Government Act 2004 proposed which type of legislature?", 'options': ["Unicameral", "Bicameral", "Tricameral", "No legislature"], 'ans': 1},
    {'id': 22, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Under the 1948 Act, executive power was vested in whom?", 'options': ["The King", "The Rana Prime Minister (Shree Teen)", "The elected Prime Minister", "The Council of Ministers"], 'ans': 1},
    {'id': 23, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The 1959 Constitution established which form of government?", 'options': ["Presidential democracy", "Parliamentary democracy", "Absolute monarchy", "Federal republic"], 'ans': 1},
    {'id': 24, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Who was the chairman of the CPN (Maoist) during the insurgency?", 'options': ["Baburam Bhattarai", "Pushpa Kamal Dahal (Prachanda)", "Mohan Baidya", "Ram Bahadur Thapa"], 'ans': 1},
    {'id': 25, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Article 127 of the 1990 Constitution dealt with what?", 'options': ["Fundamental rights", "Emergency powers of the King (Removal of Difficulties)", "Amendment procedures", "Federal structure"], 'ans': 1},
    {'id': 26, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Which article of the 2007 Interim Constitution vested sovereignty in the people?", 'options': ["Article 1", "Article 2", "Article 3", "Article 4"], 'ans': 1},
    {'id': 27, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The 2015 Constitution establishes how many tiers of government?", 'options': ["2", "3", "4", "5"], 'ans': 1},
    {'id': 28, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "Who was Nepal's last King?", 'options': ["King Mahendra", "King Birendra", "King Gyanendra", "King Tribhuvan"], 'ans': 2},
    {'id': 29, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "The Public Service Commission conducts which examinations?", 'options': ["School exams", "Loksewa exams", "University exams", "Legal bar exams"], 'ans': 1},
    {'id': 30, 'section': 'A', 'type': 'mcq', 'points': 1, 'q': "CIAA stands for what?", 'options': ["Commission for Investigation of Administrative Authority", "Commission for the Investigation of Abuse of Authority", "Central Institute for Administrative Accountability", "Council for Investigation and Anti-corruption Authority"], 'ans': 1},

    # --- SECTION B: INTERMEDIATE (2 Points) ---
    {'id': 31, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Why was the Nepal Government Act 2004 BS never fully implemented?", 'options': ["International pressure", "Natural disasters", "Rana unwillingness to surrender real power", "Popular rejection"], 'ans': 2},
    {'id': 32, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "The Interim Government Act 2007 BS was amended how many times?", 'options': ["3 times", "6 times", "9 times", "12 times"], 'ans': 1},
    {'id': 33, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Fundamental flaw of Nepal Government Act 2004 BS?", 'options': ["No judiciary", "Legislature purely advisory, PM had veto", "Too complex", "Lacked recognition"], 'ans': 1},
    {'id': 34, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "The 1959 Constitution lasted approximately how long before being suspended?", 'options': ["6 months", "1 year (approx 18 months)", "3 years", "5 years"], 'ans': 1},
    {'id': 35, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "King Mahendra's justification for the 1960 coup?", 'options': ["Military necessity", "Failure of parliamentary democracy", "Foreign interference", "Economic crisis"], 'ans': 1},
    {'id': 36, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Under Panchayat, the Rastriya Panchayat had what limitation?", 'options': ["Could not discuss foreign policy", "Bills related to military/royal needed royal approval", "No taxation powers", "Meet once a year"], 'ans': 1},
    {'id': 37, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Coalition during Jana Andolan I?", 'options': ["NC and King", "Nepali Congress and United Left Front", "Maoists and NC", "UML and Royalists"], 'ans': 1},
    {'id': 38, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "1990 Constitution legislature type?", 'options': ["Unicameral", "Bicameral (Pratinidhi & Rastriya)", "Tricameral", "Constituent Assembly"], 'ans': 1},
    {'id': 39, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Duration of Maoist insurgency?", 'options': ["5 years", "10 years", "15 years", "20 years"], 'ans': 1},
    {'id': 40, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Approximate deaths during Maoist conflict?", 'options': ["Over 5,000", "Over 8,000", "Over 13,000", "Over 20,000"], 'ans': 2},
    {'id': 41, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "CPA signed between?", 'options': ["King and Maoists", "Seven-Party Alliance (SPA) and CPN (Maoist)", "India and Nepal", "NC and UML"], 'ans': 1},
    {'id': 42, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Primary purpose of 2007 Interim Constitution?", 'options': ["Manage transition and mandate CA", "Abolish monarchy immediately", "Establish socialism", "Create new military"], 'ans': 0},
    {'id': 43, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "First CA elected in?", 'options': ["2006", "2007", "2008", "2009"], 'ans': 2},
    {'id': 44, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Why did First CA fail?", 'options': ["Dissolved by King", "International intervention", "Disputes over federalism/gov form", "Natural disaster"], 'ans': 2},
    {'id': 45, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Second CA elected in?", 'options': ["2011", "2012", "2013", "2014"], 'ans': 2},
    {'id': 46, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Event accelerating 2015 constitution?", 'options': ["Political agreement", "2015 Earthquake", "International pressure", "Economic crisis"], 'ans': 1},
    {'id': 47, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Who primarily opposed 2015 Constitution at promulgation?", 'options': ["Hill Brahmins", "Madhesis and Tharus", "Newars", "Gurungs"], 'ans': 1},
    {'id': 48, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "2015-16 blockade duration?", 'options': ["2 months", "5 months", "8 months", "12 months"], 'ans': 1},
    {'id': 49, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Members in 1st CA?", 'options': ["240", "405", "601", "750"], 'ans': 2},
    {'id': 50, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Members in HoR (2015)?", 'options': ["205", "275", "330", "601"], 'ans': 1},
    {'id': 51, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "FPTP seats in HoR?", 'options': ["110", "165", "200", "240"], 'ans': 1},
    {'id': 52, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "PR seats in HoR?", 'options': ["75", "110", "150", "165"], 'ans': 1},
    {'id': 53, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Manav Nyayashastra introduced by?", 'options': ["Gopal", "Kirat", "Lichchhavi", "Malla (Jayasthiti Malla)"], 'ans': 3},
    {'id': 54, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Lichchhavi court for criminal cases?", 'options': ["Kuther", "Suli", "Lingual", "Mapchok"], 'ans': 1},
    {'id': 55, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Rana regime duration?", 'options': ["1769-1846", "1846-1951", "1951-1990", "1846-1990"], 'ans': 1},
    {'id': 56, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "First PM of Republic Nepal?", 'options': ["GP Koirala", "Prachanda", "Madhav Nepal", "Baburam Bhattarai"], 'ans': 1},
    {'id': 57, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Who promulgated 1990 Constitution?", 'options': ["Mahendra", "Birendra", "Gyanendra", "Tribhuvan"], 'ans': 1},
    {'id': 58, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Main demand of 2007 Madhesh Movement?", 'options': ["Independence", "Federalism & PR", "Monarchy", "Economics"], 'ans': 1},
    {'id': 59, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Number of local units (2015)?", 'options': ["293", "553", "753", "953"], 'ans': 2},
    {'id': 60, 'section': 'B', 'type': 'mcq', 'points': 2, 'q': "Largest province by area?", 'options': ["Koshi", "Bagmati", "Karnali", "Sudurpaschim"], 'ans': 2},

    # --- SECTION C: ADVANCED (3 Points) ---
    {'id': 61, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Difference between 1959 and 1962 Constitutions regarding sovereignty?", 'options': ["1959: People (via Parliament), 1962: Solely King", "Both vested in King", "1959: Shared, 1962: Popular", "No difference"], 'ans': 0},
    {'id': 62, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Why did 2004 BS Act fail to create separation of powers?", 'options': ["No judiciary", "Legislature advisory, Rana PM had absolute veto", "No elections", "Intl rejection"], 'ans': 1},
    {'id': 63, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Strategic significance of 2007 BS Act being 'flexible'?", 'options': ["Respond to fluid post-revolutionary context", "Poorly written", "No authority", "Temporary only"], 'ans': 0},
    {'id': 64, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Why did 1990 'constitutional monarchy' fail?", 'options': ["Economics", "Art 127 created contradiction in sovereignty", "External interference", "No public support"], 'ans': 1},
    {'id': 65, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Why did 1960 coup succeed but 2005 failed?", 'options': ["Intl pressure", "By 2005, democratic norms & parties were stronger", "India support", "No difference"], 'ans': 1},
    {'id': 66, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Critical innovation of 2007 Interim Constitution regarding monarchy?", 'options': ["Created CA to decide fate", "Banned King", "Confiscated property", "Military rule"], 'ans': 0},
    {'id': 67, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Promulgation amid Madhesi protests reveals?", 'options': ["Nothing", "Majority vote sufficient", "Legitimacy requires broader consensus than just votes", "Protests invalidate"], 'ans': 2},
    {'id': 68, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Judicial independence pattern (1959-2015)?", 'options': ["Promised on paper, but political/executive interference persisted", "Steadily improved", "1959 was best", "No pattern"], 'ans': 0},
    {'id': 69, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Fundamental tension in CA federalism debate?", 'options': ["Number of provinces", "Identity-based vs. Administrative", "Cost", "Intl pressure"], 'ans': 1},
    {'id': 70, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Challenge to 2015 federalism implementation?", 'options': ["Complexity", "Central unwillingness to devolve power/resources", "Provincial rejection", "Intl opposition"], 'ans': 1},
    {'id': 71, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Gender discrimination in Article 11 (2015)?", 'options': ["Women can't be citizens", "Unequal rights for women conferring citizenship to children vs men", "Can't vote", "Need permission"], 'ans': 1},
    {'id': 72, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Why do interim constitutions last ~8 years?", 'options': ["Coincidence", "Served specific transition/negotiation periods", "Intl requirement", "Mandated"], 'ans': 1},
    {'id': 73, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Lesson from 1st CA failure?", 'options': ["CAs don't work", "Disputes need political will, not just deliberation", "Intl mediation needed", "Bad elections"], 'ans': 1},
    {'id': 74, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Difference: Jana Andolan I vs II outcomes?", 'options': ["None", "I: Preserved Monarchy, II: Abolished it", "I: Violent, II: Peaceful", "I: Failed, II: Succeeded"], 'ans': 1},
    {'id': 75, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Why Panchayat lasted 28 years?", 'options': ["Popular support", "Repression, resource control, party ban", "Prosperity", "Intl support"], 'ans': 1},
    {'id': 76, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Legal significance of Directive Principles (1990)?", 'options': ["Enforceable", "Guidelines, not justiciable but important", "Advisory only", "Executive only"], 'ans': 1},
    {'id': 77, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "FPTP + PR mix attempts to balance?", 'options': ["Urban/Rural", "Accountability (FPTP) & Inclusion (PR)", "Fed/Prov", "Stability"], 'ans': 1},
    {'id': 78, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Why CPA needed before constitution?", 'options': ["Intl requirement", "Integrate Maoists & ensure stakeholder acceptance", "Formality", "Economic"], 'ans': 1},
    {'id': 79, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Schedule 5-9 significance (2015)?", 'options': ["Rights", "Exclusive/Concurrent powers of 3 tiers", "Provinces names", "Bodies"], 'ans': 1},
    {'id': 80, 'section': 'C', 'type': 'mcq', 'points': 3, 'q': "Meaning of 'Socialism-oriented'?", 'options': ["Communist state", "Social justice, equality, welfare state responsibility", "No private property", "Single party"], 'ans': 1},

    # --- SECTION D: EXPERT (4 Points - Flashcards) ---
    {'id': 81, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Could the 1959 democratic experiment have survived if King Mahendra had not staged the coup?", 'ans': "Key Concepts:\n- Constitutional design was sound.\n- Parties lacked maturity.\n- King's ambition was the main cause, not systemic failure.\n- Counter-factual: Democracy could have consolidated with time, but King's control of army made him a permanent threat."},
    {'id': 82, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Paradox: 1962 Panchayat lasted 28 yrs vs 1959 Democracy 1 yr. What does this teach about longevity?", 'ans': "Key Concepts:\n- Longevity ≠ Legitimacy.\n- Panchayat survived via repression/coercion.\n- Democracy destroyed by force, not failure.\n- Lesson: Autocracies persist without consent, but collapse when repression fails."},
    {'id': 83, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Why was 1990's 'Constitutional Monarchy with Popular Sovereignty' structurally impossible?", 'ans': "Key Concepts:\n- Sovereignty is indivisible.\n- Art 127 (Emergency Powers) created parallel sovereignty.\n- 2001 Massacre weakened royal legitimacy.\n- 2005 Coup exposed the flaw: Hybrid systems are unstable."},
    {'id': 84, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Pattern of relationship between street politics (Jana Andolans) and constitutional change?", 'ans': "Key Concepts:\n- Change driven by mass mobilization, not just elite negotiation.\n- JA-I: Ended Panchayat.\n- JA-II: Ended Monarchy.\n- Madhesh Movement: Forced Federalism.\n- Street legitimacy is as vital as legal legitimacy."},
    {'id': 85, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Success/Failure of Transitional Justice (TRC) in 2007/2015 constitutions?", 'ans': "Key Concepts:\n- TRC established but lacks credibility.\n- Political parties resist accountability (fear of prosecution).\n- Blanket amnesty violates intl law.\n- Result: Impunity culture and unhealed social wounds."},
    
    # --- PREVIOUSLY MISSING QUESTIONS (86-100) ---
    {'id': 86, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Why is there an implementation gap in Nepal's Federalism?", 'ans': "Key Concepts:\n- Structure exists (3 tiers), but Center retains power/revenue.\n- Delayed enabling laws (Civil Service Act).\n- Root Cause: Kathmandu elites resisting power devolution.\n- Constitutional design insufficient without political will."},
    {'id': 87, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "2015 Constitution: Elected CA but legitimacy crisis. Relationship between process and legitimacy?", 'ans': "Key Concepts:\n- Majority vote (Process) ≠ Consensus (Substantive Legitimacy).\n- Fast-tracked after earthquake, excluding Madhesis/Tharus.\n- Lesson: Valid legal procedure isn't enough for a constitution; it needs broad ownership."},
    {'id': 88, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Evolution of rights 1959 (Civil) -> 2015 (Socio-economic/31 rights)?", 'ans': "Key Concepts:\n- Reflects shift from 'Political Democracy' to 'Social Democracy'.\n- Response to insurgency grievances.\n- Challenge: Gap between enumeration (on paper) and enforcement (in reality)."},
    {'id': 89, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Why has judicial independence remained partially unfulfilled?", 'ans': "Key Concepts:\n- Judicial Council structure includes politicians.\n- Appointments became political sharing (Bhagbanda).\n- Executive interference persists (1952, Panchayat, Republic).\n- Structural reform needed to depoliticize appointments."},
    {'id': 90, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Was abolition of monarchy inevitable?", 'ans': "Key Concepts:\n- Shah monarchs (Mahendra, Gyanendra) chose autocracy over limits.\n- 2001 Massacre destroyed specific mystique.\n- Incompatibility of hereditary rule with modern popular sovereignty.\n- It was inevitable due to the specific behavior of Nepal's monarchs."},
    {'id': 91, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Why does gender discrimination (Art 11 Citizenship) persist?", 'ans': "Key Concepts:\n- Patriarchal mindset + Xenophobic nationalism ('Foreign men').\n- Fear of demographic change masks gender bias.\n- Constitutional equality (Art 18) contradicted by specific clauses.\n- Political will needed to enforce equality."},
    {'id': 92, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Significance of 'Secularism' in 2015 Constitution vs Hindu Identity?", 'ans': "Key Concepts:\n- Symbolic break from Monarchy.\n- Inclusion for non-Hindus.\n- Tension: 'Secular' defined as 'Sanatan protection' (Status Quo).\n- Gap between constitutional text and cultural reality."},
    {'id': 93, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Does having many Constitutional Bodies (CIAA, PSC, etc.) guarantee good governance?", 'ans': "Key Concepts:\n- Necessary for checks/balances but not sufficient.\n- Problems: Overlap, Bureaucracy, Politicized appointments.\n- Institutional design matters less than the political culture operating them."},
    {'id': 94, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Pattern of transitions: 1951 (Rana->King) vs 2007 (King->People).", 'ans': "Key Concepts:\n- All transitions driven by Crisis/Revolution, not evolution.\n- 1951: Transfer between elites.\n- 2007: Transfer to People.\n- Question: Can future change be peaceful/evolutionary?"},
    {'id': 95, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "How did 2015 Constitution address Maoist insurgency grievances?", 'ans': "Key Concepts:\n- Abolished Monarchy.\n- Established Federalism.\n- Inclusion/PR system.\n- Assessment: Structural changes made, but elite capture continues."},
    {'id': 96, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Role of India in Nepal's constitutional choices?", 'ans': "Key Concepts:\n- 1950 Treaty, 1990 Blockade, 2005 Agreement, 2015 Blockade.\n- Geopolitics shapes internal choices.\n- Tension: Nationalism vs Pragmatism.\n- Nepal must balance sovereignty with geographic reality."},
    {'id': 97, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Evaluate FPTP + PR system impact.", 'ans': "Key Concepts:\n- Positive: Huge increase in Women/Dalit/Janajati MPs.\n- Negative: Party bosses control PR lists (Loyalty > Competence).\n- Better than pure FPTP, but needs 'Open List' reform."},
    {'id': 98, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Why did 1st CA fail vs 2nd CA succeed?", 'ans': "Key Concepts:\n- 1st CA: Maoist dominance, rigid stance on identity federalism.\n- 2nd CA: NC/UML coalition, Earthquake created urgency.\n- 'Success' was rushing a compromise, even if flawed."},
    {'id': 99, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Shift in Sovereignty location (1948-2015).", 'ans': "Key Concepts:\n- 1948: PM.\n- 1951: King.\n- 1959: People.\n- 1960: King.\n- 1990: Hybrid (Unstable).\n- 2015: People (Unambiguous).\n- Stability requires clear popular sovereignty."},
    {'id': 100, 'section': 'D', 'type': 'flashcard', 'points': 4, 'q': "Has Nepal achieved constitutional stability with 2015 Constitution?", 'ans': "Key Concepts:\n- Yes: Core issues (Republic, Federalism) settled.\n- No: Implementation weak, exclusion felt by Madhesis.\n- Conclusion: Framework is stable, but struggle shifts to implementation and amendment."},
]

# --- SESSION STATE INITIALIZATION ---
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

# --- FUNCTIONS ---

def start_quiz():
    st.session_state.quiz_started = True

def next_question():
    if st.session_state.current_index < len(questions_db) - 1:
        st.session_state.current_index += 1

def prev_question():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1

def submit_answer(q_id, choice_index, correct_index, points):
    # Logic: Only update score if it wasn't answered correctly before
    previous_record = st.session_state.user_answers.get(q_id)
    is_correct = (choice_index == correct_index)
    
    if previous_record is None or not previous_record['is_correct']:
        if is_correct:
            st.session_state.score += points
            
    st.session_state.user_answers[q_id] = {
        'user_choice': choice_index,
        'is_correct': is_correct,
        'correct_ans': correct_index
    }

# --- UI RENDERER ---

# 1. START SCREEN
if not st.session_state.quiz_started:
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 50px;'>
            <h1 style='color: #ef4444; font-size: 3rem;'>संवैधानिक विकासक्रम प्रश्नोत्तर</h1>
            <h3 style='color: #cbd5e1;'>Nepal Constitution Quiz</h3>
            <p style='font-size: 1.2rem; margin-top: 20px;'>Test your knowledge on Nepal's constitutional history.<br>
            100 Questions | Basic to Expert Levels</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start to practice ", use_container_width=True):
            start_quiz()
            st.rerun()

# 2. RESULTS SCREEN
elif st.session_state.show_results:
    total_score = st.session_state.score
    total_possible = sum(q['points'] for q in questions_db)
    pct = int(total_score / max(1, total_possible) * 100)
    
    st.balloons()
    st.markdown(f"""
    <div style='text-align: center; padding: 40px; background-color: #1e293b; border-radius: 15px;'>
        <h1>Final Results / अन्तिम नतिजा</h1>
        <h2 style='font-size: 4rem; color: #ef4444;'>{total_score} / {total_possible}</h2>
        <h3>({pct}%)</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        if st.button('Restart Quiz / पुन: सुरु गर्नुहोस्', use_container_width=True):
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.user_answers = {}
            st.session_state.show_results = False
            st.session_state.quiz_started = False
            st.rerun()

# 3. MAIN QUIZ INTERFACE
else:
    # --- SIDEBAR ---
    with st.sidebar:
        st.header(" Quiz Stats")
        st.metric("Current Score", st.session_state.score)
        
        answered_count = len(st.session_state.user_answers)
        total_questions = len(questions_db)
        prog = answered_count / total_questions
        st.progress(prog)
        st.caption(f"Progress: {answered_count}/{total_questions}")
        
        st.divider()
        st.subheader("📝 History")
        
        correct_list = [qid for qid, data in st.session_state.user_answers.items() if data['is_correct']]
        wrong_list = [qid for qid, data in st.session_state.user_answers.items() if not data['is_correct']]

        with st.expander(f"✅ Correct ({len(correct_list)})", expanded=False):
            for qid in correct_list:
                st.success(f"Q{qid}")

        with st.expander(f"❌ Wrong ({len(wrong_list)})", expanded=True):
            if not wrong_list:
                st.caption("Keep going!")
            for qid in wrong_list:
                data = st.session_state.user_answers[qid]
                q_data = next((item for item in questions_db if item["id"] == qid), None)
                if q_data and q_data['type'] == 'mcq':
                    st.error(f"Q{qid}")
                    st.caption(f"Your: {q_data['options'][data['user_choice']]}")
                    st.caption(f"Ans: {q_data['options'][data['correct_ans']]}")
                else:
                    st.error(f"Q{qid} (Flashcard)")

    # --- QUESTION AREA ---
    curr_q = questions_db[st.session_state.current_index]
    
    # Progress Bar Top
    st.markdown(f"**Section {curr_q['section']}** • Question {curr_q['id']} of {len(questions_db)} • <span style='color:#facc15'>{curr_q['points']} Pts</span>", unsafe_allow_html=True)
    
    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    st.markdown(f"### {curr_q['q']}")
    
    # --- MCQ HANDLER (FIXED FOR NONETYPE ERROR) ---
    if curr_q['type'] == 'mcq':
        # We add a placeholder at index 0 so Streamlit always has a valid index
        display_options = ["Select an answer..."] + curr_q['options']
        
        # Calculate index: If answered before, shift +1. If not, use 0.
        prev_ans = st.session_state.user_answers.get(curr_q['id'])
        default_idx = (prev_ans['user_choice'] + 1) if prev_ans else 0
        
        selected_opt = st.radio(
            "Options:",
            display_options,
            index=default_idx,
            label_visibility="collapsed",
            key=f"q_radio_{curr_q['id']}"
        )
        
        # Logic: Process answer if selection is NOT the placeholder
        if selected_opt and selected_opt != "Select an answer...":
            # Get actual index (0-3)
            choice_idx = display_options.index(selected_opt) - 1
            
            # Submit answer
            submit_answer(curr_q['id'], choice_idx, curr_q['ans'], curr_q['points'])
            
            # Show feedback
            if choice_idx == curr_q['ans']:
                st.success(" Correct Answer!")
            else:
                st.error(f"Wrong Answer! Correct: {curr_q['options'][curr_q['ans']]}")

    # --- FLASHCARD HANDLER ---
    elif curr_q['type'] == 'flashcard':
        st.info("Thinking Phase: Recall the answer mentally.")
        
        # Check if already mastered
        prev_fc = st.session_state.user_answers.get(curr_q['id'])
        
        if prev_fc and prev_fc['is_correct']:
             st.success(" You have mastered this concept!")
             with st.expander("View Answer Again"):
                 st.markdown(curr_q['ans'])
        else:
            with st.expander(" Reveal Answer"):
                st.markdown(f"### Key Concepts:\n{curr_q['ans']}")
                st.divider()
                st.write("Did you get the main points correct?")
                if st.button("Yes, I mastered this (+4 Pts) ", key=f"fc_btn_{curr_q['id']}"):
                    st.session_state.score += 4
                    st.session_state.user_answers[curr_q['id']] = {'user_choice': 0, 'is_correct': True, 'correct_ans': 0}
                    st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # --- NAVIGATION FOOTER ---
    col_back, col_next = st.columns([1, 1])
    
    with col_back:
        if st.button("⬅️ Backward", disabled=(st.session_state.current_index == 0)):
            prev_question()
            st.rerun()
            
    with col_next:
        if st.session_state.current_index == len(questions_db) - 1:
            if st.button("Finish & Results 🏁"):
                st.session_state.show_results = True
                st.rerun()
        else:
            if st.button("Forward ➡️"):
                next_question()
                st.rerun()