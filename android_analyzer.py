from pathlib import Path

def analyze_android_structure(files):

    result = {
        "activities": 0,
        "fragments": 0,
        "viewmodels": 0,
        "repositories": 0,
        "composables": 0,
        "tests": 0,

        "compose": False,
        "coroutines": False,
        "hilt": False,
        "room": False,
        "retrofit": False,
        "navigation": False,
        "workmanager": False,
        "material3": False
    }

    for file in files:

        filename = file.name.lower()

        if "activity" in filename:
            result["activities"] += 1

        if "fragment" in filename:
            result["fragments"] += 1

        if "viewmodel" in filename:
            result["viewmodels"] += 1

        if "repository" in filename:
            result["repositories"] += 1

        if "test" in filename:
            result["tests"] += 1

        try:

            code = Path(file).read_text(
                encoding="utf-8",
                errors="ignore"
            )

            if "@Composable" in code:
                result["composables"] += 1

            if "androidx.compose" in code:
                result["compose"] = True

            if "kotlinx.coroutines" in code:
                result["coroutines"] = True

            if "dagger.hilt" in code:
                result["hilt"] = True

            if "retrofit2" in code:
                result["retrofit"] = True

            if "androidx.room" in code:
                result["room"] = True

            if "navigation" in code:
                result["navigation"] = True

            if "workmanager" in code.lower():
                result["workmanager"] = True

            if "material3" in code.lower():
                result["material3"] = True

        except Exception:
            pass

    return result