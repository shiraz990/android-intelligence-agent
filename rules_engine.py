from pathlib import Path
import re


def analyze_rules(files):

    result = {
        "todos": 0,
        "fixmes": 0,
        "printlns": 0,
        "logd": 0,
        "http_urls": 0,
        "api_keys": 0,
        "large_files": 0
    }

    for file in files:

        try:

            code = Path(file).read_text(
                encoding="utf-8",
                errors="ignore"
            )

            result["todos"] += code.count("TODO")
            result["fixmes"] += code.count("FIXME")
            result["printlns"] += code.count("println(")
            result["logd"] += code.count("Log.d(")

            result["http_urls"] += len(
                re.findall(r"http://[^\s\"']+", code)
            )

            result["api_keys"] += len(
                re.findall(
                    r'AIza[0-9A-Za-z\-_]{35}',
                    code
                )
            )

            lines = code.splitlines()

            if len(lines) > 300:
                result["large_files"] += 1

        except Exception:
            pass

    return result