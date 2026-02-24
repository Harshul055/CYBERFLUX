def calculate_risk(result):
    score = 0

    # Simple addition of all integer checks
    for value in result.values():
        if isinstance(value, int):
            score += value

    # 3 Risk Levels
    if score <= 2:
        level = "Safe"
    elif score <= 5:
        level = "Suspicious"
    else:
        level = "Malicious"

    # Simple confidence logic
    confidence = score * 10
    if confidence > 100:
        confidence = 100

    return score, level, confidence
