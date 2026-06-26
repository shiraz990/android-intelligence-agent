import subprocess
import re
import os


def clean_output(text):
    """
    Remove ANSI escape sequences from terminal output.
    Fixes characters like:
    [9D[K
    """
    ansi_escape = re.compile(
        r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])'
    )

    return ansi_escape.sub('', text)


def review_project(project_summary):

    prompt = f"""
You are a Staff Android Engineer with 15 years of experience.

You are reviewing an Android project.

Analyze ONLY the information provided below.

DO NOT invent missing information.

If something is missing, explain its impact.

Return your review using the following sections.

# Overall Summary

# Architecture Review

Score /10

Strengths

Weaknesses

Recommendations


# Code Quality

Score /10

Strengths

Weaknesses

Recommendations


# Performance

Score /10

Potential Issues

Optimizations


# Security

Score /10

Potential Risks

Recommendations


# Scalability

Score /10


# Testing

Score /10


# Best Practices


# Priority Fixes

List the top 10 improvements in priority order.


Here is the Android project summary:

{project_summary}


Keep the review professional and concise.
"""

    try:

        response = subprocess.run(

            [
                "ollama",
                "run",
                "qwen2.5-coder:1.5b"
            ],

            input=prompt,

            capture_output=True,

            text=True,

            encoding="utf-8",

            env={
                **os.environ,
                "NO_COLOR": "1"
            }

        )


        if response.returncode != 0:
            return f"""
Ollama Error:

{response.stderr}
"""


        cleaned_response = clean_output(response.stdout)


        return cleaned_response.strip()


    except Exception as e:

        return f"Error while generating review: {str(e)}"