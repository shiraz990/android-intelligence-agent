# android-intelligence-agent


🤖 Android Intelligence Agent

An AI-powered Android project analysis tool that combines static analysis, rule-based code inspection, health scoring, and local Large Language Models (LLMs) to generate professional Android engineering reviews.

Built with Python, Streamlit, Ollama, and Qwen2.5-Coder.

✨ Features
📂 Scan Android projects automatically
📊 Calculate an Android Health Score
🏗 Analyze Android project architecture
🔍 Detect Android technologies (Compose, Hilt, Room, Retrofit, etc.)
🛡 Perform rule-based quality and security checks
🤖 Generate AI-powered engineering reviews
🔒 Analyze projects locally using Ollama (no cloud API required)
🏗 Architecture
Android Project
│
▼
Project Scanner
scanner.py
│
▼
┌─────────────────────────┐
│                         │
▼                         ▼
Static Analyzer             Rules Engine
analyzer.py              rules_engine.py
│                         │
└─────────────┬───────────┘
▼
Health Score Engine
│
▼
Project Intelligence Summary
│
▼
AI Reviewer Agent
ai_reviewer.py
│
▼
Ollama + Qwen2.5-Coder
│
▼
Streamlit Dashboard
📂 Project Structure
android-intelligence-agent/

├── app.py
├── analyzer.py
├── ai_reviewer.py
├── scanner.py
├── rules_engine.py
├── health_score.py
├── test_ai.py
├── requirements.txt
└── README.md
🔍 What Gets Analyzed?
Architecture
Activities
Fragments
ViewModels
Repositories
Compose Screens
Android Technologies
Jetpack Compose
Material3
Navigation
Hilt
Retrofit
Room
WorkManager
Coroutines
Code Quality
TODO comments
FIXME comments
println()
Log.d()
HTTP URLs
Possible API Keys
Large source files
AI Review

The AI generates a structured engineering report covering:

Overall Summary
Architecture Review
Code Quality
Performance
Security
Scalability
Testing
Best Practices
Priority Fixes
🚀 Installation
Clone the repository
git clone https://github.com/shiraz990/android-intelligence-agent.git

cd android-intelligence-agent
Install dependencies
pip install -r requirements.txt
Install Ollama

Download and install Ollama from:

https://ollama.com

Download the AI model
ollama pull qwen2.5-coder:1.5b
Run the application
streamlit run app.py

Then open:

http://localhost:8501
📋 Example Workflow
Enter the path to an Android project.
Scan Kotlin, Java, XML, Gradle, and version catalog files.
Detect Android architecture components and technologies.
Perform rule-based code quality and security checks.
Calculate an Android Health Score.
Generate an AI-powered engineering review.
View the results in the Streamlit dashboard.
🛣 Roadmap
Android Studio Plugin
GitHub Pull Request Reviewer
AI-powered Code Fix Suggestions
Multi-module Project Support
PDF Report Export
Firebase Crashlytics Integration
CI/CD Integration
🤝 Contributing

Contributions, bug reports, and feature requests are welcome.

If you'd like to improve the project, feel free to open an issue or submit a pull request.

📄 License

MIT License

👨‍💻 Author

Muhammad Shiraz

Senior Android Developer | AI Enthusiast

If you find this project useful, consider giving it a ⭐ on GitHub.