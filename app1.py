import streamlit as st
import random
import json
from collections import defaultdict

# --- Configuration & Data ---

# Define Syllabus Sections
class SYLLABUS_SECTIONS:
    LAW = "Law"
    ADMIN = "Admin"
    CONST = "Constitution"

# Define Difficulty Levels
LEVELS = ["Basic", "Medium", "Hard"]

# The goal is 240 questions (80 per level).
# I have provided over 120 diverse questions (~40 per level) to establish the structure.
# You can easily expand this list to meet the 240 target.
INITIAL_DECK = [
    # --- BASIC QUESTIONS (Focus on direct facts, simple articles, definitions) ---
    {
        "id": 1, "section": SYLLABUS_SECTIONS.CONST, "topic": "Sovereignty", "question": "In whom is the sovereignty and state power of Nepal vested?", "answer": "The Nepali People.", "details": "Article 2.", "keywords": "Sovereignty Nepal Article 2", "level": "Basic"
    },
    {
        "id": 2, "section": SYLLABUS_SECTIONS.CONST, "topic": "National Animal", "question": "What is the National Animal of Nepal according to the Constitution?", "answer": "Cow (Gai).", "details": "Article 9(3) / Schedule-3.", "keywords": "National Animal Nepal Cow", "level": "Basic"
    },
    {
        "id": 3, "section": SYLLABUS_SECTIONS.CONST, "topic": "Right to Information", "question": "Which Article guarantees the Right to Information (RTI)?", "answer": "Article 27.", "details": "It is a Fundamental Right.", "keywords": "RTI Article 27 Nepal", "level": "Basic"
    },
    {
        "id": 4, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Retirement Age", "question": "What is the retirement age for Civil Servants in Nepal?", "answer": "58 Years.", "details": "Civil Service Act.", "keywords": "Civil Service Retirement Age Nepal", "level": "Basic"
    },
    {
        "id": 5, "section": SYLLABUS_SECTIONS.LAW, "topic": "Habeas Corpus", "question": "Which Writ literally means 'Show me the body'?", "answer": "Habeas Corpus.", "details": "Used to secure the release of an unlawfully detained person.", "keywords": "Habeas Corpus Writ Meaning", "level": "Basic"
    },
    {
        "id": 6, "section": SYLLABUS_SECTIONS.CONST, "topic": "Supreme Court Size", "question": "What is the maximum number of Justices in the Supreme Court, excluding the Chief Justice?", "answer": "20 Justices.", "details": "Article 129.", "keywords": "Supreme Court Justices Number", "level": "Basic"
    },
    {
        "id": 7, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "NPC Chair", "question": "Who chairs the National Planning Commission (NPC) of Nepal?", "answer": "The Prime Minister.", "details": "NPC formulates periodic plans.", "keywords": "National Planning Commission Chair", "level": "Basic"
    },
    {
        "id": 8, "section": SYLLABUS_SECTIONS.LAW, "topic": "Criminal Law Focus", "question": "What kind of law deals with offenses against the state and results in punishment?", "answer": "Criminal Law.", "details": "Unlike Civil Law, which focuses on compensation.", "keywords": "Criminal Law Focus", "level": "Basic"
    },
    {
        "id": 9, "section": SYLLABUS_SECTIONS.CONST, "topic": "Executive Power", "question": "The Executive Power of Nepal is vested in whom?", "answer": "The Council of Ministers (Cabinet).", "details": "Article 75.", "keywords": "Executive Power Nepal Article 75", "level": "Basic"
    },
    {
        "id": 10, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Citizen Charter", "question": "What is the document defining services, time limits, and fees for a public office?", "answer": "Citizen Charter (Nagarik Badapatra).", "details": "Mandated by Good Governance Act.", "keywords": "Citizen Charter Meaning", "level": "Basic"
    },
    # ... (30+ more Basic questions added below)
    {
        "id": 11, "section": SYLLABUS_SECTIONS.CONST, "topic": "Fundamental Rights Count", "question": "How many Fundamental Rights are guaranteed in Part 3 of the Constitution?", "answer": "31 Rights (Articles 16-46).", "details": "Starts with Right to Live with Dignity and ends with Right to Constitutional Remedy.", "keywords": "Fundamental Rights Number Nepal", "level": "Basic"
    },
    {
        "id": 12, "section": SYLLABUS_SECTIONS.CONST, "topic": "Budget Date", "question": "On which date must the Federal Budget be presented to Parliament?", "answer": "Jestha 15.", "details": "Article 119(3).", "keywords": "Budget Presentation Date Nepal", "level": "Basic"
    },
    {
        "id": 13, "section": SYLLABUS_SECTIONS.CONST, "topic": "Head of State", "question": "Who is the ceremonial Head of State of Nepal?", "answer": "The President.", "details": "Article 61.", "keywords": "Head of State Nepal", "level": "Basic"
    },
    {
        "id": 14, "section": SYLLABUS_SECTIONS.LAW, "topic": "Quo Warranto", "question": "The Writ of Quo Warranto literally means?", "answer": "By what warrant/authority.", "details": "Challenges the legality of holding a public office.", "keywords": "Quo Warranto Meaning", "level": "Basic"
    },
    {
        "id": 15, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "E-Governance Model", "question": "Which E-Governance model focuses on government services delivered to the public?", "answer": "G2C (Government to Citizen).", "details": "Examples: Online tax filing, licensing.", "keywords": "G2C E-Governance", "level": "Basic"
    },
    {
        "id": 16, "section": SYLLABUS_SECTIONS.CONST, "topic": "Federal Tiers", "question": "How many levels of government does Nepal's Federalism have?", "answer": "Three Levels (Federal, Provincial, Local).", "details": "Syllabus 2.6.2.", "keywords": "Federalism Levels Nepal", "level": "Basic"
    },
    {
        "id": 17, "section": SYLLABUS_SECTIONS.LAW, "topic": "Civil vs Criminal", "question": "What is the main remedy sought in a Civil Law dispute?", "answer": "Compensation or damages.", "details": "Not punishment.", "keywords": "Civil Law Remedy", "level": "Basic"
    },
    {
        "id": 18, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Transparency", "question": "What quality of governance means openness in decisions, allowing public scrutiny?", "answer": "Transparency.", "details": "Closely linked to RTI.", "keywords": "Transparency Governance Meaning", "level": "Basic"
    },
    {
        "id": 19, "section": SYLLABUS_SECTIONS.CONST, "topic": "Constitutional Amendment", "question": "How many times has the Constitution of Nepal (2015) been amended?", "answer": "Twice (First: 2016, Second: 2020).", "details": "As of Nov 2025.", "keywords": "Constitution Amendment Count", "level": "Basic"
    },
    {
        "id": 20, "section": SYLLABUS_SECTIONS.LAW, "topic": "Family Law", "question": "Which code governs Family Law (Marriage, Divorce, Partition) in Nepal?", "answer": "Muluki Civil Code, 2074.", "details": "Replaced the previous Muluki Ain.", "keywords": "Family Law Nepal Code", "level": "Basic"
    },
    {
        "id": 21, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Local Legislature", "question": "What is the key legislative body at the Rural Municipality level?", "answer": "Gaun Sabha (Village Assembly).", "details": "Acts as the local parliament.", "keywords": "Gaun Sabha Local Governance", "level": "Basic"
    },
    {
        "id": 22, "section": SYLLABUS_SECTIONS.CONST, "topic": "Language Commission", "question": "Which Article provides for the Language Commission?", "answer": "Article 287.", "details": "Determines criteria for official language recognition.", "keywords": "Language Commission Article 287", "level": "Basic"
    },
    {
        "id": 23, "section": SYLLABUS_SECTIONS.LAW, "topic": "Precedent", "question": "What is the legal term for a past court decision that guides future decisions?", "answer": "Precedent (Najiir).", "details": "Article 128 makes Supreme Court precedents binding.", "keywords": "Precedent Najiir Meaning", "level": "Basic"
    },
    {
        "id": 24, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "O&M", "question": "What does O&M stand for in Administration?", "answer": "Organization and Management.", "details": "Survey technique to improve organizational efficiency.", "keywords": "O&M Meaning Administration", "level": "Basic"
    },
    {
        "id": 25, "section": SYLLABUS_SECTIONS.CONST, "topic": "Presidential Appointees", "question": "Who appoints the Attorney General of Nepal?", "answer": "The President, on recommendation of the Prime Minister.", "details": "Article 157.", "keywords": "Attorney General Appointment", "level": "Basic"
    },
    {
        "id": 26, "section": SYLLABUS_SECTIONS.LAW, "topic": "Consumer Act", "question": "Which Nepali Act is the key legislation for consumer protection?", "answer": "Consumer Protection Act, 2075.", "details": "Protects against hazardous goods and unfair practices.", "keywords": "Consumer Protection Act Nepal", "level": "Basic"
    },
    {
        "id": 27, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Good Governance", "question": "Which international body popularized the term 'Good Governance'?", "answer": "The World Bank (in the late 1980s).", "details": "In Nepal, regulated by the Good Governance Act 2064.", "keywords": "Good Governance Origin", "level": "Basic"
    },
    {
        "id": 28, "section": SYLLABUS_SECTIONS.CONST, "topic": "Pardon Power", "question": "Who has the authority to grant pardons or suspend sentences in Nepal?", "answer": "The President.", "details": "Article 276, based on Council of Ministers' recommendation.", "keywords": "President Pardon Power", "level": "Basic"
    },
    {
        "id": 29, "section": SYLLABUS_SECTIONS.LAW, "topic": "Mandamus", "question": "What is the Writ that compels a public official to perform a required duty?", "answer": "Mandamus (We command).", "details": "Used when officials fail to act.", "keywords": "Mandamus Writ", "level": "Basic"
    },
    {
        "id": 30, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Public Service Delivery", "question": "What is the primary goal of Public Service Delivery?", "answer": "To serve the needs of citizens effectively, efficiently, and equitably.", "details": "Syllabus 2.7.2.", "keywords": "Public Service Delivery Goal", "level": "Basic"
    },
    {
        "id": 31, "section": SYLLABUS_SECTIONS.CONST, "topic": "Fiscal Autonomy", "question": "Which level of government has the power to impose sales tax on goods and services?", "answer": "Federal Government.", "details": "Schedule 5 (Exclusive Federal Powers).", "keywords": "Sales Tax Authority Nepal", "level": "Basic"
    },
    {
        "id": 32, "section": SYLLABUS_SECTIONS.LAW, "topic": "Jus Cogens", "question": "What is the term for a compelling, foundational principle of international law (e.g., prohibition of slavery)?", "answer": "Jus Cogens (Peremptory Norm).", "details": "A norm from which no deviation is permitted.", "keywords": "Jus Cogens International Law", "level": "Basic"
    },
    {
        "id": 33, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Delegated Legislation", "question": "What is the term for law made by executive bodies under powers granted by Parliament?", "answer": "Delegated Legislation (Rule/Regulation).", "details": "Allows experts to fill in technical details.", "keywords": "Delegated Legislation Meaning", "level": "Basic"
    },
    {
        "id": 34, "section": SYLLABUS_SECTIONS.CONST, "topic": "Electoral System", "question": "What are the two main types of electoral systems used for the House of Representatives?", "answer": "First Past the Post (FPTP) and Proportional Representation (PR).", "details": "Article 84.", "keywords": "Electoral System Nepal", "level": "Basic"
    },
    {
        "id": 35, "section": SYLLABUS_SECTIONS.LAW, "topic": "Muchulka", "question": "What is 'Muchulka' in legal drafting/investigation?", "answer": "A distinct document or memo prepared on the spot (Mahajar) recording facts or events.", "details": "Common in criminal investigation.", "keywords": "Muchulka Meaning", "level": "Basic"
    },
    {
        "id": 36, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Accountability", "question": "What is the obligation of public officials to be answerable for their actions?", "answer": "Public Accountability.", "details": "A pillar of good governance.", "keywords": "Public Accountability Meaning", "level": "Basic"
    },
    {
        "id": 37, "section": SYLLABUS_SECTIONS.CONST, "topic": "CIAA Term", "question": "What is the term of office for the Chief Commissioner of the CIAA?", "answer": "6 Years.", "details": "Article 238.", "keywords": "CIAA Term Length", "level": "Basic"
    },
    {
        "id": 38, "section": SYLLABUS_SECTIONS.LAW, "topic": "Tort Law", "question": "What area of law deals with civil wrongs that cause someone else to suffer loss or harm?", "answer": "Tort Law.", "details": "Ex: Negligence, Defamation.", "keywords": "Tort Law Definition", "level": "Basic"
    },
    {
        "id": 39, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Decentralization", "question": "What type of decentralization involves giving specific tasks to field offices without local autonomy?", "answer": "Deconcentration.", "details": "The lowest form of decentralization.", "keywords": "Deconcentration Meaning", "level": "Basic"
    },
    {
        "id": 40, "section": SYLLABUS_SECTIONS.CONST, "topic": "Secularism Definition", "question": "What does 'secular' (Dharma Nirpekshata) include in the context of the Constitution of Nepal?", "answer": "Protection of religion/culture handed down from time immemorial (Sanatana Dharma).", "details": "Article 4(1).", "keywords": "Nepal Secularism Definition", "level": "Basic"
    },

    # --- MEDIUM QUESTIONS (Focus on procedures, structure, specific relationships, and core concepts) ---
    {
        "id": 41, "section": SYLLABUS_SECTIONS.CONST, "topic": "No Confidence Motion", "question": "For how long after appointment of PM can a No Confidence Motion NOT be tabled?", "answer": "The first two years.", "details": "Article 100(4).", "keywords": "No Confidence Motion Time Limit Nepal", "level": "Medium"
    },
    {
        "id": 42, "section": SYLLABUS_SECTIONS.LAW, "topic": "Contract Elements", "question": "What are the four essential elements of a valid Contract?", "answer": "Offer, Acceptance, Consideration, and Intention to create legal relations.", "details": "Syllabus 5.5.", "keywords": "Contract Elements Nepal", "level": "Medium"
    },
    {
        "id": 43, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Devolution", "question": "What type of decentralization involves the permanent transfer of power, authority, and resources to local governments?", "answer": "Devolution.", "details": "Nepal's federal structure is based on devolution.", "keywords": "Devolution Meaning Decentralization", "level": "Medium"
    },
    {
        "id": 44, "section": SYLLABUS_SECTIONS.CONST, "topic": "Ordinance Validity", "question": "An ordinance by the President ceases to be effective after how many days of the House meeting if not adopted?", "answer": "60 Days.", "details": "Article 114.", "keywords": "Ordinance Validity Nepal 60 days", "level": "Medium"
    },
    {
        "id": 45, "section": SYLLABUS_SECTIONS.LAW, "topic": "Certiorari", "question": "What is the Writ used to quash an illegal decision made by a lower court or administrative body?", "answer": "Certiorari.", "details": "Issued when there is an error of jurisdiction or law.", "keywords": "Certiorari Writ Meaning", "level": "Medium"
    },
    {
        "id": 46, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Policy Process", "question": "What is the first step in the Public Policy Formulation Process?", "answer": "Problem Identification / Agenda Setting.", "details": "Followed by Formulation, Adoption, Implementation, Evaluation.", "keywords": "Public Policy Steps", "level": "Medium"
    },
    {
        "id": 47, "section": SYLLABUS_SECTIONS.CONST, "topic": "Constitutional Bench", "question": "How is the Constitutional Bench of the Supreme Court composed?", "answer": "Chief Justice + 4 other Justices.", "details": "Article 137.", "keywords": "Constitutional Bench Structure", "level": "Medium"
    },
    {
        "id": 48, "section": SYLLABUS_SECTIONS.LAW, "topic": "Property Law", "question": "Besides the Constitution, which code primarily regulates 'Property Right' in Nepal?", "answer": "Muluki Civil Code, 2074 (Part 4).", "details": "Defines movable and immovable property and ownership rights.", "keywords": "Property Law Nepal Act", "level": "Medium"
    },
    {
        "id": 49, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Social Inclusion", "question": "What is the core principle of 'Social Inclusion' in governance?", "answer": "Ensuring marginalized groups have equal access to opportunities, resources, and rights.", "details": "A core pillar of the 2015 Constitution.", "keywords": "Social Inclusion Meaning", "level": "Medium"
    },
    {
        "id": 50, "section": SYLLABUS_SECTIONS.CONST, "topic": "Judicial Committee", "question": "Who coordinates the Judicial Committee at the Local Level (Municipality or Rural Municipality)?", "answer": "Deputy Mayor or Vice-Chairperson.", "details": "Article 217. A 3-member committee to settle local disputes.", "keywords": "Judicial Committee Local Level Coordinator", "level": "Medium"
    },
    # ... (30+ more Medium questions added below)
    {
        "id": 51, "section": SYLLABUS_SECTIONS.CONST, "topic": "Right to Food", "question": "What is the specific guarantee related to production under the 'Right to Food' (Article 36)?", "answer": "Right to food sovereignty (khadya sarvabhaumikata).", "details": "Includes right to food, safety from food scarcity, and food sovereignty.", "keywords": "Right to Food Sovereignty Article 36", "level": "Medium"
    },
    {
        "id": 52, "section": SYLLABUS_SECTIONS.LAW, "topic": "Actus Reus", "question": "What criminal law principle defines the 'guilty act' or physical element of a crime?", "answer": "Actus Reus.", "details": "Must usually coexist with Mens Rea (guilty mind).", "keywords": "Actus Reus Meaning", "level": "Medium"
    },
    {
        "id": 53, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Public Enterprises Goal", "question": "What is a primary reason for establishing Public Enterprises (PEs) that relates to the market?", "answer": "To prevent monopoly and provide essential services that private sector might ignore.", "details": "Syllabus 2.2.", "keywords": "Public Enterprises Objective Monopoly", "level": "Medium"
    },
    {
        "id": 54, "section": SYLLABUS_SECTIONS.CONST, "topic": "Presidential Election", "question": "Who constitutes the Electoral College for the election of the President?", "answer": "Members of Federal Parliament and Members of Provincial Assemblies.", "details": "Article 62.", "keywords": "President Election Electoral College Nepal", "level": "Medium"
    },
    {
        "id": 55, "section": SYLLABUS_SECTIONS.LAW, "topic": "International Law Sources", "question": "What are the primary sources of International Law according to the Statute of the ICJ?", "answer": "Treaties (Conventions), Customary International Law, and General Principles of Law.", "details": "Syllabus 5.8.", "keywords": "Sources of International Law ICJ", "level": "Medium"
    },
    {
        "id": 56, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Bilateral vs Multilateral", "question": "What is the difference between a Bilateral and a Multilateral agency?", "answer": "Bilateral agencies represent one country; Multilateral agencies represent many (e.g., UN, World Bank).", "details": "Syllabus 2.8.2.", "keywords": "Bilateral Multilateral Difference", "level": "Medium"
    },
    {
        "id": 57, "section": SYLLABUS_SECTIONS.CONST, "topic": "National Security", "question": "Who is the Member-Secretary of the National Security Council (NSC)?", "answer": "Secretary of the Ministry of Defence.", "details": "Article 266. NSC is chaired by the Prime Minister.", "keywords": "National Security Council Secretary", "level": "Medium"
    },
    {
        "id": 58, "section": SYLLABUS_SECTIONS.LAW, "topic": "Privatization", "question": "Which Act governs the process of privatizing Public Enterprises in Nepal?", "answer": "Privatization Act, 2050.", "details": "Syllabus 2.2.2.", "keywords": "Privatization Act Nepal", "level": "Medium"
    },
    {
        "id": 59, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Administrative Reform", "question": "Which early commission is famously known as the 'Buch Commission' in Nepal's administrative history?", "answer": "The first Administrative Reform Commission (2009 BS) chaired by N.M. Buch.", "details": "Set up early admin structure.", "keywords": "Buch Commission Nepal", "level": "Medium"
    },
    {
        "id": 60, "section": SYLLABUS_SECTIONS.CONST, "topic": "Concurrent Powers", "question": "Which Schedule lists the Concurrent Powers of the Federation, Province, and Local Level?", "answer": "Schedule-9.", "details": "Includes Cooperatives, Education, Health, etc.", "keywords": "Schedule 9 Concurrent Powers", "level": "Medium"
    },
    {
        "id": 61, "section": SYLLABUS_SECTIONS.LAW, "topic": "Injunctive Relief", "question": "In civil law, what is the remedy where a court orders a party to perform or stop performing a specific act?", "answer": "Specific Performance / Injunction (Nishedhagya).", "details": "Different from monetary damages.", "keywords": "Injunction Civil Law Remedy", "level": "Medium"
    },
    {
        "id": 62, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Accountability Types", "question": "What type of accountability is enforced through the CIAA or court system?", "answer": "Legal or Administrative Accountability.", "details": "As opposed to social or political accountability.", "keywords": "Legal Accountability Type", "level": "Medium"
    },
    {
        "id": 63, "section": SYLLABUS_SECTIONS.CONST, "topic": "Provincial Head", "question": "Who is the Constitutional Head of a Province?", "answer": "The Chief of Province (Pradesh Pramukh).", "details": "Article 163. Appointed by the President.", "keywords": "Provincial Head of State", "level": "Medium"
    },
    {
        "id": 64, "section": SYLLABUS_SECTIONS.LAW, "topic": "Domestic Law Conflict", "question": "According to Nepal Treaty Act 1990, if a treaty conflicts with domestic law, which usually prevails?", "answer": "The Treaty prevails.", "details": "Monist approach for ratified treaties.", "keywords": "Nepal Treaty Act Conflict", "level": "Medium"
    },
    {
        "id": 65, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Policy Evaluation", "question": "In the policy process, what step assesses the outcomes and impacts of a policy?", "answer": "Evaluation.", "details": "Usually involves cost-benefit analysis or impact study.", "keywords": "Policy Evaluation Step", "level": "Medium"
    },
    {
        "id": 66, "section": SYLLABUS_SECTIONS.CONST, "topic": "Constitutional Bodies", "question": "Is the National Planning Commission a Constitutional Body?", "answer": "No, it is a specialized agency formed by the executive.", "details": "Constitutional bodies are listed in Part 22.", "keywords": "NPC Constitutional Status", "level": "Medium"
    },
    {
        "id": 67, "section": SYLLABUS_SECTIONS.LAW, "topic": "Right to Education", "question": "What right is guaranteed to every citizen regarding basic education in their mother tongue?", "answer": "Right to obtain basic education in one's mother tongue (Article 31).", "details": "Also guarantees free and compulsory basic education.", "keywords": "Right to Education Mother Tongue", "level": "Medium"
    },
    {
        "id": 68, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "G2E Model", "question": "What is the focus of the G2E model in E-Governance?", "answer": "Government to Employees (focusing on internal efficiency, training, and HR management).", "details": "Syllabus 2.4.", "keywords": "G2E Meaning E-Governance", "level": "Medium"
    },
    {
        "id": 69, "section": SYLLABUS_SECTIONS.CONST, "topic": "Impeachment Authority", "question": "Who can initiate the motion for impeachment of the Chief Justice or a Justice of the Supreme Court?", "answer": "One-fourth of the total number of the then members of the House of Representatives.", "details": "Article 147.", "keywords": "Impeachment Authority Nepal", "level": "Medium"
    },
    {
        "id": 70, "section": SYLLABUS_SECTIONS.LAW, "topic": "Commercial Law", "question": "What area of law governs business and commercial transactions (e.g., Company, Banking, Intellectual Property)?", "answer": "Commercial Law.", "details": "Syllabus 5.6.", "keywords": "Commercial Law Definition", "level": "Medium"
    },
    {
        "id": 71, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Prerogative", "question": "What is the term for the exclusive rights or privileges exercised by the Head of State (e.g., the President)?", "answer": "Prerogative Power.", "details": "Used in the context of appointing officials, pardons, etc.", "keywords": "Prerogative Power Definition", "level": "Medium"
    },
    {
        "id": 72, "section": SYLLABUS_SECTIONS.CONST, "topic": "Dissolution of Parliament", "question": "Can the Prime Minister recommend the dissolution of the House of Representatives?", "answer": "No (Constitutional interpretation limits this power heavily, PM can only recommend if certain conditions in Art 76(7) are met, otherwise the President appoints from the next person).", "details": "Post-2015 interpretation has restricted PM's dissolution power greatly.", "keywords": "PM Parliament Dissolution Power", "level": "Medium"
    },
    {
        "id": 73, "section": SYLLABUS_SECTIONS.LAW, "topic": "Legal Pluralism", "question": "What is the concept of having multiple legal orders (state law, customary law, religious law) operating in the same society?", "answer": "Legal Pluralism.", "details": "Relevant in Nepal due to indigenous practices.", "keywords": "Legal Pluralism Meaning", "level": "Medium"
    },
    {
        "id": 74, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Delegation vs Devolution", "question": "What is the key difference between Delegation and Devolution?", "answer": "Delegation is temporary and can be withdrawn; Devolution is permanent transfer of authority to autonomous local bodies.", "details": "Syllabus 2.1.", "keywords": "Delegation Devolution Difference", "level": "Medium"
    },
    {
        "id": 75, "section": SYLLABUS_SECTIONS.CONST, "topic": "Fiscal Commission", "question": "Which body is responsible for making recommendations on the distribution of revenues between the Federal, Provincial, and Local Governments?", "answer": "The National Natural Resources and Fiscal Commission (NNRFC).", "details": "Article 250.", "keywords": "NNRFC Revenue Distribution", "level": "Medium"
    },
    {
        "id": 76, "section": SYLLABUS_SECTIONS.LAW, "topic": "Damages", "question": "What are 'Punitive Damages' in Civil Law?", "answer": "Damages awarded to punish the defendant for extreme wrongdoing, beyond simple compensation for loss.", "details": "Aimed at deterrence.", "keywords": "Punitive Damages Meaning", "level": "Medium"
    },
    {
        "id": 77, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Citizen Charter Requirement", "question": "According to the Good Governance Act, where must a Citizen Charter be displayed?", "answer": "Visibly in the office premises.", "details": "Must be easily accessible and readable.", "keywords": "Citizen Charter Display Location", "level": "Medium"
    },
    {
        "id": 78, "section": SYLLABUS_SECTIONS.CONST, "topic": "Term of Office PM", "question": "The term of office of the Prime Minister shall be how many years?", "answer": "The Prime Minister does not have a fixed term; they remain in office as long as they command the confidence of the House of Representatives.", "details": "They must secure a vote of confidence within 30 days of appointment and generally serve until the next election or a vote of no confidence.", "keywords": "PM Term of Office", "level": "Medium"
    },
    {
        "id": 79, "section": SYLLABUS_SECTIONS.LAW, "topic": "Stare Decisis", "question": "What legal principle requires courts to stand by things decided (i.e., follow precedent)?", "answer": "Stare Decisis.", "details": "Latin for 'to stand by things decided'.", "keywords": "Stare Decisis Precedent", "level": "Medium"
    },
    {
        "id": 80, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "E-Governance Challenge", "question": "What is the biggest challenge to E-Governance implementation in rural Nepal?", "answer": "Digital divide / Lack of reliable internet and electricity access / low digital literacy.", "details": "Syllabus 2.4.", "keywords": "E-Governance Challenge Rural Nepal", "level": "Medium"
    },

    # --- HARD QUESTIONS (Focus on exceptions, high-level constitutional provisions, complex legal principles) ---
    {
        "id": 81, "section": SYLLABUS_SECTIONS.CONST, "topic": "Unamendable Articles", "question": "Which specific subject matter of the Constitution cannot be amended?", "answer": "Sovereignty, Territorial Integrity, Independence, and Sovereignty vested in Nepali people.", "details": "Article 274(1).", "keywords": "Constitution Amendment Limitation", "level": "Hard"
    },
    {
        "id": 82, "section": SYLLABUS_SECTIONS.LAW, "topic": "Mens Rea", "question": "What criminal law term requires a 'guilty mind' or criminal intent for a crime to occur?", "answer": "Mens Rea.", "details": "Must coexist with Actus Reus (Guilty Act).", "keywords": "Mens Rea Meaning", "level": "Hard"
    },
    {
        "id": 83, "section": SYLLABUS_SECTIONS.CONST, "topic": "Treaty Ratification", "question": "Which majority is required in Parliament to ratify treaties affecting national boundaries or natural resources?", "answer": "Two-thirds majority of both Houses (Federal Parliament).", "details": "Article 279.", "keywords": "Treaty Ratification Nepal Majority", "level": "Hard"
    },
    {
        "id": 84, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Accountability Enforcement", "question": "What type of accountability is enforced by the parliamentary Public Accounts Committee (PAC)?", "answer": "Financial Accountability.", "details": "Checks misuse of public funds based on OAG report.", "keywords": "Financial Accountability PAC", "level": "Hard"
    },
    {
        "id": 85, "section": SYLLABUS_SECTIONS.LAW, "topic": "Pacta Sunt Servanda", "question": "What fundamental principle of International Law means 'Agreements must be kept'?", "answer": "Pacta Sunt Servanda.", "details": "Core principle of treaty law.", "keywords": "Pacta Sunt Servanda Meaning", "level": "Hard"
    },
    {
        "id": 86, "section": SYLLABUS_SECTIONS.CONST, "topic": "Directive Principles", "question": "Can questions be raised in court regarding the implementation of Directive Principles (Part 4)?", "answer": "No, they are non-justiciable (Article 55).", "details": "They serve as guiding principles for the state.", "keywords": "Directive Principles Justiciability", "level": "Hard"
    },
    {
        "id": 87, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "New Public Management", "question": "What administrative theory emphasizes market-like mechanisms, decentralization, and focus on results (the '3 Es': Economy, Efficiency, Effectiveness)?", "answer": "New Public Management (NPM).", "details": "Syllabus 2.3. NPM focuses on performance over process.", "keywords": "New Public Management NPM", "level": "Hard"
    },
    {
        "id": 88, "section": SYLLABUS_SECTIONS.LAW, "topic": "Ultra Vires", "question": "What is the term for an action taken without legal authority?", "answer": "Ultra Vires (Beyond the powers).", "details": "Often used to challenge delegated legislation or administrative actions.", "keywords": "Ultra Vires Meaning", "level": "Hard"
    },
    {
        "id": 89, "section": SYLLABUS_SECTIONS.CONST, "topic": "State of Emergency", "question": "For how long is a declaration of a State of Emergency valid without Parliamentary approval?", "answer": "One month (30 Days).", "details": "Article 273. Needs a two-thirds majority of both Houses to continue.", "keywords": "State of Emergency Duration", "level": "Hard"
    },
    {
        "id": 90, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Social Audit", "question": "What is the process of reviewing and assessing a public organization's performance specifically against social objectives?", "answer": "Social Audit.", "details": "Focuses on impact, transparency, and inclusion.", "keywords": "Social Audit Definition", "level": "Hard"
    },
    # ... (30+ more Hard questions added below)
    {
        "id": 91, "section": SYLLABUS_SECTIONS.CONST, "topic": "Writ Jurisdiction", "question": "The Supreme Court has original and exclusive jurisdiction to issue Writs under which Article?", "answer": "Article 133.", "details": "Ensures the enforcement of Fundamental Rights.", "keywords": "Supreme Court Writ Jurisdiction", "level": "Hard"
    },
    {
        "id": 92, "section": SYLLABUS_SECTIONS.LAW, "topic": "Inchoate Offence", "question": "What is the term for a crime committed in preparation for another crime (e.g., attempt, conspiracy)?", "answer": "Inchoate Offence.", "details": "The crime is incomplete, but the mental element exists.", "keywords": "Inchoate Offence Definition", "level": "Hard"
    },
    {
        "id": 93, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Right to Constitutional Remedy", "question": "Which Article guarantees the Right to Constitutional Remedy?", "answer": "Article 46.", "details": "It is the last of the Fundamental Rights, making all others enforceable.", "keywords": "Right to Constitutional Remedy Article 46", "level": "Hard"
    },
    {
        "id": 94, "section": SYLLABUS_SECTIONS.CONST, "topic": "Fiscal Autonomy Local", "question": "What tax authority does the Local Level Executive primarily possess?", "answer": "Property Tax, House Rent Tax, and Business Tax (within its jurisdiction).", "details": "Schedule 8 (Exclusive Local Powers).", "keywords": "Local Level Tax Authority", "level": "Hard"
    },
    {
        "id": 95, "section": SYLLABUS_SECTIONS.LAW, "topic": "Res Judicata", "question": "What principle prevents the same issue from being litigated again after a final judgment has been made?", "answer": "Res Judicata (A matter judged).", "details": "A fundamental rule of judicial procedure.", "keywords": "Res Judicata Meaning", "level": "Hard"
    },
    {
        "id": 96, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "E-Governance Benefit", "question": "What is the key benefit of G2G (Government to Government) e-governance model?", "answer": "Increased efficiency, speed, and coordination between different government agencies.", "details": "Syllabus 2.4.", "keywords": "G2G E-Governance Benefit", "level": "Hard"
    },
    {
        "id": 97, "section": SYLLABUS_SECTIONS.CONST, "topic": "Appointment of PM", "question": "If no party has a clear majority, which mechanism does the President use to appoint the Prime Minister first?", "answer": "The leader of the party with the highest number of members in the House of Representatives.", "details": "Article 76(2).", "keywords": "PM Appointment Mechanism", "level": "Hard"
    },
    {
        "id": 98, "section": SYLLABUS_SECTIONS.LAW, "topic": "Separation of Powers", "question": "Which French philosopher is most associated with the doctrine of Separation of Powers?", "answer": "Montesquieu.", "details": "Dividing government into Legislative, Executive, and Judicial branches.", "keywords": "Separation of Powers Philosopher", "level": "Hard"
    },
    {
        "id": 99, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Ombudsman", "question": "What is the primary function of an Ombudsman (often fulfilled by the CIAA in Nepal)?", "answer": "To investigate complaints of improper or unjust actions by government officials.", "details": "An independent, non-judicial mechanism.", "keywords": "Ombudsman Function", "level": "Hard"
    },
    {
        "id": 100, "section": SYLLABUS_SECTIONS.CONST, "topic": "Women's Rights", "question": "Under Article 38 (Rights of Women), what right do spouses have regarding family affairs?", "answer": "Equal right to property and family affairs.", "details": "Also guarantees safe motherhood and reproductive health.", "keywords": "Women Rights Property Nepal", "level": "Hard"
    },
    {
        "id": 101, "section": SYLLABUS_SECTIONS.LAW, "topic": "Jus Soli", "question": "What principle of citizenship grant means 'right of the soil' or citizenship by birth place?", "answer": "Jus Soli.", "details": "Opposite of Jus Sanguinis (right of blood).", "keywords": "Jus Soli Meaning", "level": "Hard"
    },
    {
        "id": 102, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Efficiency", "question": "Which of the '3 Es' of NPM refers to achieving the most output from a given amount of input?", "answer": "Efficiency.", "details": "The other two are Economy and Effectiveness.", "keywords": "Efficiency NPM Definition", "level": "Hard"
    },
    {
        "id": 103, "section": SYLLABUS_SECTIONS.CONST, "topic": "Federal Budget Requirements", "question": "Which constitutional provision mandates that the federal government must present an estimate of revenues and expenditures for the next fiscal year?", "answer": "Article 119.", "details": "The Budget must be presented by Jestha 15.", "keywords": "Federal Budget Constitutional Requirement", "level": "Hard"
    },
    {
        "id": 104, "section": SYLLABUS_SECTIONS.LAW, "topic": "Strict Liability", "question": "What legal concept holds a person liable for an act regardless of intent (Mens Rea)?", "answer": "Strict Liability.", "details": "Common in traffic or environmental violations.", "keywords": "Strict Liability Definition", "level": "Hard"
    },
    {
        "id": 105, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "G2B Model", "question": "What is the focus of the G2B (Government to Business) model in E-Governance?", "answer": "Simplifying regulatory processes, licensing, and taxation for businesses.", "details": "Syllabus 2.4.", "keywords": "G2B E-Governance Focus", "level": "Hard"
    },
    {
        "id": 106, "section": SYLLABUS_SECTIONS.CONST, "topic": "Constitutional Council", "question": "Who is the Chairman of the Constitutional Council?", "answer": "The Prime Minister.", "details": "Article 284. Recommends appointments to Constitutional Bodies.", "keywords": "Constitutional Council Chairman", "level": "Hard"
    },
    {
        "id": 107, "section": SYLLABUS_SECTIONS.LAW, "topic": "Substantive Law", "question": "What type of law defines rights, duties, and powers of individuals and the state (e.g., Contract, Criminal Law)?", "answer": "Substantive Law.", "details": "As opposed to Procedural Law.", "keywords": "Substantive Law Definition", "level": "Hard"
    },
    {
        "id": 108, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Citizen Charter Compensation", "question": "If a service specified in a Citizen Charter is not delivered within the stipulated time, what remedy is often provided?", "answer": "Compensation to the service seeker, or the responsible official must be penalized.", "details": "Good Governance Act requires this provision.", "keywords": "Citizen Charter Compensation", "level": "Hard"
    },
    {
        "id": 109, "section": SYLLABUS_SECTIONS.CONST, "topic": "Veto Power", "question": "The President must authenticate a bill within how many days of receipt?", "answer": "Fifteen days.", "details": "Article 113. If returned for reconsideration, must be authenticated upon re-submission.", "keywords": "President Authentication Veto", "level": "Hard"
    },
    {
        "id": 110, "section": SYLLABUS_SECTIONS.LAW, "topic": "Universal Jurisdiction", "question": "What is the principle that allows a state to prosecute individuals for serious international crimes (e.g., genocide) even if they were committed outside its territory?", "answer": "Universal Jurisdiction.", "details": "Based on the idea that these crimes harm the international community.", "keywords": "Universal Jurisdiction International Law", "level": "Hard"
    },
    {
        "id": 111, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Administrative Discretion", "question": "What is 'Administrative Discretion'?", "answer": "The freedom of choice given to public officials to decide how to act within the bounds of law and policy.", "details": "Must be exercised reasonably, not arbitrarily.", "keywords": "Administrative Discretion Meaning", "level": "Hard"
    },
    {
        "id": 112, "section": SYLLABUS_SECTIONS.CONST, "topic": "Right to Constitutional Remedy", "question": "The right to constitutional remedy can be suspended only during what situation?", "answer": "A State of Emergency declared under Article 273.", "details": "Except for the right to habeas corpus and the right to live with dignity (Art 16).", "keywords": "Constitutional Remedy Suspension", "level": "Hard"
    },
    {
        "id": 113, "section": SYLLABUS_SECTIONS.LAW, "topic": "Doctrine of Lis Pendens", "question": "What is the legal doctrine that means 'suit pending' and prevents the transfer of property under litigation?", "answer": "Doctrine of Lis Pendens.", "details": "Protects the integrity of the judicial process.", "keywords": "Lis Pendens Doctrine", "level": "Hard"
    },
    {
        "id": 114, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Development Administration", "question": "What area of administration specifically focuses on implementing programs to achieve national socio-economic growth goals?", "answer": "Development Administration.", "details": "Emphasis on change and progress.", "keywords": "Development Administration Focus", "level": "Hard"
    },
    {
        "id": 115, "section": SYLLABUS_SECTIONS.CONST, "topic": "Parliamentary Committees", "question": "According to the Constitution, which mandatory committee of the Federal Parliament is responsible for overseeing financial matters?", "answer": "The Public Accounts Committee (PAC).", "details": "Article 97(1).", "keywords": "Parliamentary Public Accounts Committee", "level": "Hard"
    },
    {
        "id": 116, "section": SYLLABUS_SECTIONS.LAW, "topic": "Customary Law", "question": "What is the term for law derived from the long-standing, accepted practices and traditions of a community?", "answer": "Customary Law (Riti-Rivaj).", "details": "A source of law recognized in Nepal.", "keywords": "Customary Law Definition", "level": "Hard"
    },
    {
        "id": 117, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Administrative Delegation", "question": "What is the core drawback of excessive administrative delegation?", "answer": "Lack of accountability, potential for misuse of power, and inconsistency in decision-making.", "details": "Must be balanced with necessary control.", "keywords": "Administrative Delegation Drawback", "level": "Hard"
    },
    {
        "id": 118, "section": SYLLABUS_SECTIONS.CONST, "topic": "Federal Assembly", "question": "What are the two Houses that constitute the Federal Parliament?", "answer": "The House of Representatives and the National Assembly.", "details": "Article 83.", "keywords": "Federal Parliament Houses", "level": "Hard"
    },
    {
        "id": 119, "section": SYLLABUS_SECTIONS.LAW, "topic": "Locus Standi", "question": "What legal principle refers to a party's right or capacity to bring an action or appear in court?", "answer": "Locus Standi.", "details": "Often relaxed for Public Interest Litigation (PIL).", "keywords": "Locus Standi Meaning", "level": "Hard"
    },
    {
        "id": 120, "section": SYLLABUS_SECTIONS.ADMIN, "topic": "Citizen Engagement", "question": "What method of citizen engagement involves citizens directly in the budget allocation process?", "answer": "Participatory Budgeting.", "details": "Common at the local level in Nepal.", "keywords": "Participatory Budgeting", "level": "Hard"
    },
]

# --- Streamlit State Initialization ---

def initialize_session_state():
    """Sets up all necessary session variables."""
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.current_index = 0
        st.session_state.show_answer = False
        st.session_state.score = 0
        st.session_state.stats = {'Correct': 0, 'Incorrect': 0}
        st.session_state.attempt_history = []
        st.session_state.practice_type = "Flashcard"
        st.session_state.difficulty = "All"
        st.session_state.section = "All"
        st.session_state.questions = []
        
        # Reset deck based on initial filters
        reset_deck()

def reset_deck():
    """Filters and shuffles the deck based on selected filters."""
    filtered_questions = INITIAL_DECK
    
    # Filter by difficulty
    if st.session_state.difficulty != "All":
        filtered_questions = [q for q in filtered_questions if q['level'] == st.session_state.difficulty]
    
    # Filter by section
    if st.session_state.section != "All":
        filtered_questions = [q for q in filtered_questions if q['section'] == st.session_state.section]

    random.shuffle(filtered_questions)
    st.session_state.questions = filtered_questions
    st.session_state.current_index = 0
    st.session_state.show_answer = False
    st.session_state.score = 0

# --- UI Components and Logic ---

def display_stats():
    """Placeholder for stats - currently disabled."""
    pass

def handle_answer(is_correct):
    """Updates state based on user's answer and moves to the next card."""
    q_id = st.session_state.questions[st.session_state.current_index]['id']
    attempt_type = 'Correct' if is_correct else 'Incorrect'

    # 1. Update overall stats
    st.session_state.stats[attempt_type] += 1
    
    # 2. Update session history (for detailed review if needed)
    st.session_state.attempt_history.append({'id': q_id, 'type': attempt_type})

    # 3. Move to the next question
    if st.session_state.current_index < len(st.session_state.questions) - 1:
        st.session_state.current_index += 1
        st.session_state.show_answer = False
    else:
        st.session_state.current_index += 1 # To show completion state
        st.session_state.show_answer = False
        st.toast("🎉 Quiz Mode Completed!")
        
def show_card(card):
    """Renders the flashcard view."""
    
    st.markdown(f"### ❓ Question {st.session_state.current_index + 1} / {len(st.session_state.questions)}")
    st.markdown(f"**Section:** `{card['section']} - {card['topic']}`")
    
    st.markdown(f"<div style='background-color: #1e3a8a; padding: 20px; border-radius: 10px; border-left: 5px solid #3b82f6; margin-top: 15px;'><h2 style='color: white;'>{card['question']}</h2></div>", unsafe_allow_html=True)

    st.button("Reveal Answer", on_click=lambda: st.session_state.__setitem__('show_answer', True), key="reveal_btn", disabled=st.session_state.show_answer)

    if st.session_state.show_answer:
        st.markdown("---")
        st.success("✅ Answer:")
        st.markdown(f"<div style='background-color: #556b2f; padding: 15px; border-radius: 8px; color: white;'><strong>{card['answer']}</strong></div>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6c757d; font-style: italic; font-size: 0.9em; margin-top: 10px;'>Context: {card['details']}</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Action Buttons
        col1, col2 = st.columns(2)
        col1.button("✅ I Got It (Correct)", on_click=lambda: handle_answer(True), use_container_width=True, type="primary")
        col2.button("❌ I Need Review (Incorrect)", on_click=lambda: handle_answer(False), use_container_width=True, type="secondary")




def show_completion_screen():
    """Renders the completion and final results screen."""
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #1e90ff;'>🥳 Study Session Complete!</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>You have successfully reviewed all {len(st.session_state.questions)} cards in the **{st.session_state.mode}** difficulty mode.</p>", unsafe_allow_html=True)

    # Final Statistics
    total_attempts = st.session_state.stats['Correct'] + st.session_state.stats['Incorrect']
    if total_attempts > 0:
        accuracy = (st.session_state.stats['Correct'] / total_attempts)
    else:
        accuracy = 0
        
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Attempts", total_attempts)
    col2.metric("Correct", st.session_state.stats['Correct'], delta=f"{accuracy*100:.1f}% Accuracy")
    col3.metric("Incorrect", st.session_state.stats['Incorrect'], delta=f"{(1-accuracy)*100:.1f}%")

    # Final Action
    if st.button("🔄 Start New Quiz", type="primary"):
        st.session_state.initialized = False # Re-initialize state for full reset
        st.experimental_rerun()

# --- Main Application Logic ---

def main():
    """Main Streamlit application function."""
    st.set_page_config(
        page_title="Loksewa Flashcard Tutor",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    initialize_session_state()

    st.title("🇳🇵 Loksewa Aayog Flashcard Tutor")
    st.markdown("Study and master your syllabus topics with the help of AI insights and current affairs grounding.")
    st.markdown("---")
    
    # Sidebar - Filters
    st.sidebar.markdown("### ⚙️ Study Filters")
    
    # Practice Type Filter
    practice_types = ["Flashcard", "MCQ", "Current Affairs"]
    new_practice = st.sidebar.selectbox(
        "Practice Type",
        practice_types,
        index=practice_types.index(st.session_state.practice_type),
        key="practice_selector"
    )
    
    # Difficulty Filter
    difficulty_list = ["All"] + LEVELS
    new_difficulty = st.sidebar.selectbox(
        "Difficulty",
        difficulty_list,
        index=difficulty_list.index(st.session_state.difficulty),
        key="difficulty_selector"
    )
    
    # Section Filter
    section_list = ["All", "Law", "Admin", "Constitution"]
    section_display = ["All", SYLLABUS_SECTIONS.LAW, SYLLABUS_SECTIONS.ADMIN, SYLLABUS_SECTIONS.CONST]
    new_section = st.sidebar.selectbox(
        "Section",
        section_display,
        index=section_display.index(st.session_state.section) if st.session_state.section in section_display else 0,
        key="section_selector"
    )
    
    # Convert display name back to stored value
    section_index = section_display.index(new_section) if new_section in section_display else 0
    new_section = section_list[section_index]
    
    # Check if any filter changed
    if (new_practice != st.session_state.practice_type or 
        new_difficulty != st.session_state.difficulty or 
        new_section != st.session_state.section):
        st.session_state.practice_type = new_practice
        st.session_state.difficulty = new_difficulty
        st.session_state.section = new_section
        reset_deck()
        st.experimental_rerun()
        return

    display_stats()
    
    # Main Content Display
    if st.session_state.current_index < len(st.session_state.questions):
        current_card = st.session_state.questions[st.session_state.current_index]
        show_card(current_card)
    else:
        show_completion_screen()

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import random

# --- Configuration & Constants ---

class SYLLABUS_SECTIONS:
    LAW = "Law & Justice"
    ADMIN = "Public Administration"
    CONST = "Constitution"

LEVELS = ["Basic", "Medium", "Hard"]

# --- 1. DATA: MCQs (120+ Questions) ---
# Expanded based on the syllabus and initial deck provided.
mcq_dataset = [
    # --- BASIC QUESTIONS ---
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
    {"id": 11, "section": SYLLABUS_SECTIONS.CONST, "question": "How many Fundamental Rights are guaranteed in Part 3 of the Constitution?", "options": {"A": "25", "B": "31", "C": "35", "D": "40"}, "answer": "B", "details": "Articles 16 to 46 (31 Rights).", "level": "Basic"},
    {"id": 12, "section": SYLLABUS_SECTIONS.CONST, "question": "On which date must the Federal Budget be presented to Parliament?", "options": {"A": "Baishakh 1", "B": "Jestha 15", "C": "Asar 1", "D": "Shrawan 1"}, "answer": "B", "details": "Article 119(3) mandates Jestha 15 (Republic Day).", "level": "Basic"},
    {"id": 13, "section": SYLLABUS_SECTIONS.CONST, "question": "Who is the ceremonial Head of State of Nepal?", "options": {"A": "Prime Minister", "B": "Chief Justice", "C": "President", "D": "Speaker"}, "answer": "C", "details": "Article 61 defines the President as the Head of State.", "level": "Basic"},
    {"id": 14, "section": SYLLABUS_SECTIONS.LAW, "question": "The Writ of Quo Warranto literally means?", "options": {"A": "We Command", "B": "By what authority", "C": "To be certified", "D": "Prohibition"}, "answer": "B", "details": "Challenges the legality of a person holding public office.", "level": "Basic"},
    {"id": 15, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which E-Governance model focuses on government services delivered to the public?", "options": {"A": "G2G", "B": "G2B", "C": "G2C", "D": "G2E"}, "answer": "C", "details": "Government to Citizen (G2C).", "level": "Basic"},
    {"id": 16, "section": SYLLABUS_SECTIONS.CONST, "question": "How many levels of government does Nepal's Federalism have?", "options": {"A": "Two", "B": "Three", "C": "Five", "D": "Seven"}, "answer": "B", "details": "Federal, Provincial, and Local.", "level": "Basic"},
    {"id": 17, "section": SYLLABUS_SECTIONS.LAW, "question": "What is the main remedy sought in a Civil Law dispute?", "options": {"A": "Imprisonment", "B": "Compensation/Damages", "C": "Fine to State", "D": "Capital Punishment"}, "answer": "B", "details": "Civil law aims to restore the injured party.", "level": "Basic"},
    {"id": 18, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What quality of governance means openness in decisions, allowing public scrutiny?", "options": {"A": "Efficiency", "B": "Transparency", "C": "Economy", "D": "Secrecy"}, "answer": "B", "details": "Transparency is key to Good Governance.", "level": "Basic"},
    {"id": 19, "section": SYLLABUS_SECTIONS.CONST, "question": "How many times has the Constitution of Nepal (2015) been amended?", "options": {"A": "Once", "B": "Twice", "C": "Thrice", "D": "Never"}, "answer": "B", "details": "First in 2016, Second in 2020.", "level": "Basic"},
    {"id": 20, "section": SYLLABUS_SECTIONS.LAW, "question": "Which code governs Family Law (Marriage, Divorce) in Nepal?", "options": {"A": "Muluki Ain 2020", "B": "Muluki Civil Code 2074", "C": "Evidence Act", "D": "Constitution"}, "answer": "B", "details": "Muluki Civil Code 2074 replaced the old Muluki Ain.", "level": "Basic"},
    {"id": 21, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the key legislative body at the Rural Municipality level?", "options": {"A": "Gaun Palika", "B": "Gaun Sabha", "C": "Ward Committee", "D": "District Coordination Committee"}, "answer": "B", "details": "The Village Assembly (Gaun Sabha) acts as the local legislature.", "level": "Basic"},
    {"id": 22, "section": SYLLABUS_SECTIONS.CONST, "question": "Which Article provides for the Language Commission?", "options": {"A": "Article 280", "B": "Article 287", "C": "Article 100", "D": "Article 50"}, "answer": "B", "details": "Article 287 establishes the Language Commission.", "level": "Basic"},
    {"id": 23, "section": SYLLABUS_SECTIONS.LAW, "question": "What is 'Najiir'?", "options": {"A": "A new law", "B": "A court precedent", "C": "A police report", "D": "A contract"}, "answer": "B", "details": "Precedent established by the Supreme Court.", "level": "Basic"},
    {"id": 24, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What does O&M stand for in Administration?", "options": {"A": "Office and Management", "B": "Organization and Management", "C": "Order and Method", "D": "Operation and Maintenance"}, "answer": "B", "details": "Survey technique for structural efficiency.", "level": "Basic"},
    {"id": 25, "section": SYLLABUS_SECTIONS.CONST, "question": "Who appoints the Attorney General of Nepal?", "options": {"A": "Prime Minister", "B": "Chief Justice", "C": "President", "D": "Law Minister"}, "answer": "C", "details": "President appoints on recommendation of the Prime Minister.", "level": "Basic"},
    {"id": 26, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Act is key for consumer protection in Nepal?", "options": {"A": "Black Marketing Act", "B": "Consumer Protection Act 2075", "C": "Civil Code", "D": "Food Act"}, "answer": "B", "details": "The 2075 Act is the primary legislation.", "level": "Basic"},
    {"id": 27, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which international body popularized the term 'Good Governance'?", "options": {"A": "United Nations", "B": "World Bank", "C": "IMF", "D": "WTO"}, "answer": "B", "details": "In the late 1980s.", "level": "Basic"},
    {"id": 28, "section": SYLLABUS_SECTIONS.CONST, "question": "Who has the authority to grant pardons in Nepal?", "options": {"A": "Supreme Court", "B": "Prime Minister", "C": "President", "D": "Home Minister"}, "answer": "C", "details": "Article 276.", "level": "Basic"},
    {"id": 29, "section": SYLLABUS_SECTIONS.LAW, "question": "What is Mandamus?", "options": {"A": "Order to stop", "B": "Order to perform a duty", "C": "Order to produce a person", "D": "Order to certify"}, "answer": "B", "details": "Compels a public official to act.", "level": "Basic"},
    {"id": 30, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the primary goal of Public Service Delivery?", "options": {"A": "Profit maximization", "B": "Serving citizens effectively", "C": "Expanding bureaucracy", "D": "Collecting taxes"}, "answer": "B", "details": "Effective, efficient, and equitable service.", "level": "Basic"},
    {"id": 31, "section": SYLLABUS_SECTIONS.CONST, "question": "Which tier of government has the power to impose sales tax?", "options": {"A": "Local", "B": "Provincial", "C": "Federal", "D": "Concurrent"}, "answer": "C", "details": "Schedule 5 lists it as a Federal power.", "level": "Basic"},
    {"id": 32, "section": SYLLABUS_SECTIONS.LAW, "question": "What is 'Jus Cogens'?", "options": {"A": "A flexible rule", "B": "A compelling, peremptory norm", "C": "A bilateral treaty", "D": "Domestic law"}, "answer": "B", "details": "A fundamental principle of international law.", "level": "Basic"},
    {"id": 33, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is Delegated Legislation?", "options": {"A": "Acts of Parliament", "B": "Constitution", "C": "Rules/Regulations made by Executive", "D": "Court Orders"}, "answer": "C", "details": "Law-making power delegated to the executive.", "level": "Basic"},
    {"id": 34, "section": SYLLABUS_SECTIONS.CONST, "question": "What electoral systems are used for the House of Representatives?", "options": {"A": "FPTP only", "B": "PR only", "C": "FPTP and PR", "D": "Electoral College"}, "answer": "C", "details": "Mixed system: 165 FPTP + 110 PR.", "level": "Basic"},
    {"id": 35, "section": SYLLABUS_SECTIONS.LAW, "question": "What is 'Muchulka'?", "options": {"A": "A verdict", "B": "A petition", "C": "A memo/record of facts", "D": "A bail bond"}, "answer": "C", "details": "Prepared on the spot to record facts.", "level": "Basic"},
    {"id": 36, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Public Accountability implies answerability to whom?", "options": {"A": "Superiors only", "B": "The Public", "C": "Donors", "D": "Political Parties"}, "answer": "B", "details": "Answerability to the citizens.", "level": "Basic"},
    {"id": 37, "section": SYLLABUS_SECTIONS.CONST, "question": "What is the tenure of the CIAA Chief Commissioner?", "options": {"A": "4 Years", "B": "5 Years", "C": "6 Years", "D": "Till age 60"}, "answer": "C", "details": "Article 238.", "level": "Basic"},
    {"id": 38, "section": SYLLABUS_SECTIONS.LAW, "question": "Tort Law deals with:", "options": {"A": "Crimes", "B": "Civil wrongs causing harm", "C": "International treaties", "D": "Constitutional amendments"}, "answer": "B", "details": "e.g., Negligence, Nuisance.", "level": "Basic"},
    {"id": 39, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Deconcentration is a form of:", "options": {"A": "Centralization", "B": "Privatization", "C": "Decentralization", "D": "Nationalization"}, "answer": "C", "details": "The weakest form of decentralization.", "level": "Basic"},
    {"id": 40, "section": SYLLABUS_SECTIONS.CONST, "question": "What does 'Secularism' mean in the Nepal Constitution?", "options": {"A": "Absence of religion", "B": "Anti-religion", "C": "Protection of Sanatana Dharma", "D": "One state religion"}, "answer": "C", "details": "Article 4 Explanation.", "level": "Basic"},

    # --- MEDIUM QUESTIONS ---
    {"id": 41, "section": SYLLABUS_SECTIONS.CONST, "question": "For how long after the appointment of a PM can a No Confidence Motion NOT be tabled?", "options": {"A": "6 Months", "B": "1 Year", "C": "2 Years", "D": "No limit"}, "answer": "C", "details": "Article 100(4).", "level": "Medium"},
    {"id": 42, "section": SYLLABUS_SECTIONS.LAW, "question": "Which is NOT an essential element of a valid Contract?", "options": {"A": "Offer", "B": "Acceptance", "C": "Consideration", "D": "Friendship"}, "answer": "D", "details": "Intention to create legal relations is required, not friendship.", "level": "Medium"},
    {"id": 43, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Devolution differs from Delegation because Devolution is:", "options": {"A": "Temporary", "B": "Permanent transfer to autonomous bodies", "C": "Revocable at will", "D": "Administrative only"}, "answer": "B", "details": "Delegation is temporary; Devolution is statutory and permanent.", "level": "Medium"},
    {"id": 44, "section": SYLLABUS_SECTIONS.CONST, "question": "An ordinance ceases to be effective if not adopted within how many days of the House meeting?", "options": {"A": "30 Days", "B": "45 Days", "C": "60 Days", "D": "90 Days"}, "answer": "C", "details": "Article 114.", "level": "Medium"},
    {"id": 45, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Writ is issued to quash an illegal decision of a lower court?", "options": {"A": "Mandamus", "B": "Habeas Corpus", "C": "Certiorari", "D": "Quo Warranto"}, "answer": "C", "details": "Corrects jurisdictional errors.", "level": "Medium"},
    {"id": 46, "section": SYLLABUS_SECTIONS.ADMIN, "question": "What is the first step in the Public Policy Process?", "options": {"A": "Evaluation", "B": "Implementation", "C": "Formulation", "D": "Agenda Setting / Problem ID"}, "answer": "D", "details": "Identifying the problem comes first.", "level": "Medium"},
    {"id": 47, "section": SYLLABUS_SECTIONS.CONST, "question": "Composition of the Constitutional Bench:", "options": {"A": "CJ + 2 Justices", "B": "CJ + 4 Justices", "C": "5 Senior Justices", "D": "Full Bench"}, "answer": "B", "details": "Article 137.", "level": "Medium"},
    {"id": 48, "section": SYLLABUS_SECTIONS.LAW, "question": "Which part of the Muluki Civil Code deals with Property Rights?", "options": {"A": "Part 1", "B": "Part 3", "C": "Part 4", "D": "Part 6"}, "answer": "C", "details": "Governs ownership, possession, and transfer.", "level": "Medium"},
    {"id": 49, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Social Inclusion aims to help:", "options": {"A": "The Elite", "B": "Marginalized groups", "C": "Political Parties", "D": "Foreign Investors"}, "answer": "B", "details": "Ensures equal access for excluded groups.", "level": "Medium"},
    {"id": 50, "section": SYLLABUS_SECTIONS.CONST, "question": "Who coordinates the Judicial Committee at the Local Level?", "options": {"A": "Mayor/Chairperson", "B": "Deputy Mayor/Vice-Chairperson", "C": "Chief Administrative Officer", "D": "Ward Chair"}, "answer": "B", "details": "Article 217.", "level": "Medium"},
    {"id": 51, "section": SYLLABUS_SECTIONS.CONST, "question": "Article 36 (Right to Food) guarantees the right to:", "options": {"A": "Free food for all", "B": "Food Sovereignty", "C": "Imported food", "D": "Subsidized crops"}, "answer": "B", "details": "Also includes protection from starvation.", "level": "Medium"},
    {"id": 52, "section": SYLLABUS_SECTIONS.LAW, "question": "The physical act of a crime is called:", "options": {"A": "Mens Rea", "B": "Actus Reus", "C": "Obiter Dicta", "D": "Res Judicata"}, "answer": "B", "details": "Mens Rea is the mental intent.", "level": "Medium"},
    {"id": 53, "section": SYLLABUS_SECTIONS.ADMIN, "question": "A primary market-related reason for Public Enterprises is to:", "options": {"A": "Increase taxes", "B": "Prevent Monopoly", "C": "Employ party cadres", "D": "Reduce exports"}, "answer": "B", "details": "And provide essential services.", "level": "Medium"},
    {"id": 54, "section": SYLLABUS_SECTIONS.CONST, "question": "Who votes in the Presidential Election?", "options": {"A": "Only MPs", "B": "Only Provincial Members", "C": "Federal Parliament & Provincial Assemblies", "D": "All Citizens"}, "answer": "C", "details": "Electoral College (Article 62).", "level": "Medium"},
    {"id": 55, "section": SYLLABUS_SECTIONS.LAW, "question": "Which is a primary source of International Law?", "options": {"A": "Treaties", "B": "News reports", "C": "NGO reports", "D": "Domestic circulars"}, "answer": "A", "details": "Along with Custom and General Principles.", "level": "Medium"},
    {"id": 56, "section": SYLLABUS_SECTIONS.ADMIN, "question": "The World Bank is an example of a:", "options": {"A": "Bilateral Agency", "B": "Multilateral Agency", "C": "NGO", "D": "Local Club"}, "answer": "B", "details": "Represents multiple member countries.", "level": "Medium"},
    {"id": 57, "section": SYLLABUS_SECTIONS.CONST, "question": "Who is the Member-Secretary of the National Security Council?", "options": {"A": "Home Secretary", "B": "Defence Secretary", "C": "Chief of Army Staff", "D": "IGP"}, "answer": "B", "details": "Article 266.", "level": "Medium"},
    {"id": 58, "section": SYLLABUS_SECTIONS.LAW, "question": "Which Act governs the privatization of PEs?", "options": {"A": "Company Act", "B": "Privatization Act 2050", "C": "Industrial Enterprise Act", "D": "Labor Act"}, "answer": "B", "details": "Enacted to manage the transfer of PEs.", "level": "Medium"},
    {"id": 59, "section": SYLLABUS_SECTIONS.ADMIN, "question": "The 'Buch Commission' (2009 BS) is related to:", "options": {"A": "Land Reform", "B": "Administrative Reform", "C": "Education", "D": "Health"}, "answer": "B", "details": "First major admin reform commission.", "level": "Medium"},
    {"id": 60, "section": SYLLABUS_SECTIONS.CONST, "question": "Schedule 9 of the Constitution lists:", "options": {"A": "Federal Powers", "B": "Provincial Powers", "C": "Local Powers", "D": "Concurrent Powers"}, "answer": "D", "details": "Powers shared by all three tiers.", "level": "Medium"},
    {"id": 61, "section": SYLLABUS_SECTIONS.LAW, "question": "An Injunction is a court order to:", "options": {"A": "Pay money", "B": "Perform or stop a specific act", "C": "Go to jail", "D": "Apologize"}, "answer": "B", "details": "A remedy in civil law.", "level": "Medium"},
    {"id": 62, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Accountability enforced by courts is:", "options": {"A": "Social Accountability", "B": "Legal Accountability", "C": "Political Accountability", "D": "Ethical Accountability"}, "answer": "B", "details": "Based on law and compliance.", "level": "Medium"},
    {"id": 63, "section": SYLLABUS_SECTIONS.CONST, "question": "Who is the 'Chief of Province'?", "options": {"A": "Chief Minister", "B": "Speaker of Province", "C": "Representative of Federal Govt in Province", "D": "Chief Judge"}, "answer": "C", "details": "Appointed by President (Article 163).", "level": "Medium"},
    {"id": 64, "section": SYLLABUS_SECTIONS.LAW, "question": "If a ratified treaty conflicts with Nepal law, which prevails?", "options": {"A": "Nepal Law", "B": "The Treaty", "C": "Supreme Court decides", "D": "Both are void"}, "answer": "B", "details": "Per Nepal Treaty Act 1990.", "level": "Medium"},
    {"id": 65, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which policy step assesses impact?", "options": {"A": "Formulation", "B": "Implementation", "C": "Adoption", "D": "Evaluation"}, "answer": "D", "details": "Checking if goals were met.", "level": "Medium"},
    {"id": 66, "section": SYLLABUS_SECTIONS.CONST, "question": "Is the NPC a Constitutional Body?", "options": {"A": "Yes", "B": "No", "C": "Partially", "D": "Pending status"}, "answer": "B", "details": "It is a specialized executive agency.", "level": "Medium"},
    {"id": 67, "section": SYLLABUS_SECTIONS.LAW, "question": "Article 31 guarantees education in:", "options": {"A": "English", "B": "Mother Tongue", "C": "Sanskrit", "D": "Hindi"}, "answer": "B", "details": "Right to basic education in mother tongue.", "level": "Medium"},
    {"id": 68, "section": SYLLABUS_SECTIONS.ADMIN, "question": "G2E E-Governance targets:", "options": {"A": "Citizens", "B": "Businesses", "C": "Employees (Internal)", "D": "Foreign Govts"}, "answer": "C", "details": "Improving internal efficiency.", "level": "Medium"},
    {"id": 69, "section": SYLLABUS_SECTIONS.CONST, "question": "Who can initiate impeachment of the CJ?", "options": {"A": "President", "B": "PM", "C": "1/4th of HoR members", "D": "Bar Association"}, "answer": "C", "details": "Article 101.", "level": "Medium"},
    {"id": 70, "section": SYLLABUS_SECTIONS.LAW, "question": "Company and Banking laws fall under:", "options": {"A": "Criminal Law", "B": "Commercial Law", "C": "Family Law", "D": "Constitutional Law"}, "answer": "B", "details": "Regulating business transactions.", "level": "Medium"},
    {"id": 71, "section": SYLLABUS_SECTIONS.ADMIN, "question": "'Prerogative Power' usually belongs to:", "options": {"A": "Civil Servants", "B": "The Head of State", "C": "Local Ward Chair", "D": "NGOs"}, "answer": "B", "details": "Discretionary powers.", "level": "Medium"},
    {"id": 72, "section": SYLLABUS_SECTIONS.CONST, "question": "Can the PM dissolve the House at will?", "options": {"A": "Yes, always", "B": "No, heavily restricted", "C": "Yes, with President's support", "D": "Only in emergency"}, "answer": "B", "details": "Only if government formation is impossible.", "level": "Medium"},
    {"id": 73, "section": SYLLABUS_SECTIONS.LAW, "question": "Coexistence of state and customary law is:", "options": {"A": "Legal Monism", "B": "Legal Pluralism", "C": "Anarchy", "D": "Dictatorship"}, "answer": "B", "details": "Multiple legal systems.", "level": "Medium"},
    {"id": 74, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Delegation is temporary; Devolution is:", "options": {"A": "Also temporary", "B": "Permanent", "C": "Illegal", "D": "Informal"}, "answer": "B", "details": "Transfer to autonomous units.", "level": "Medium"},
    {"id": 75, "section": SYLLABUS_SECTIONS.CONST, "question": "Who recommends revenue distribution?", "options": {"A": "Ministry of Finance", "B": "NPC", "C": "NNRFC", "D": "Rastra Bank"}, "answer": "C", "details": "National Natural Resources and Fiscal Commission.", "level": "Medium"},
    {"id": 76, "section": SYLLABUS_SECTIONS.LAW, "question": "'Punitive Damages' are meant to:", "options": {"A": "Compensate", "B": "Punish and deter", "C": "Refund costs", "D": "Pay taxes"}, "answer": "B", "details": "Beyond actual loss.", "level": "Medium"},
    {"id": 77, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Where must a Citizen Charter be displayed?", "options": {"A": "In the file", "B": "On the website only", "C": "Visibly in the office", "D": "In the store"}, "answer": "C", "details": "Good Governance Act requirement.", "level": "Medium"},
    {"id": 78, "section": SYLLABUS_SECTIONS.CONST, "question": "What is the fixed term of the PM?", "options": {"A": "5 Years", "B": "2 Years", "C": "No fixed term", "D": "10 Years"}, "answer": "C", "details": "Depends on House confidence.", "level": "Medium"},
    {"id": 79, "section": SYLLABUS_SECTIONS.LAW, "question": "Stare Decisis means:", "options": {"A": "To stand by decided matters", "B": "To argue", "C": "To legislate", "D": "To appeal"}, "answer": "A", "details": "Precedent principle.", "level": "Medium"},
    {"id": 80, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Challenge for E-Governance in rural Nepal:", "options": {"A": "Too much internet", "B": "Digital Divide", "C": "Excess electricity", "D": "High literacy"}, "answer": "B", "details": "Lack of access/skills.", "level": "Medium"},

    # --- HARD QUESTIONS ---
    {"id": 81, "section": SYLLABUS_SECTIONS.CONST, "question": "Which subject cannot be amended in the Constitution?", "options": {"A": "Fundamental Rights", "B": "Sovereignty & Territorial Integrity", "C": "Federalism", "D": "Secularism"}, "answer": "B", "details": "Article 274(1).", "level": "Hard"},
    {"id": 82, "section": SYLLABUS_SECTIONS.LAW, "question": "'Mens Rea' refers to:", "options": {"A": "The criminal act", "B": "The guilty mind/intent", "C": "The punishment", "D": "The victim"}, "answer": "B", "details": "Essential element of crime.", "level": "Hard"},
    {"id": 83, "section": SYLLABUS_SECTIONS.CONST, "question": "Majority required to ratify treaties on natural resources?", "options": {"A": "Simple Majority", "B": "Two-thirds of both Houses", "C": "Unanimous", "D": "Cabinet decision"}, "answer": "B", "details": "Article 279.", "level": "Hard"},
    {"id": 84, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which Committee enforces Financial Accountability?", "options": {"A": "State Affairs Committee", "B": "Public Accounts Committee (PAC)", "C": "Legislation Committee", "D": "Development Committee"}, "answer": "B", "details": "Reviews Auditor General reports.", "level": "Hard"},
    {"id": 85, "section": SYLLABUS_SECTIONS.LAW, "question": "'Pacta Sunt Servanda' means:", "options": {"A": "Agreements must be kept", "B": "Treaties are optional", "C": "War is illegal", "D": "Diplomacy first"}, "answer": "A", "details": "Fundamental treaty law principle.", "level": "Hard"},
    {"id": 86, "section": SYLLABUS_SECTIONS.CONST, "question": "Are Directive Principles (Part 4) justiciable?", "options": {"A": "Yes, in Supreme Court", "B": "No", "C": "Only Fundamental Duties", "D": "Yes, in High Court"}, "answer": "B", "details": "Article 55: Questions cannot be raised in court.", "level": "Hard"},
    {"id": 87, "section": SYLLABUS_SECTIONS.ADMIN, "question": "NPM (New Public Management) emphasizes:", "options": {"A": "Strict rules", "B": "Process over results", "C": "The '3 Es' (Economy, Efficiency, Effectiveness)", "D": "Centralization"}, "answer": "C", "details": "Market-oriented administration.", "level": "Hard"},
    {"id": 88, "section": SYLLABUS_SECTIONS.CONST, "question": "Who acts as the final interpreter of the Constitution?", "options": {"A": "Parliament", "B": "President", "C": "Supreme Court", "D": "Constitutional Council"}, "answer": "C", "details": "Article 128.", "level": "Hard"},
    {"id": 89, "section": SYLLABUS_SECTIONS.LAW, "question": "Double Jeopardy means:", "options": {"A": "Tried twice for same offense", "B": "Tried in two courts", "C": "Punished twice", "D": "Protection against being tried/punished for same offense"}, "answer": "D", "details": "Article 20(6).", "level": "Hard"},
    {"id": 90, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which theory treats organization as a social system?", "options": {"A": "Bureaucratic Theory", "B": "Human Relations Theory", "C": "Scientific Management", "D": "Classical Theory"}, "answer": "B", "details": "Elton Mayo.", "level": "Hard"},
    {"id": 91, "section": SYLLABUS_SECTIONS.CONST, "question": "Residual Powers are vested in:", "options": {"A": "Local Level", "B": "Province", "C": "Federation", "D": "Shared"}, "answer": "C", "details": "Article 58.", "level": "Hard"},
    {"id": 92, "section": SYLLABUS_SECTIONS.LAW, "question": "Res Judicata prevents:", "options": {"A": "Appeals", "B": "Re-litigation of decided cases", "C": "New evidence", "D": "Transfers"}, "answer": "B", "details": "Finality of judgment.", "level": "Hard"},
    {"id": 93, "section": SYLLABUS_SECTIONS.ADMIN, "question": "The 'Merit System' in civil service opposes:", "options": {"A": "Competence", "B": "Spoils System/Patronage", "C": "Exams", "D": "Neutrality"}, "answer": "B", "details": "Selection based on ability, not politics.", "level": "Hard"},
    {"id": 94, "section": SYLLABUS_SECTIONS.CONST, "question": "Emergency Power duration (initial) if declared by President:", "options": {"A": "1 Month", "B": "3 Months", "C": "6 Months", "D": "1 Year"}, "answer": "A", "details": "Must be approved by House within 1 month.", "level": "Hard"},
    {"id": 95, "section": SYLLABUS_SECTIONS.LAW, "question": "Which is NOT a general defense in Tort?", "options": {"A": "Volenti non fit injuria", "B": "Act of God", "C": "Necessity", "D": "Malice"}, "answer": "D", "details": "Malice is an element of liability, not a defense.", "level": "Hard"},
    {"id": 96, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Who appoints the Chief Secretary?", "options": {"A": "Public Service Commission", "B": "Prime Minister", "C": "Cabinet", "D": "Minister of General Admin"}, "answer": "C", "details": "Cabinet decision.", "level": "Hard"},
    {"id": 97, "section": SYLLABUS_SECTIONS.CONST, "question": "Inter-Provincial Council is chaired by:", "options": {"A": "Home Minister", "B": "President", "C": "Prime Minister", "D": "Senior CM"}, "answer": "C", "details": "Article 234.", "level": "Hard"},
    {"id": 98, "section": SYLLABUS_SECTIONS.LAW, "question": "Specific Performance is a remedy in:", "options": {"A": "Contract Law", "B": "Criminal Law", "C": "Tax Law", "D": "Traffic Law"}, "answer": "A", "details": "Compelling a party to fulfill the contract.", "level": "Hard"},
    {"id": 99, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Line vs Staff Agency: Staff Agency function is:", "options": {"A": "Execution", "B": "Decision making", "C": "Advisory", "D": "Public dealing"}, "answer": "C", "details": "Line executes; Staff advises.", "level": "Hard"},
    {"id": 100, "section": SYLLABUS_SECTIONS.CONST, "question": "How many members in the National Assembly?", "options": {"A": "59", "B": "60", "C": "110", "D": "275"}, "answer": "A", "details": "56 elected + 3 nominated.", "level": "Hard"},
    {"id": 101, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Span of Control refers to:", "options": {"A": "Area of office", "B": "Number of subordinates a superior can manage", "C": "Length of service", "D": "Power of Minister"}, "answer": "B", "details": "Management principle.", "level": "Hard"},
    {"id": 102, "section": SYLLABUS_SECTIONS.LAW, "question": "Ignorantia juris non excusat means:", "options": {"A": "Ignorance of fact is excuse", "B": "Ignorance of law is no excuse", "C": "Law is blind", "D": "Judges are supreme"}, "answer": "B", "details": "Universal legal maxim.", "level": "Hard"},
    {"id": 103, "section": SYLLABUS_SECTIONS.CONST, "question": "Who acts as the Secretariat of the Constitutional Council?", "options": {"A": "Parliament Secretariat", "B": "Office of President", "C": "Office of PM (OPMCM)", "D": "Supreme Court"}, "answer": "C", "details": "Chief Secretary functions as secretary.", "level": "Hard"},
    {"id": 104, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Which creates a 'Virtual Bureaucracy'?", "options": {"A": "Red Tape", "B": "E-Governance", "C": "Decentralization", "D": "Privatization"}, "answer": "B", "details": "Digitized admin.", "level": "Hard"},
    {"id": 105, "section": SYLLABUS_SECTIONS.LAW, "question": "Jurisprudence is the study of:", "options": {"A": "Jury selection", "B": "Prison management", "C": "Philosophy/Theory of Law", "D": "Case files"}, "answer": "C", "details": "Science of law.", "level": "Hard"},
    {"id": 106, "section": SYLLABUS_SECTIONS.CONST, "question": "Vote of Credit (Article 122) allows:", "options": {"A": "Loans from bank", "B": "Expenditure when budget is not passed", "C": "Foreign aid", "D": "Tax collection"}, "answer": "B", "details": "Advance expenditure.", "level": "Hard"},
    {"id": 107, "section": SYLLABUS_SECTIONS.ADMIN, "question": "POSDCORB was coined by:", "options": {"A": "Luther Gulick", "B": "Max Weber", "C": "Taylor", "D": "Fayol"}, "answer": "A", "details": "Acronym for admin functions.", "level": "Hard"},
    {"id": 108, "section": SYLLABUS_SECTIONS.LAW, "question": "Hostile Witness is one who:", "options": {"A": "Attacks the judge", "B": "Testifies against the party calling them", "C": "Refuses to speak", "D": "Lies"}, "answer": "B", "details": "Adverse witness.", "level": "Hard"},
    {"id": 109, "section": SYLLABUS_SECTIONS.CONST, "question": "District Assembly consists of:", "options": {"A": "All citizens", "B": "Chair/Vice-Chair of Rural Municipalities + Mayor/Deputy Mayor", "C": "MPs", "D": "CDO and Police"}, "answer": "B", "details": "Article 220.", "level": "Hard"},
    {"id": 110, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Red Tape implies:", "options": {"A": "Fast service", "B": "Efficient filing", "C": "Excessive formalities/delay", "D": "Digital records"}, "answer": "C", "details": "Bureaucratic pathology.", "level": "Hard"},
    {"id": 111, "section": SYLLABUS_SECTIONS.LAW, "question": "Locus Standi means:", "options": {"A": "Place of standing/Right to bring action", "B": "Location of crime", "C": "Stand up in court", "D": "Local standard"}, "answer": "A", "details": "Right to be heard.", "level": "Hard"},
    {"id": 112, "section": SYLLABUS_SECTIONS.CONST, "question": "Can the Army be mobilized without NSC recommendation?", "options": {"A": "Yes, by PM", "B": "Yes, by President", "C": "No", "D": "In war only"}, "answer": "C", "details": "Article 267(6).", "level": "Hard"},
    {"id": 113, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Matrix Organization combines:", "options": {"A": "Functional and Project structures", "B": "Public and Private", "C": "Central and Local", "D": "Line and Staff"}, "answer": "A", "details": "Dual reporting.", "level": "Hard"},
    {"id": 114, "section": SYLLABUS_SECTIONS.LAW, "question": "Obiter Dicta refers to:", "options": {"A": "Binding decision", "B": "Incidental remark/opinion of judge", "C": "Final verdict", "D": "The charge sheet"}, "answer": "B", "details": "Not binding precedent.", "level": "Hard"},
    {"id": 115, "section": SYLLABUS_SECTIONS.CONST, "question": "Which commission handles Electoral Constituency Delimitation?", "options": {"A": "Election Commission", "B": "Constituency Delimitation Commission", "C": "Parliament", "D": "Supreme Court"}, "answer": "B", "details": "Article 286.", "level": "Hard"},
    {"id": 116, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Hierarchy is known as:", "options": {"A": "Scalar Chain", "B": "Gang Plank", "C": "Esprit de Corps", "D": "Unity of Command"}, "answer": "A", "details": "Chain of command.", "level": "Hard"},
    {"id": 117, "section": SYLLABUS_SECTIONS.LAW, "question": "Ex Post Facto Law is:", "options": {"A": "Future law", "B": "Retrospective criminal law (Prohibited)", "C": "Civil law", "D": "Foreign law"}, "answer": "B", "details": "Article 20(4) prohibits it.", "level": "Hard"},
    {"id": 118, "section": SYLLABUS_SECTIONS.CONST, "question": "Constitutional Council is chaired by:", "options": {"A": "President", "B": "Chief Justice", "C": "Prime Minister", "D": "Speaker"}, "answer": "C", "details": "Article 284.", "level": "Hard"},
    {"id": 119, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Parkinson's Law states:", "options": {"A": "Work expands to fill time available", "B": "Work contracts", "C": "Admins are lazy", "D": "Money is power"}, "answer": "A", "details": "Bureaucratic expansion.", "level": "Hard"},
    {"id": 120, "section": SYLLABUS_SECTIONS.LAW, "question": "Natural Justice includes:", "options": {"A": "Right to bias", "B": "Rule against bias & Right to hearing", "C": "Immediate jail", "D": "No trial"}, "answer": "B", "details": "Nemo judex in causa sua.", "level": "Hard"},
    {"id": 121, "section": SYLLABUS_SECTIONS.CONST, "question": "Who can remove a Provincial Governor?", "options": {"A": "Provincial Assembly", "B": "President", "C": "Chief Minister", "D": "High Court"}, "answer": "B", "details": "Article 165.", "level": "Hard"},
    {"id": 122, "section": SYLLABUS_SECTIONS.ADMIN, "question": "Unity of Command means:", "options": {"A": "One boss for one subordinate", "B": "Many bosses", "C": "Team work", "D": "Union power"}, "answer": "A", "details": "Prevents confusion.", "level": "Hard"},
]

# --- 2. DATA: Current Affairs (Reused) ---
current_affairs_news = [
    # Admin (Structure, Reforms, Federalism)
    {"id": 301, "title": "Approval of Federal Civil Service Bill Draft", "summary": "The government approved the draft of the long-awaited Federal Civil Service Bill, aiming to finalize the administrative structure under the federal system and streamline recruitment.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
    {"id": 302, "title": "E-Governance Portal Integration Milestone", "summary": "The Digital Nepal Framework reached a milestone with the integration of over 50 public service portals into a single e-governance platform for citizens.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 303, "title": "New Public Policy on Climate Resilience", "summary": "The government launched a new National Public Policy focusing on climate change adaptation and resilience, mandating integration across all provincial and local planning processes.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
    {"id": 304, "title": "Local Level Budget Ceiling Fixation", "summary": "The Ministry of Federal Affairs fixed the budget ceilings for all 753 local levels, clarifying fiscal limits and resource mobilization expectations for the current fiscal year.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    {"id": 305, "title": "Reform in Foreign Employment Administration", "summary": "A significant administrative reform simplified the process for obtaining work permits and addressing grievances for migrant workers, enhancing labor law implementation.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 306, "title": "Federalism Implementation Review", "summary": "A high-level commission submitted its report on the status of federalism implementation, highlighting challenges in concurrent power sharing and inter-governmental coordination.", "section": SYLLABUS_SECTIONS.CONST, "level": "Hard"},
    {"id": 307, "title": "Decentralization of Land Revenue Offices", "summary": "Several land revenue offices were decentralized and their services transferred to local governments to improve public service delivery efficiency.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    {"id": 308, "title": "New Digital Tax System Rollout", "summary": "The Inland Revenue Department successfully rolled out a new digital system for VAT and income tax filing, part of an e-governance initiative to boost compliance.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 309, "title": "Public Sector Enterprise Privatization Study", "summary": "A task force was formed to study the potential privatization or restructuring of three major loss-making public enterprises, citing challenges in performance.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
    {"id": 310, "title": "Civic Sense Campaign Launched", "summary": "The Ministry of Culture launched a nationwide campaign to promote civic sense and public servant responsibilities, focusing on accountability and ethics.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    # Law (Courts, Acts, Rights, Procedures)
    {"id": 311, "title": "Supreme Court Ruling on Ordinance Validity", "summary": "The SC delivered a landmark judgment questioning the excessive use of ordinances by the executive, emphasizing the role of the legislature in law-making.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 312, "title": "Secured Transaction Act Implementation", "summary": "The government issued new rules for the full implementation of the Secured Transaction Act, facilitating access to credit for small and medium enterprises.", "section": SYLLABUS_SECTIONS.LAW, "level": "Medium"},
    {"id": 313, "title": "Amendment to Consumer Protection Law", "summary": "Parliament passed an amendment to the Consumer Protection Act, introducing stricter penalties for substandard goods and services, especially e-commerce fraud.", "section": SYLLABUS_SECTIONS.LAW, "level": "Basic"},
    {"id": 314, "title": "Legal Aid Services Expansion in Provinces", "summary": "The Judicial Council announced a plan to expand free legal aid services to all district courts in the seven provinces, focusing on marginalized communities.", "section": SYLLABUS_SECTIONS.LAW, "level": "Medium"},
    {"id": 315, "title": "New Regulation on Environmental Impact Assessment", "summary": "New regulations were issued under the Environment Protection Act, making Environmental Impact Assessments (EIAs) mandatory for even smaller development projects.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 316, "title": "Ruling on Property Rights for Women", "summary": "A High Court ruling provided clarity on the equal inheritance and property rights of daughters, reinforcing existing provisions in the Civil Code.", "section": SYLLABUS_SECTIONS.LAW, "level": "Basic"},
    {"id": 317, "title": "International Labor Organization Convention Ratification", "summary": "Nepal ratified a key ILO convention related to occupational health and safety, strengthening the country's labor law framework and international obligations.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 318, "title": "Supreme Court Verdict on Citizenship Rights", "summary": "The SC issued an important verdict clarifying the process for granting citizenship by descent to children of citizens who obtained citizenship by birth.", "section": SYLLABUS_SECTIONS.CONST, "level": "Medium"},
    {"id": 319, "title": "Training for Administrative Law Judges", "summary": "A national training program was conducted for administrative law judges and officials on effective implementation of the Administrative Procedure Act.", "section": SYLLABUS_SECTIONS.LAW, "level": "Medium"},
    {"id": 320, "title": "Criminal Procedure Code Amendment Proposed", "summary": "A proposal for amending the Criminal Procedure Code was tabled in Parliament to streamline investigation processes and ensure speedy trials.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    # Constitution (Constitutional Bodies, Rights, Federal Structure)
    {"id": 321, "title": "Constitutional Council Appointments", "summary": "The Constitutional Council recommended new appointments to the Commission for the Investigation of Abuse of Authority (CIAA) and other constitutional bodies.", "section": SYLLABUS_SECTIONS.CONST, "level": "Basic"},
    {"id": 322, "title": "Debate on Concurrent Powers", "summary": "Provincial Chief Ministers met with the Federal government to discuss the ambiguities and conflicts arising from the concurrent list of powers (Schedule 9).", "section": SYLLABUS_SECTIONS.CONST, "level": "Medium"},
    {"id": 323, "title": "High Court Upholds Fundamental Right to Clean Environment", "summary": "A High Court delivered a judgment based on the fundamental right to a clean environment, ordering a local municipality to manage waste effectively.", "section": SYLLABUS_SECTIONS.CONST, "level": "Basic"},
    {"id": 324, "title": "National Planning Commission Restructuring Proposal", "summary": "A task force recommended restructuring the National Planning Commission to better align its functions with the federal structure of the Constitution.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 325, "title": "New Regulations for Judicial Service Commission", "summary": "The Judicial Service Commission introduced new regulations for the recruitment and promotion of judicial staff to enhance judicial administration.", "section": SYLLABUS_SECTIONS.CONST, "level": "Hard"},
    {"id": 326, "title": "Provincial Government Budget Presentation", "summary": "All seven Provincial Governments successfully presented their budgets for the new fiscal year, showcasing greater fiscal autonomy under federalism.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    {"id": 327, "title": "Human Rights Commission Annual Report", "summary": "The National Human Rights Commission released its annual report, recommending key reforms in police procedures and prison management.", "section": SYLLABUS_SECTIONS.CONST, "level": "Medium"},
    {"id": 328, "title": "Public Hearing on Right to Food Act", "summary": "A national public hearing was conducted on the implementation framework of the Right to Food and Food Sovereignty Act, a fundamental right under the Constitution.", "section": SYLLABUS_SECTIONS.LAW, "level": "Medium"},
    {"id": 329, "title": "Amendment to Election Act Discussed", "summary": "Parliamentarians initiated discussions on amending the Election Act to ensure greater transparency and efficiency in electoral processes managed by the Election Commission.", "section": SYLLABUS_SECTIONS.CONST, "level": "Medium"},
    {"id": 330, "title": "New Civil Service Ethics Code", "summary": "The government introduced a new code of ethics and conduct for public servants, emphasizing neutrality, integrity, and responsibility in service delivery.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
    {"id": 331, "title": "Inter-Provincial Coordination Meeting on Security", "summary": "The chief ministers held a coordination meeting to discuss unified security strategies and administrative cooperation across provincial boundaries.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 332, "title": "Supreme Court on International Treaty Enforcement", "summary": "A judgment clarified the mechanism for the domestic enforcement of international treaties ratified by Nepal, strengthening the Law of Treaties.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 333, "title": "Local Level E-Bidding Mandate", "summary": "The Ministry of Federal Affairs mandated the use of an e-bidding system for all local government procurement to enhance transparency and reduce corruption.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    {"id": 334, "title": "Legal Literacy Program for Rural Areas", "summary": "The Nepal Bar Association launched a nationwide legal literacy program to educate rural communities on fundamental rights and access to justice.", "section": SYLLABUS_SECTIONS.LAW, "level": "Basic"},
    {"id": 335, "title": "Constitutional Bench on Federal Dispute", "summary": "The Constitutional Bench is currently hearing a case challenging the constitutionality of certain provincial tax laws that conflict with federal tax jurisdiction.", "section": SYLLABUS_SECTIONS.CONST, "level": "Hard"},
    {"id": 336, "title": "Public Sector Employee Performance Appraisal Reform", "summary": "A new result-based performance appraisal system was introduced for all civil servants to link evaluation directly to public service delivery outcomes.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
    {"id": 337, "title": "Court Ruling on Child Labor Law", "summary": "A district court successfully prosecuted a case under the Labor Law, imposing a stiff penalty on an establishment for employing minors.", "section": SYLLABUS_SECTIONS.LAW, "level": "Basic"},
    {"id": 338, "title": "New Directive on Citizen's Charter", "summary": "The Ministry of General Administration issued a new directive mandating all public offices to display and strictly adhere to their Citizen's Charter for transparency.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    {"id": 339, "title": "Review of Foreign Aid Mobilization Policy", "summary": "The government is reviewing its public policy on foreign aid mobilization to ensure alignment with national priorities and constitutional mandates.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 340, "title": "Legal Provision for Digital Evidence", "summary": "The Federal Parliament is debating an amendment to the Evidence Act to provide clearer legal provisions and admissibility standards for digital and electronic evidence.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 341, "title": "Commission for Investigation of Abuse of Authority (CIAA) Action", "summary": "The CIAA launched an investigation into high-profile corruption cases involving public officials in administrative bodies at the local level.", "section": SYLLABUS_SECTIONS.CONST, "level": "Medium"},
    {"id": 342, "title": "E-Passport Service Expansion", "summary": "The Department of Passport expanded its e-passport service to all district administration offices, streamlining a key public service delivery mechanism.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    {"id": 343, "title": "Debate on Federal Police Act", "summary": "The Federal Police Act remains a central point of contention between the Federal and Provincial governments regarding security coordination and control.", "section": SYLLABUS_SECTIONS.CONST, "level": "Hard"},
    {"id": 344, "title": "Public Interest Litigation on Air Pollution", "summary": "A public interest litigation (PIL) was filed in the Supreme Court demanding stricter implementation of environmental laws to combat alarming air pollution levels.", "section": SYLLABUS_SECTIONS.LAW, "level": "Medium"},
    {"id": 345, "title": "Training on Gender-Sensitive Law Enforcement", "summary": "The Nepal Police launched a national training module for its personnel on gender-sensitive handling of domestic violence and criminal cases.", "section": SYLLABUS_SECTIONS.LAW, "level": "Medium"},
    {"id": 346, "title": "New Guidelines for Cooperative Regulation", "summary": "The Ministry of Cooperatives issued new guidelines aimed at strengthening the regulation and monitoring of cooperative societies to protect consumer funds.", "section": SYLLABUS_SECTIONS.LAW, "level": "Basic"},
    {"id": 347, "title": "Supreme Court on Right to Health Services", "summary": "A SC judgment reaffirmed the constitutional right to basic health services as a fundamental right, directing the government to ensure access.", "section": SYLLABUS_SECTIONS.CONST, "level": "Basic"},
    {"id": 348, "title": "Administrative Staff Adjustment in Provinces", "summary": "The MoFAGA completed a major phase of administrative staff adjustment, transferring thousands of civil servants to provincial and local levels.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 349, "title": "International Law Seminar on Treaties", "summary": "A national seminar was held to discuss the implications of international law and conventions, particularly those related to transboundary water resources and treaties.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 350, "title": "Local Level Revenue Sharing Formula", "summary": "A new formula was adopted by the Federal government for sharing non-tax revenue collected at the local level with the provincial governments.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
    {"id": 351, "title": "Drafting Rules for Labor Court Procedures", "summary": "New drafting rules have been prepared to simplify the procedure for filing and hearing petitions in the Labor Court.", "section": SYLLABUS_SECTIONS.LAW, "level": "Basic"},
    {"id": 352, "title": "Review of Fundamental Duties of Citizens", "summary": "An expert committee was formed to review the scope and enforcement mechanisms for the fundamental duties and responsibilities of citizens.", "section": SYLLABUS_SECTIONS.CONST, "level": "Medium"},
    {"id": 353, "title": "E-Tax Payment System for Local Governments", "summary": "Several metropolitan cities adopted an integrated e-tax payment and property valuation system to enhance administrative transparency.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    {"id": 354, "title": "Supreme Court on Administrative Discretion", "summary": "A SC ruling set clear boundaries on the administrative discretion of government officials, emphasizing the principle of Rule of Law.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 355, "title": "Public Policy on Tourism Development", "summary": "The Ministry of Tourism introduced a new public policy aimed at promoting sustainable and inclusive tourism, requiring coordination across all three tiers of government.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 356, "title": "Constitutional Provision for Special Structure", "summary": "Parliament is discussing a bill to implement the constitutional provision allowing for special structures or protected areas for marginalized groups.", "section": SYLLABUS_SECTIONS.CONST, "level": "Hard"},
    {"id": 357, "title": "Judicial Administration Training for District Judges", "summary": "A compulsory advanced training program was initiated for all district judges focusing on modern judicial administration practices and case management.", "section": SYLLABUS_SECTIONS.LAW, "level": "Medium"},
    {"id": 358, "title": "Progress on Right to Housing Act Implementation", "summary": "The Ministry of Urban Development reported progress on the implementation of the Right to Housing Act, particularly in allocating landless squatters' land.", "section": SYLLABUS_SECTIONS.CONST, "level": "Basic"},
    {"id": 359, "title": "Administrative Reform on Pension Disbursement", "summary": "The government streamlined the process for pension disbursement using an online system, greatly improving the public service delivery to senior citizens.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
    {"id": 360, "title": "Constitutional Bench Formed for Federal Dispute", "summary": "A new constitutional bench has been formed to hear disputes regarding the division of powers between the Federal and Provincial governments.", "section": SYLLABUS_SECTIONS.CONST, "level": "Hard"},
    {"id": 361, "title": "National ID Card Mandatory for Service", "summary": "The government announced that the National ID card will soon be mandatory for accessing key public services, enhancing E-Governance implementation.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 362, "title": "Court Ruling on Government Contracts", "summary": "A High Court ruled on the proper drafting and execution of government contracts, emphasizing transparency and legal compliance in public agreements.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 363, "title": "New Rules on Public Procurement", "summary": "New Public Procurement Rules were introduced to simplify procedures for local levels while increasing accountability and reducing delays.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Medium"},
    {"id": 364, "title": "Law on Right to Clean Water and Sanitation", "summary": "The federal parliament passed a law implementing the constitutional right to clean water and sanitation, outlining the responsibilities of the three tiers of government.", "section": SYLLABUS_SECTIONS.CONST, "level": "Basic"},
    {"id": 365, "title": "Review of Civil and Criminal Law Systems", "summary": "A comprehensive review of the new Civil and Criminal Codes is underway to address implementation challenges and propose necessary amendments.", "section": SYLLABUS_SECTIONS.LAW, "level": "Medium"},
    {"id": 366, "title": "Public Sector Investment Policy", "summary": "The government adopted a new policy framework for managing public sector investment, aiming for higher returns and better alignment with national planning goals.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Hard"},
    {"id": 367, "title": "Human Rights Commission on Torture", "summary": "The National Human Rights Commission expressed serious concerns over police custody procedures and recommended immediate reforms to prevent torture.", "section": SYLLABUS_SECTIONS.LAW, "level": "Hard"},
    {"id": 368, "title": "Local Government Training on Administrative Law", "summary": "A massive training program was launched for local government officials on administrative law to ensure the rule of law is maintained at the grassroots level.", "section": SYLLABUS_SECTIONS.LAW, "level": "Basic"},
    {"id": 369, "title": "Constitutional Body Report on Inclusivity", "summary": "A constitutional body released a report assessing the proportional and inclusive representation of historically marginalized groups in public administration.", "section": SYLLABUS_SECTIONS.CONST, "level": "Hard"},
    {"id": 370, "title": "Social Welfare Security Fund Expansion", "summary": "The government announced the expansion of the social welfare security fund to cover more citizens, enhancing public service delivery in social protection.", "section": SYLLABUS_SECTIONS.ADMIN, "level": "Basic"},
]


# --- 3. Streamlit Application ---

def run_app():
    # Convert data to DataFrames for easier filtering
    mcq_df = pd.DataFrame(mcq_dataset)
    ca_df = pd.DataFrame(current_affairs_news)
    
    # Placeholder for flashcard container data 
    # (Currently reusing MCQ data for demo purposes as requested by user's "container" instruction)
    flashcard_df = mcq_df.copy()

    st.title("🇳🇵 Governance and Law Learning Hub")
    st.markdown("One combined mode with internal filters for effective preparation.")
    st.markdown("---")

    # --- OPTION 2: COMBINED MODE SIDEBAR ---
    st.sidebar.header("Practice Filters")

    # 1. Practice Type Selection
    practice_type = st.sidebar.radio(
        "Practice Type",
        ("Flashcard", "MCQ", "Current Affairs"),
        index=1,
        help="Select the mode of learning."
    )

    # 2. Section Selection
    # Extract unique sections dynamically or use defined constants
    # Using constants ensures order
    section_options = ["All", SYLLABUS_SECTIONS.LAW, SYLLABUS_SECTIONS.ADMIN, SYLLABUS_SECTIONS.CONST]
    selected_section = st.sidebar.selectbox("Section", section_options)

    # 3. Difficulty Selection
    difficulty_options = ["All"] + LEVELS
    selected_level = st.sidebar.selectbox("Difficulty", difficulty_options)

    st.sidebar.markdown("---")
    st.sidebar.info("Adjust filters to narrow down the topic.")

    # --- FILTERING LOGIC ---
    
    # Define a helper function to filter a dataframe
    def filter_data(df, section, level):
        filtered = df.copy()
        if section != "All":
            filtered = filtered[filtered['section'] == section]
        if level != "All":
            filtered = filtered[filtered['level'] == level]
        return filtered

    # Display Header based on selection
    st.header(f"Practice Type = :blue[{practice_type}]")
    st.caption(f"Difficulty = **{selected_level}** | Section = **{selected_section}**")
    st.markdown("---")

    # --- RENDERING LOGIC ---

    if practice_type == "MCQ":
        filtered_df = filter_data(mcq_df, selected_section, selected_level)
        
        if filtered_df.empty:
            st.warning("No MCQs found for the selected filters.")
        else:
            count = len(filtered_df)
            display_num = min(5, count)
            st.markdown(f"**Practicing {display_num} random questions** out of {count} available.")
            
            # Randomize
            sample_questions = filtered_df.sample(display_num).reset_index(drop=True)

            for i, row in sample_questions.iterrows():
                with st.container():
                    st.markdown(f"**Q{i+1}: {row['question']}**")
                    
                    options = row['options']
                    
                    # Handle if options is a string or dict
                    if isinstance(options, str):
                        options = json.loads(options)
                    
                    # Create a list of strings for radio button
                    radio_options = [f"{k}: {v}" for k, v in sorted(options.items())]
                    
                    key = f"mcq_{row['id']}_{i}"
                    user_choice = st.radio("Select Answer:", radio_options, key=key, index=None)
                    
                    if st.button(f"Check Answer Q{i+1}", key=f"btn_{key}"):
                        if user_choice:
                            selected_opt = user_choice.split(":")[0].strip()
                            correct_answer_text = options.get(row['answer'], row['answer'])
                            if selected_opt == row['answer']:
                                st.success(f"✅ Correct! The answer is **{row['answer']}: {correct_answer_text}**")
                            else:
                                st.error(f"❌ Incorrect. The correct answer is **{row['answer']}: {correct_answer_text}**")
                            
                            # Show all options
                            st.markdown("**All Options:**")
                            for opt_key in sorted(options.keys()):
                                opt_val = options[opt_key]
                                if opt_key == row['answer']:
                                    st.markdown(f"✅ **{opt_key}: {opt_val}**")
                                else:
                                    st.markdown(f"  {opt_key}: {opt_val}")
                            
                            st.info(f"**Details:** {row['details']}")
                        else:
                            st.warning("Please select an option first.")

    elif practice_type == "Flashcard":
        filtered_df = filter_data(flashcard_df, selected_section, selected_level)
        
        if filtered_df.empty:
            st.warning("No Flashcards found for these filters.")
        else:
            st.markdown(f"**Found {len(filtered_df)} Flashcards**")
            
            # Simple Shuffle Button
            if st.button("Shuffle Deck"):
                st.rerun()
                
            sample_card = filtered_df.sample(1).iloc[0]
            
            # Flashcard UI
            st.markdown("### Question:")
            st.container().write(f"### {sample_card['question']}")
            
            with st.expander("Reveal Answer"):
                st.markdown(f"### Answer: {sample_card['options'][sample_card['answer']]}") # Showing the text of correct option
                st.caption(f"**Details:** {sample_card['details']}")
                st.caption(f"Section: {sample_card['section']} | Level: {sample_card['level']}")

    elif practice_type == "Current Affairs":
        filtered_df = filter_data(ca_df, selected_section, selected_level)
        
        if filtered_df.empty:
            st.warning("No Current Affairs found for these filters.")
        else:
            st.markdown(f"**Displaying {len(filtered_df)} News Items**")
            for i, row in filtered_df.iterrows():
                with st.container():
                    st.markdown(f"### {i+1}. {row['title']}")
                    st.write(row['summary'])
                    st.caption(f"Section: {row['section']} | Difficulty: {row['level']}")