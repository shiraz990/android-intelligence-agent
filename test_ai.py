from ai_reviewer import review_project

summary = """
Health Score: 84

Compose: Yes
Material3: Yes

ViewModels: 0
Repositories: 0

Warnings

No Repository

No ViewModel

2 TODO comments

1 Log.d()
"""

print(review_project(summary))