import re


def analyze_project(project):

    files = project["files"]

    result = {}

    kotlin_files = 0
    activities = 0
    fragments = 0
    services = 0
    receivers = 0
    compose = 0
    viewmodels = 0
    repositories = 0
    tests = 0

    todo = 0
    fixme = 0
    println = 0
    logd = 0
    http = 0
    apikey = 0
    large_files = 0

    technologies = {
        "Jetpack Compose": False,
        "Material3": False,
        "Navigation": False,
        "Coroutines": False,
        "Hilt": False,
        "Retrofit": False,
        "Room": False,
        "WorkManager": False
    }

    recommendations = []

    gradle_text = "\n".join(project["gradle_files"])
    gradle_text += "\n" + project["toml"]

    # --------------------------
    # Detect dependencies
    # --------------------------

    if "compose" in gradle_text.lower():
        technologies["Jetpack Compose"] = True

    if "material3" in gradle_text.lower():
        technologies["Material3"] = True

    if "navigation" in gradle_text.lower():
        technologies["Navigation"] = True

    if "retrofit" in gradle_text.lower():
        technologies["Retrofit"] = True

    if "room" in gradle_text.lower():
        technologies["Room"] = True

    if "workmanager" in gradle_text.lower():
        technologies["WorkManager"] = True

    if "coroutines" in gradle_text.lower():
        technologies["Coroutines"] = True

    if "hilt" in gradle_text.lower():
        technologies["Hilt"] = True

    # --------------------------
    # Analyze every source file
    # --------------------------

    for file in files:

        if file["type"] not in ["kotlin", "java"]:
            continue

        kotlin_files += 1

        code = file["content"]

        if len(code) > 15000:
            large_files += 1

        lower = code.lower()

        if "activity" in code:
            activities += 1

        if "fragment" in code:
            fragments += 1

        if "service" in code:
            services += 1

        if "receiver" in code:
            receivers += 1

        if "@composable" in lower:
            compose += lower.count("@composable")

        if "viewmodel" in lower:
            viewmodels += 1

        if "repository" in lower:
            repositories += 1

        if "@test" in lower:
            tests += 1

        todo += lower.count("todo")
        fixme += lower.count("fixme")
        println += lower.count("println(")
        logd += lower.count("log.d")

        http += lower.count("http://")

        if re.search(r'AIza[0-9A-Za-z\-_]{35}', code):
            apikey += 1

    # --------------------------
    # Health Score
    # --------------------------

    health = 100

    health -= todo
    health -= fixme
    health -= println
    health -= logd
    health -= http * 5
    health -= apikey * 10
    health -= large_files * 3

    if viewmodels == 0:
        health -= 5

    if repositories == 0:
        health -= 5

    if health < 0:
        health = 0

    # --------------------------
    # Recommendations
    # --------------------------

    if viewmodels == 0:
        recommendations.append(
            "⚠ No ViewModel detected. Consider using MVVM."
        )

    if repositories == 0:
        recommendations.append(
            "⚠ No Repository layer detected."
        )

    if technologies["Navigation"] is False:
        recommendations.append(
            "⚠ Jetpack Navigation is not detected."
        )

    if technologies["Hilt"] is False:
        recommendations.append(
            "⚠ Hilt dependency injection is missing."
        )

    if technologies["Retrofit"] is False:
        recommendations.append(
            "⚠ Retrofit is not detected."
        )

    if technologies["Room"] is False:
        recommendations.append(
            "⚠ Room database is not detected."
        )

    if technologies["Coroutines"] is False:
        recommendations.append(
            "⚠ Kotlin Coroutines are not detected."
        )

    if todo > 0:
        recommendations.append(
            f"⚠ {todo} TODO comments found."
        )

    if fixme > 0:
        recommendations.append(
            f"⚠ {fixme} FIXME comments found."
        )

    if println > 0:
        recommendations.append(
            f"⚠ Remove {println} println() statements."
        )

    if logd > 0:
        recommendations.append(
            f"⚠ Remove {logd} Log.d() statements."
        )

    if http > 0:
        recommendations.append(
            "⚠ HTTP URLs detected. Use HTTPS."
        )

    if apikey > 0:
        recommendations.append(
            "🚨 Possible API Key found."
        )

    # --------------------------
    # Return
    # --------------------------

    result["health_score"] = health

    result["kotlin_files"] = kotlin_files

    result["activities"] = activities
    result["fragments"] = fragments
    result["services"] = services
    result["receivers"] = receivers

    result["compose"] = compose
    result["viewmodels"] = viewmodels
    result["repositories"] = repositories
    result["tests"] = tests

    result["technologies"] = technologies

    result["recommendations"] = recommendations

    result["rules"] = {
        "todo": todo,
        "fixme": fixme,
        "println": println,
        "logd": logd,
        "http": http,
        "apikey": apikey,
        "large": large_files
    }

    return result