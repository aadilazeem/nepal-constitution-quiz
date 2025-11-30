import streamlit as st
import random

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Nepal Constitution & Governance Quiz",
    page_icon="🇳🇵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING ---
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
</style>
""", unsafe_allow_html=True)

# --- CONSTANTS ---
class SYLLABUS_SECTIONS:
    LAW = "Law & Justice"
    ADMIN = "Public Administration"
    CONST = "Constitution"

# --- DATA SECTION - ALL 122 QUESTIONS ---
mcq_dataset = [
    # --- BASIC QUESTIONS (1-40) ---
    {"id": 1, "section": SYLLABUS_SECTIONS.CONST, "question": "In whom is the sovereignty and state power of Nepal vested?", "options": ["The President","The Parliament","The Nepali People","The Council of Ministers"], "answer": 2, "details": "Article 2 of the Constitution states sovereignty is vested in the Nepali people.", "level": "Basic"},
    {"id": 2, "section": SYLLABUS_SECTIONS.CONST, "question": "What is the National Animal of Nepal according to the Constitution?", "options": ["Tiger", "Rhino", "Cow (Gai)", "Musk Deer"], "answer": 2, "details": "Article 9(3) / Schedule-3.", "level": "Basic"},
    {"id": 3, "section": SYLLABUS_SECTIONS.CONST, "question": "Which Article guarantees the Right to Information (RTI)?", "options": ["Article 16", "Article 27", "Article 33", "Article 46"], "answer": 1, "details": "Article 27 guarantees the right to demand and receive information.", "level": "Basic"},
    {"id": 4, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the standard retirement age for Civil Servants in Nepal?", "options": ["55 Years", "58 Years", "60 Years", "63 Years"], "answer": 1, "details": "According to the Civil Service Act.", "level": "Basic"},
    {"id": 5, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Writ literally means 'Show me the body'?", "options": ["Mandamus", "Certiorari", "Quo Warranto", "Habeas Corpus"], "answer": 3, "details": "Used to secure the release of an unlawfully detained person.", "level": "Basic"},
    {"id": 6, "section": SYLLABUS_SECTIONS.CONST, "question": "What is the maximum number of Justices in the Supreme Court (excluding CJ)?", "options": ["15", "20", "21", "25"], "answer": 1, "details": "Article 129 states a maximum of 20 Justices in addition to the Chief Justice.", "level": "Basic"},
    {"id": 7, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Who chairs the National Planning Commission (NPC) of Nepal?", "options": ["Finance Minister", "Chief Secretary", "Prime Minister", "President"], "answer": 2, "details": "The Prime Minister is the Chairperson of the NPC.", "level": "Basic"},
    {"id": 8, "section": SYLLABUS_SECTIONS.LAW, "question": "What kind of law deals with offenses against the state and results in punishment?", "options": ["Civil Law", "Criminal Law", "Family Law", "Contract Law"], "answer": 1, "details": "Criminal law focuses on punishment for offenses.", "level": "Basic"},
    {"id": 9, "section": SYLLABUS_SECTIONS.CONST, "question": "The Executive Power of Nepal is vested in whom?", "options": ["The President", "The Council of Ministers", "The Parliament", "The Supreme Court"], "answer":1, "details": "Article 75 vests executive power in the Council of Ministers.", "level": "Basic"},
    {"id": 10, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the document defining services, time limits, and fees for a public office?", "options": ["Office Manual", "Citizen Charter", "Constitution", "Annual Report"], "answer": 1, "details": "Nagarik Badapatra (Citizen Charter) is mandated by the Good Governance Act.", "level": "Basic"},
    {"id": 11, "section": SYLLABUS_SECTIONS.CONST, "question": "How many Fundamental Rights are guaranteed in Part 3 of the Constitution?", "options": ["25", "31", "35", "40"], "answer": 1, "details": "Articles 16 to 46 (31 Rights).", "level": "Basic"},
    {"id": 12, "section": SYLLABUS_SECTIONS.CONST, "question": "On which date must the Federal Budget be presented to Parliament?", "options": ["Baishakh 1", "Jestha 15", "Asar 1", "Shrawan 1"], "answer": 1, "details": "Article 119(3) mandates Jestha 15 (Republic Day).", "level": "Basic"},
    {"id": 13, "section": SYLLABUS_SECTIONS.CONST, "question": "Who is the ceremonial Head of State of Nepal?", "options": ["Prime Minister", "Chief Justice", "President", "Speaker"], "answer": 2, "details": "Article 61 defines the President as the Head of State.", "level": "Basic"},
    {"id": 14, "section": SYLLABUS_SECTIONS.LAW, "question": "The Writ of Quo Warranto literally means?", "options": ["We Command", "By what authority", "To be certified", "Prohibition"], "answer": 1, "details": "Challenges the legality of a person holding public office.", "level": "Basic"},
    {"id": 15, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which E-Governance model focuses on government services delivered to the public?", "options": ["G2G", "G2B", "G2C", "G2E"], "answer": 2, "details": "Government to Citizen (G2C).", "level": "Basic"},
    {"id": 16, "section": SYLLABUS_SECTIONS.CONST, "question": "How many levels of government does Nepal's Federalism have?", "options": ["Two", "Three", "Five", "Seven"], "answer": 1, "details": "Federal, Provincial, and Local.", "level": "Basic"},
    {"id": 17, "section": SYLLABUS_SECTIONS.LAW, "question": "What is the main remedy sought in a Civil Law dispute?", "options": ["Imprisonment", "Compensation/Damages", "Fine to State", "Capital Punishment"], "answer": 1, "details": "Civil law aims to restore the injured party.", "level": "Basic"},
    {"id": 18, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What quality of governance means openness in decisions, allowing public scrutiny?", "options": ["Efficiency", "Transparency", "Economy", "Secrecy"], "answer": 1, "details": "Transparency is key to Good Governance.", "level": "Basic"},
    {"id": 19, "section": SYLLABUS_SECTIONS.CONST, "question": "How many times has the Constitution of Nepal (2015) been amended?", "options": ["Once", "Twice", "Thrice", "Never"], "answer": 1, "details": "First in 2016, Second in 2020.", "level": "Basic"},
    {"id": 20, "section": SYLLABUS_SECTIONS.LAW, "question": "Which code governs Family Law (Marriage, Divorce) in Nepal?", "options": ["Muluki Ain 2020", "Muluki Civil Code 2074", "Evidence Act", "Constitution"], "answer": 1, "details": "Muluki Civil Code 2074 replaced the old Muluki Ain.", "level": "Basic"},
    {"id": 21, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the key legislative body at the Rural Municipality level?", "options": ["Gaun Palika", "Gaun Sabha", "Ward Committee", "District Coordination Committee"], "answer": 1, "details": "The Village Assembly (Gaun Sabha) acts as the local legislature.", "level": "Basic"},
    {"id": 22, "section": SYLLABUS_SECTIONS.CONST, "question": "Which Article provides for the Language Commission?", "options": ["Article 280", "Article 287", "Article 100", "Article 50"], "answer": 1, "details": "Article 287 establishes the Language Commission.", "level": "Basic"},
    {"id": 23, "section": SYLLABUS_SECTIONS.LAW, "question": "What is 'Najiir'?", "options": ["A new law", "A court precedent", "A police report", "A contract"], "answer": 1, "details": "Precedent established by the Supreme Court.", "level": "Basic"},
    {"id": 24, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What does O&M stand for in Administration?", "options": ["Office and Management", "Organization and Management", "Order and Method", "Operation and Maintenance"], "answer": 1, "details": "Survey technique for structural efficiency.", "level": "Basic"},
    {"id": 25, "section": SYLLABUS_SECTIONS.CONST, "question": "Who appoints the Attorney General of Nepal?", "options": ["Prime Minister", "Chief Justice", "President", "Law Minister"], "answer": 2, "details": "President appoints on recommendation of the Prime Minister.", "level": "Basic"},
    {"id": 26, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Act is key for consumer protection in Nepal?", "options": ["Black Marketing Act", "Consumer Protection Act 2075", "Civil Code", "Food Act"], "answer": 1, "details": "The 2075 Act is the primary legislation.", "level": "Basic"},
    {"id": 27, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which international body popularized the term 'Good Governance'?", "options": ["United Nations", "World Bank", "IMF", "WTO"], "answer": 1, "details": "In the late 1980s.", "level": "Basic"},
    {"id": 28, "section": SYLLABUS_SECTIONS.CONST, "question": "Who has the authority to grant pardons in Nepal?", "options": ["Supreme Court", "Prime Minister", "President", "Home Minister"], "answer": 2, "details": "Article 276.", "level": "Basic"},
    {"id": 29, "section": SYLLABUS_SECTIONS.LAW, "question": "What is Mandamus?", "options": ["Order to stop", "Order to perform a duty", "Order to produce a person", "Order to certify"], "answer": 1, "details": "Compels a public official to act.", "level": "Basic"},
    {"id": 30, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the primary goal of Public Service Delivery?", "options": ["Profit maximization", "Serving citizens effectively", "Expanding bureaucracy", "Collecting taxes"], "answer": 1, "details": "Effective, efficient, and equitable service.", "level": "Basic"},
    {"id": 31, "section": SYLLABUS_SECTIONS.CONST, "question": "Which tier of government has the power to impose sales tax?", "options": ["Local", "Provincial", "Federal", "Concurrent"], "answer": 2, "details": "Schedule 5 lists it as a Federal power.", "level": "Basic"},
    {"id": 32, "section": SYLLABUS_SECTIONS.LAW, "question": "What is 'Jus Cogens'?", "options": ["A flexible rule", "A compelling, peremptory norm", "A bilateral treaty", "Domestic law"], "answer": 1, "details": "A fundamental principle of international law.", "level": "Basic"},
    {"id": 33, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is Delegated Legislation?", "options": ["Acts of Parliament", "Constitution", "Rules/Regulations made by Executive", "Court Orders"], "answer": 2, "details": "Law-making power delegated to the executive.", "level": "Basic"},
    {"id": 34, "section": SYLLABUS_SECTIONS.CONST, "question": "What electoral systems are used for the House of Representatives?", "options": ["FPTP only", "PR only", "FPTP and PR", "Electoral College"], "answer": 2, "details": "Mixed system: 165 FPTP + 110 PR.", "level": "Basic"},
    {"id": 35, "section": SYLLABUS_SECTIONS.LAW, "question": "What is 'Muchulka'?", "options": ["A verdict", "A petition", "A memo/record of facts", "A bail bond"], "answer": 2, "details": "Prepared on the spot to record facts.", "level": "Basic"},
    {"id": 36, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Public Accountability implies answerability to whom?", "options": ["Superiors only", "The Public", "Donors", "Political Parties"], "answer": 1, "details": "Answerability to the citizens.", "level": "Basic"},
    {"id": 37, "section": SYLLABUS_SECTIONS.CONST, "question": "What is the tenure of the CIAA Chief Commissioner?", "options": ["4 Years", "5 Years", "6 Years", "Till age 60"], "answer": 2, "details": "Article 238.", "level": "Basic"},
    {"id": 38, "section": SYLLABUS_SECTIONS.LAW, "question": "Tort Law deals with:", "options": ["Crimes", "Civil wrongs causing harm", "International treaties", "Constitutional amendments"], "answer": 1, "details": "e.g., Negligence, Nuisance.", "level": "Basic"},
    {"id": 39, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Deconcentration is a form of:", "options": ["Centralization", "Privatization", "Decentralization", "Nationalization"], "answer": 2, "details": "The weakest form of decentralization.", "level": "Basic"},
    {"id": 40, "section": SYLLABUS_SECTIONS.CONST, "question": "What does 'Secularism' mean in the Nepal Constitution?", "options": ["Absence of religion", "Anti-religion", "Protection of Sanatana Dharma", "One state religion"], "answer": 2, "details": "Article 4 Explanation.", "level": "Basic"},

    # --- MEDIUM QUESTIONS (41-80) ---
    {"id": 41, "section": SYLLABUS_SECTIONS.CONST, "question": "For how long after the appointment of a PM can a No Confidence Motion NOT be tabled?", "options": ["6 Months", "1 Year", "2 Years", "No limit"], "answer": 2, "details": "Article 100(4).", "level": "Medium"},
    {"id": 42, "section": SYLLABUS_SECTIONS.LAW, "question": "Which is NOT an essential element of a valid Contract?", "options": ["Offer", "Acceptance", "Consideration", "Friendship"], "answer": 3, "details": "Intention to create legal relations is required, not friendship.", "level": "Medium"},
    {"id": 43, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Devolution differs from Delegation because Devolution is:", "options": ["Temporary", "Permanent transfer to autonomous bodies", "Revocable at will", "Administrative only"], "answer": 1, "details": "Delegation is temporary; Devolution is statutory and permanent.", "level": "Medium"},
    {"id": 44, "section": SYLLABUS_SECTIONS.CONST, "question": "An ordinance ceases to be effective if not adopted within how many days of the House meeting?", "options": ["30 Days", "45 Days", "60 Days", "90 Days"], "answer": 2, "details": "Article 114.", "level": "Medium"},
    {"id": 45, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Writ is issued to quash an illegal decision of a lower court?", "options": ["Mandamus", "Habeas Corpus", "Certiorari", "Quo Warranto"], "answer": 2, "details": "Corrects jurisdictional errors.", "level": "Medium"},
    {"id": 46, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the first step in the Public Policy Process?", "options": ["Evaluation", "Implementation", "Formulation", "Agenda Setting / Problem ID"], "answer": 3, "details": "Identifying the problem comes first.", "level": "Medium"},
    {"id": 47, "section": SYLLABUS_SECTIONS.CONST, "question": "Composition of the Constitutional Bench:", "options": ["CJ + 2 Justices", "CJ + 4 Justices", "5 Senior Justices", "Full Bench"], "answer": 1, "details": "Article 137.", "level": "Medium"},
    {"id": 48, "section": SYLLABUS_SECTIONS.LAW, "question": "Which part of the Muluki Civil Code deals with Property Rights?", "options": ["Part 1", "Part 3", "Part 4", "Part 6"], "answer": 2, "details": "Governs ownership, possession, and transfer.", "level": "Medium"},
    {"id": 49, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Social Inclusion aims to help:", "options": ["The Elite", "Marginalized groups", "Political Parties", "Foreign Investors"], "answer": 1, "details": "Ensures equal access for excluded groups.", "level": "Medium"},
    {"id": 50, "section": SYLLABUS_SECTIONS.CONST, "question": "Who coordinates the Judicial Committee at the Local Level?", "options": ["Mayor/Chairperson", "Deputy Mayor/Vice-Chairperson", "Chief Administrative Officer", "Ward Chair"], "answer": 1, "details": "Article 217.", "level": "Medium"},
    {"id": 51, "section": SYLLABUS_SECTIONS.CONST, "question": "Article 36 (Right to Food) guarantees the right to:", "options": ["Free food for all", "Food Sovereignty", "Imported food", "Subsidized crops"], "answer": 1, "details": "Also includes protection from starvation.", "level": "Medium"},
    {"id": 52, "section": SYLLABUS_SECTIONS.LAW, "question": "The physical act of a crime is called:", "options": ["Mens Rea", "Actus Reus", "Obiter Dicta", "Res Judicata"], "answer": 1, "details": "Mens Rea is the mental intent.", "level": "Medium"},
    {"id": 53, "section": SYLLABUS_SECTIONS.ADMIN, "question": "A primary market-related reason for Public Enterprises is to:", "options": ["Increase taxes", "Prevent Monopoly", "Employ party cadres", "Reduce exports"], "answer": 1, "details": "And provide essential services.", "level": "Medium"},
    {"id": 54, "section": SYLLABUS_SECTIONS.CONST, "question": "Who votes in the Presidential Election?", "options": ["Only MPs", "Only Provincial Members", "Federal Parliament & Provincial Assemblies", "All Citizens"], "answer": 2, "details": "Electoral College (Article 62).", "level": "Medium"},
    {"id": 55, "section": SYLLABUS_SECTIONS.LAW, "question": "Which is a primary source of International Law?", "options": ["Treaties", "News reports", "NGO reports", "Domestic circulars"], "answer": 0, "details": "Along with Custom and General Principles.", "level": "Medium"},
    {"id": 56, "section": SYLLABUS_SECTIONS.ADMIN, "question": "The World Bank is an example of a:", "options": ["Bilateral Agency", "Multilateral Agency", "NGO", "Local Club"], "answer": 1, "details": "Represents multiple member countries.", "level": "Medium"},
    {"id": 57, "section": SYLLABUS_SECTIONS.CONST, "question": "Who is the Member-Secretary of the National Security Council?", "options": ["Home Secretary", "Defence Secretary", "Chief of Army Staff", "IGP"], "answer": 1, "details": "Article 266.", "level": "Medium"},
    {"id": 58, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Act governs the privatization of PEs?", "options": ["Company Act", "Privatization Act 2050", "Industrial Enterprise Act", "Labor Act"], "answer": 1, "details": "Enacted to manage the transfer of PEs.", "level": "Medium"},
    {"id": 59, "section": SYLLABUS_SECTIONS.ADMIN, "question": "The 'Buch Commission' (2009 BS) is related to:", "options": ["Land Reform", "Administrative Reform", "Education", "Health"], "answer": 1, "details": "First major admin reform commission.", "level": "Medium"},
    {"id": 60, "section": SYLLABUS_SECTIONS.CONST, "question": "Schedule 9 of the Constitution lists:", "options": ["Federal Powers", "Provincial Powers", "Local Powers", "Concurrent Powers"], "answer": 3, "details": "Powers shared by all three tiers.", "level": "Medium"},
    {"id": 61, "section": SYLLABUS_SECTIONS.LAW, "question": "An Injunction is a court order to:", "options": ["Pay money", "Perform or stop a specific act", "Go to jail", "Apologize"], "answer": 1, "details": "A remedy in civil law.", "level": "Medium"},
    {"id": 62, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Accountability enforced by courts is:", "options": ["Social Accountability", "Legal Accountability", "Political Accountability", "Ethical Accountability"], "answer": 1, "details": "Based on law and compliance.", "level": "Medium"},
    {"id": 63, "section": SYLLABUS_SECTIONS.CONST, "question": "Who is the 'Chief of Province'?", "options": ["Chief Minister", "Speaker of Province", "Representative of Federal Govt in Province", "Chief Judge"], "answer": 2, "details": "Appointed by President (Article 163).", "level": "Medium"},
    {"id": 64, "section": SYLLABUS_SECTIONS.LAW, "question": "If a ratified treaty conflicts with Nepal law, which prevails?", "options": ["Nepal Law", "The Treaty", "Supreme Court decides", "Both are void"], "answer": 1, "details": "Per Nepal Treaty Act 1990.", "level": "Medium"},
    {"id": 65, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which policy step assesses impact?", "options": ["Formulation", "Implementation", "Adoption", "Evaluation"], "answer": 3, "details": "Checking if goals were met.", "level": "Medium"},
    {"id": 66, "section": SYLLABUS_SECTIONS.CONST, "question": "Is the NPC a Constitutional Body?", "options": ["Yes", "No", "Partially", "Pending status"], "answer": 1, "details": "It is a specialized executive agency.", "level": "Medium"},
    {"id": 67, "section": SYLLABUS_SECTIONS.LAW, "question": "Article 31 guarantees education in:", "options": ["English", "Mother Tongue", "Sanskrit", "Hindi"], "answer": 1, "details": "Right to basic education in mother tongue.", "level": "Medium"},
    {"id": 68, "section": SYLLABUS_SECTIONS.ADMIN, "question": "G2E E-Governance targets:", "options": ["Citizens", "Businesses", "Employees (Internal)", "Foreign Govts"], "answer": 2, "details": "Improving internal efficiency.", "level": "Medium"},
    {"id": 69, "section": SYLLABUS_SECTIONS.CONST, "question": "Who can initiate impeachment of the CJ?", "options": ["President", "PM", "1/4th of HoR members", "Bar Association"], "answer": 2, "details": "Article 101.", "level": "Medium"},
    {"id": 70, "section": SYLLABUS_SECTIONS.LAW, "question": "Company and Banking laws fall under:", "options": ["Criminal Law", "Commercial Law", "Family Law", "Constitutional Law"], "answer": 1, "details": "Regulating business transactions.", "level": "Medium"},
    {"id": 71, "section": SYLLABUS_SECTIONS.ADMIN, "question": "'Prerogative Power' usually belongs to:", "options": ["Civil Servants", "The Head of State", "Local Ward Chair", "NGOs"], "answer": 1, "details": "Discretionary powers.", "level": "Medium"},
    {"id": 72, "section": SYLLABUS_SECTIONS.CONST, "question": "Can the PM dissolve the House at will?", "options": ["Yes, always", "No, heavily restricted", "Yes, with President's support", "Only in emergency"], "answer": 1, "details": "Only if government formation is impossible.", "level": "Medium"},
    {"id": 73, "section": SYLLABUS_SECTIONS.LAW, "question": "Coexistence of state and customary law is:", "options": ["Legal Monism", "Legal Pluralism", "Anarchy", "Dictatorship"], "answer": 1, "details": "Multiple legal systems.", "level": "Medium"},
    {"id": 74, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Delegation is temporary; Devolution is:", "options": ["Also temporary", "Permanent", "Illegal", "Informal"], "answer": 1, "details": "Transfer to autonomous units.", "level": "Medium"},
    {"id": 75, "section": SYLLABUS_SECTIONS.CONST, "question": "Who recommends revenue distribution?", "options": ["Ministry of Finance", "NPC", "NNRFC", "Rastra Bank"], "answer": 2, "details": "National Natural Resources and Fiscal Commission.", "level": "Medium"},
    {"id": 76, "section": SYLLABUS_SECTIONS.LAW, "question": "'Punitive Damages' are meant to:", "options": ["Compensate", "Punish and deter", "Refund costs", "Pay taxes"], "answer": 1, "details": "Beyond actual loss.", "level": "Medium"},
    {"id": 77, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Where must a Citizen Charter be displayed?", "options": ["In the file", "On the website only", "Visibly in the office", "In the store"], "answer": 2, "details": "Good Governance Act requirement.", "level": "Medium"},
    {"id": 78, "section": SYLLABUS_SECTIONS.CONST, "question": "What is the fixed term of the PM?", "options": ["5 Years", "2 Years", "No fixed term", "10 Years"], "answer": 2, "details": "Depends on House confidence.", "level": "Medium"},
    {"id": 79, "section": SYLLABUS_SECTIONS.LAW, "question": "Stare Decisis means:", "options": ["To stand by decided matters", "To argue", "To legislate", "To appeal"], "answer": 0, "details": "Precedent principle.", "level": "Medium"},
    {"id": 80, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Challenge for E-Governance in rural Nepal:", "options": ["Too much internet", "Digital Divide", "Excess electricity", "High literacy"], "answer": 1, "details": "Lack of access/skills.", "level": "Medium"},

    # --- HARD QUESTIONS (81-122) ---
    {"id": 81, "section": SYLLABUS_SECTIONS.CONST, "question": "Which subject cannot be amended in the Constitution?", "options": ["Fundamental Rights", "Sovereignty & Territorial Integrity", "Federalism", "Secularism"], "answer": 1, "details": "Article 274(1).", "level": "Hard"},
    {"id": 82, "section": SYLLABUS_SECTIONS.LAW, "question": "'Mens Rea' refers to:", "options": ["The criminal act", "The guilty mind/intent", "The punishment", "The victim"], "answer": 1, "details": "Essential element of crime.", "level": "Hard"},
    {"id": 83, "section": SYLLABUS_SECTIONS.CONST, "question": "Majority required to ratify treaties on natural resources?", "options": ["Simple Majority", "Two-thirds of both Houses", "Unanimous", "Cabinet decision"], "answer": 1, "details": "Article 279.", "level": "Hard"},
    {"id": 84, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which Committee enforces Financial Accountability?", "options": ["State Affairs Committee", "Public Accounts Committee (PAC)", "Legislation Committee", "Development Committee"], "answer": 1, "details": "Reviews Auditor General reports.", "level": "Hard"},
    {"id": 85, "section": SYLLABUS_SECTIONS.LAW, "question": "'Pacta Sunt Servanda' means:", "options": ["Agreements must be kept", "Treaties are optional", "War is illegal", "Diplomacy first"], "answer": 0, "details": "Fundamental treaty law principle.", "level": "Hard"},
    {"id": 86, "section": SYLLABUS_SECTIONS.CONST, "question": "Are Directive Principles (Part 4) justiciable?", "options": ["Yes, in Supreme Court", "No", "Only Fundamental Duties", "Yes, in High Court"], "answer": 1, "details": "Article 55: Questions cannot be raised in court.", "level": "Hard"},
    {"id": 87, "section": SYLLABUS_SECTIONS.ADMIN, "question": "NPM (New Public Management) emphasizes:", "options": ["Strict rules", "Process over results", "The '3 Es' (Economy, Efficiency, Effectiveness)", "Centralization"], "answer": 2, "details": "Market-oriented administration.", "level": "Hard"},
    {"id": 88, "section": SYLLABUS_SECTIONS.CONST, "question": "Who acts as the final interpreter of the Constitution?", "options": ["Parliament", "President", "Supreme Court", "Constitutional Council"], "answer": 2, "details": "Article 128.", "level": "Hard"},
    {"id": 89, "section": SYLLABUS_SECTIONS.LAW, "question": "Double Jeopardy means:", "options": ["Tried twice for same offense", "Tried in two courts", "Punished twice", "Protection against being tried/punished for same offense"], "answer": 3, "details": "Article 20(6).", "level": "Hard"},
    {"id": 90, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which theory treats organization as a social system?", "options": ["Bureaucratic Theory", "Human Relations Theory", "Scientific Management", "Classical Theory"], "answer": 1, "details": "Elton Mayo.", "level": "Hard"},
    {"id": 91, "section": SYLLABUS_SECTIONS.CONST, "question": "Residual Powers are vested in:", "options": ["Local Level", "Province", "Federation", "Shared"], "answer": 2, "details": "Article 58.", "level": "Hard"},
    {"id": 92, "section": SYLLABUS_SECTIONS.LAW, "question": "Res Judicata prevents:", "options": ["Appeals", "Re-litigation of decided cases", "New evidence", "Transfers"], "answer": 1, "details": "Finality of judgment.", "level": "Hard"},
    {"id": 93, "section": SYLLABUS_SECTIONS.ADMIN, "question": "The 'Merit System' in civil service opposes:", "options": ["Competence", "Spoils System/Patronage", "Exams", "Neutrality"], "answer": 1, "details": "Selection based on ability, not politics.", "level": "Hard"},
    {"id": 94, "section": SYLLABUS_SECTIONS.CONST, "question": "Emergency Power duration (initial) if declared by President:", "options": ["1 Month", "3 Months", "6 Months", "1 Year"], "answer": 0, "details": "Must be approved by House within 1 month.", "level": "Hard"},
    {"id": 95, "section": SYLLABUS_SECTIONS.LAW, "question": "Which is NOT a general defense in Tort?", "options": ["Volenti non fit injuria", "Act of God", "Necessity", "Malice"], "answer": 3, "details": "Malice is an element of liability, not a defense.", "level": "Hard"},
    {"id": 96, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Who appoints the Chief Secretary?", "options": ["Public Service Commission", "Prime Minister", "Cabinet", "Minister of General Admin"], "answer": 2, "details": "Cabinet decision.", "level": "Hard"},
    {"id": 97, "section": SYLLABUS_SECTIONS.CONST, "question": "Inter-Provincial Council is chaired by:", "options": ["Home Minister", "President", "Prime Minister", "Senior CM"], "answer": 2, "details": "Article 234.", "level": "Hard"},
    {"id": 98, "section": SYLLABUS_SECTIONS.LAW, "question": "Specific Performance is a remedy in:", "options": ["Contract Law", "Criminal Law", "Tax Law", "Traffic Law"], "answer": 0, "details": "Compelling a party to fulfill the contract.", "level": "Hard"},
    {"id": 99, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Line vs Staff Agency: Staff Agency function is:", "options": ["Execution", "Decision making", "Advisory", "Public dealing"], "answer": 2, "details": "Line executes; Staff advises.", "level": "Hard"},
    {"id": 100, "section": SYLLABUS_SECTIONS.CONST, "question": "How many members in the National Assembly?", "options": ["59", "60", "110", "275"], "answer": 0, "details": "56 elected + 3 nominated.", "level": "Hard"},
    {"id": 101, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Span of Control refers to:", "options": ["Area of office", "Number of subordinates a superior can manage", "Length of service", "Power of Minister"], "answer": 1, "details": "Management principle.", "level": "Hard"},
    {"id": 102, "section": SYLLABUS_SECTIONS.LAW, "question": "Ignorantia juris non excusat means:", "options": ["Ignorance of fact is excuse", "Ignorance of law is no excuse", "Law is blind", "Judges are supreme"], "answer": 1, "details": "Universal legal maxim.", "level": "Hard"},
    {"id": 103, "section": SYLLABUS_SECTIONS.CONST, "question": "Who acts as the Secretariat of the Constitutional Council?", "options": ["Parliament Secretariat", "Office of President", "Office of PM (OPMCM)", "Supreme Court"], "answer": 2, "details": "Chief Secretary functions as secretary.", "level": "Hard"},
    {"id": 104, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which creates a 'Virtual Bureaucracy'?", "options": ["Red Tape", "E-Governance", "Decentralization", "Privatization"], "answer": 1, "details": "Digitized admin.", "level": "Hard"},
    {"id": 105, "section": SYLLABUS_SECTIONS.LAW, "question": "Jurisprudence is the study of:", "options": ["Jury selection", "Prison management", "Philosophy/Theory of Law", "Case files"], "answer": 2, "details": "Science of law.", "level": "Hard"},
    {"id": 106, "section": SYLLABUS_SECTIONS.CONST, "question": "Vote of Credit (Article 122) allows:", "options": ["Loans from bank", "Expenditure when budget is not passed", "Foreign aid", "Tax collection"], "answer": 1, "details": "Advance expenditure.", "level": "Hard"},
    {"id": 107, "section": SYLLABUS_SECTIONS.ADMIN, "question": "POSDCORB was coined by:", "options": ["Luther Gulick", "Max Weber", "Taylor", "Fayol"], "answer": 0, "details": "Acronym for admin functions.", "level": "Hard"},
    {"id": 108, "section": SYLLABUS_SECTIONS.LAW, "question": "Hostile Witness is one who:", "options": ["Attacks the judge", "Testifies against the party calling them", "Refuses to speak", "Lies"], "answer": 1, "details": "Adverse witness.", "level": "Hard"},
    {"id": 109, "section": SYLLABUS_SECTIONS.CONST, "question": "District Assembly consists of:", "options": ["All citizens", "Chair/Vice-Chair of Rural Municipalities + Mayor/Deputy Mayor", "MPs", "CDO and Police"], "answer": 1, "details": "Article 220.", "level": "Hard"},
    {"id": 110, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Red Tape implies:", "options": ["Fast service", "Efficient filing", "Excessive formalities/delay", "Digital records"], "answer": 2, "details": "Bureaucratic pathology.", "level": "Hard"},
    {"id": 111, "section": SYLLABUS_SECTIONS.LAW, "question": "Locus Standi means:", "options": ["Place of standing/Right to bring action", "Location of crime", "Stand up in court", "Local standard"], "answer": 0, "details": "Right to be heard.", "level": "Hard"},
    {"id": 112, "section": SYLLABUS_SECTIONS.CONST, "question": "Can the Army be mobilized without NSC recommendation?", "options": ["Yes, by PM", "Yes, by President", "No", "In war only"], "answer": 2, "details": "Article 267(6).", "level": "Hard"},
    {"id": 113, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Matrix Organization combines:", "options": ["Functional and Project structures", "Public and Private", "Central and Local", "Line and Staff"], "answer": 0, "details": "Dual reporting.", "level": "Hard"},
    {"id": 114, "section": SYLLABUS_SECTIONS.LAW, "question": "Obiter Dicta refers to:", "options": ["Binding decision", "Incidental remark/opinion of judge", "Final verdict", "The charge sheet"], "answer": 1, "details": "Not binding precedent.", "level": "Hard"},
    {"id": 115, "section": SYLLABUS_SECTIONS.CONST, "question": "Which commission handles Electoral Constituency Delimitation?", "options": ["Election Commission", "Constituency Delimitation Commission", "Parliament", "Supreme Court"], "answer": 1, "details": "Article 286.", "level": "Hard"},
    {"id": 116, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Hierarchy is known as:", "options": ["Scalar Chain", "Gang Plank", "Esprit de Corps", "Unity of Command"], "answer": 0, "details": "Chain of command.", "level": "Hard"},
    {"id": 117, "section": SYLLABUS_SECTIONS.LAW, "question": "Ex Post Facto Law is:", "options": ["Future law", "Retrospective criminal law (Prohibited)", "Civil law", "Foreign law"], "answer": 1, "details": "Article 20(4) prohibits it.", "level": "Hard"},
    {"id": 118, "section": SYLLABUS_SECTIONS.CONST, "question": "Constitutional Council is chaired by:", "options": ["President", "Chief Justice", "Prime Minister", "Speaker"], "answer": 2, "details": "Article 284.", "level": "Hard"},
    {"id": 119, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Parkinson's Law states:", "options": ["Work expands to fill time available", "Work contracts", "Admins are lazy", "Money is power"], "answer": 0, "details": "Bureaucratic expansion.", "level": "Hard"},
    {"id": 120, "section": SYLLABUS_SECTIONS.LAW, "question": "Natural Justice includes:", "options": ["Right to bias", "Rule against bias & Right to hearing", "Immediate jail", "No trial"], "answer": 1, "details": "Nemo judex in causa sua.", "level": "Hard"},
    {"id": 121, "section": SYLLABUS_SECTIONS.CONST, "question": "Who can remove a Provincial Governor?", "options": ["Provincial Assembly", "President", "Chief Minister", "High Court"], "answer": 1, "details": "Article 165.", "level": "Hard"},
    {"id": 122, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Unity of Command means:", "options": ["One boss for one subordinate", "Many bosses", "Team work", "Union power"], "answer": 0, "details": "Prevents confusion.", "level": "Hard"},
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

# --- MAIN APP ---
st.title("🇳🇵 Nepal Constitution & Governance Quiz")
st.markdown("**Practice your knowledge with real Loksewa-style questions**")

with st.sidebar:
    st.header("📊 Stats")
    st.metric("Score", st.session_state.score)
    st.metric("Progress", f"{st.session_state.current_index + 1}/{len(mcq_dataset)}")

if not st.session_state.quiz_started:
    st.markdown("### Ready to test your knowledge?")
    if st.button("Start Quiz 🚀", type="primary"):
        st.session_state.quiz_started = True
        st.rerun()
else:
    if st.session_state.current_index < len(mcq_dataset):
        q = mcq_dataset[st.session_state.current_index]
        
        st.markdown(f"### Question {q['id']}")
        st.markdown(f"**Section:** {q['section']} | **Level:** {q['level']}")
        st.markdown(f"#### {q['question']}")
        
        user_choice = st.radio("Choose your answer:", q['options'], key=f"q_{q['id']}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Submit Answer"):
                selected_idx = q['options'].index(user_choice)
                if selected_idx == q['answer']:
                    st.success("✅ Correct!")
                    st.info(f"**Details:** {q['details']}")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Wrong! Correct answer: {q['options'][q['answer']]}")
                    st.info(f"**Details:** {q['details']}")
                st.session_state.user_answers[q['id']] = selected_idx
        
        with col2:
            if st.button("Next Question →"):
                st.session_state.current_index += 1
                st.rerun()
    else:
        st.balloons()
        st.markdown("## 🎉 Quiz Complete!")
        st.metric("Final Score", f"{st.session_state.score}/{len(mcq_dataset)}")
        if st.button("Restart"):
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.user_answers = {}
            st.rerun()
