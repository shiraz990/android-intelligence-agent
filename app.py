import streamlit as st

from scanner import scan_project
from analyzer import analyze_project
from ai_reviewer import review_project

st.set_page_config(
    page_title="Android Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Android Intelligence Agent")

project_path = st.text_input(
    "Android Project Path",
    "/Users/shiraz/Documents/Android/AutomationApp"
)

if st.button("Analyze Project"):

    with st.spinner("Scanning Android Project..."):

        project = scan_project(project_path)

        result = analyze_project(project)

    st.success("Project analyzed successfully!")

    health = result["health_score"]

    if health >= 90:
        st.success(f"🟢 Android Health Score : {health}/100")
    elif health >= 70:
        st.warning(f"🟡 Android Health Score : {health}/100")
    else:
        st.error(f"🔴 Android Health Score : {health}/100")

    st.markdown("---")

    st.header("📊 Project Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Kotlin Files", result["kotlin_files"])
        st.metric("Activities", result["activities"])
        st.metric("Compose Screens", result["compose"])

    with col2:
        st.metric("ViewModels", result["viewmodels"])
        st.metric("Repositories", result["repositories"])
        st.metric("Tests", result["tests"])

    with col3:
        st.metric("Fragments", result["fragments"])
        st.metric("Services", result["services"])
        st.metric("Receivers", result["receivers"])

    st.markdown("---")

    st.header("🛠 Technologies")

    technologies = result["technologies"]

    for tech in technologies:
        if technologies[tech]:
            st.success("✅ " + tech)
        else:
            st.error("❌ " + tech)

    st.markdown("---")

    st.header("🛡 Rules Engine")

    rules = result["rules"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("TODO", rules["todo"])
        st.metric("FIXME", rules["fixme"])

    with col2:
        st.metric("println()", rules["println"])
        st.metric("Log.d()", rules["logd"])

    with col3:
        st.metric("HTTP URLs", rules["http"])
        st.metric("API Keys", rules["apikey"])

    if len(result["recommendations"]) > 0:

        st.markdown("---")

        st.header("📌 Rule Based Recommendations")

        for recommendation in result["recommendations"]:
            st.warning(recommendation)

    st.markdown("---")

    st.header("🤖 AI Review")

    summary = f"""
Project Health Score : {result['health_score']}

Activities : {result['activities']}
Fragments : {result['fragments']}
Services : {result['services']}
Receivers : {result['receivers']}

Kotlin Files : {result['kotlin_files']}

Compose Screens : {result['compose']}

ViewModels : {result['viewmodels']}

Repositories : {result['repositories']}

Tests : {result['tests']}

Technologies

Jetpack Compose : {technologies['Jetpack Compose']}
Material3 : {technologies['Material3']}
Navigation : {technologies['Navigation']}
Hilt : {technologies['Hilt']}
Retrofit : {technologies['Retrofit']}
Room : {technologies['Room']}
WorkManager : {technologies['WorkManager']}
Coroutines : {technologies['Coroutines']}

Rules

TODO : {rules['todo']}
FIXME : {rules['fixme']}
println : {rules['println']}
Log.d : {rules['logd']}
HTTP : {rules['http']}
API Keys : {rules['apikey']}

Recommendations

{chr(10).join(result["recommendations"])}
"""

    with st.spinner("AI is reviewing your Android project..."):

        ai_review = review_project(summary)

    st.info(ai_review)

    st.markdown("---")

    st.header("📂 Kotlin Files")

    for file in project["kotlin_files"]:
        st.text(file)

    st.markdown("---")

    st.header("📄 Project Preview")

    preview = ""

    for file in project["files"][:3]:

        preview += f"\n// ===== {file['name']} =====\n\n"

        preview += file["content"][:3000]

        preview += "\n\n"

    st.code(preview, language="kotlin")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit + Ollama")