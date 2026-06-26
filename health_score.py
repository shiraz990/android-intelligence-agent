def calculate_health_score(result, rules):

    score = 100

    # Positive checks
    if result["compose"]:
        score += 5

    if result["material3"]:
        score += 5

    if result["viewmodels"] > 0:
        score += 10

    if result["repositories"] > 0:
        score += 10

    if result["tests"] > 0:
        score += 10

    # Negative checks
    score -= rules["todos"] * 2
    score -= rules["fixmes"] * 3
    score -= rules["printlns"] * 5
    score -= rules["logd"] * 2
    score -= rules["large_files"] * 5
    score -= rules["api_keys"] * 25

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return score