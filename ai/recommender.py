def suggest_productivity(analysis):
    """
    Generates suggestions based on the analysis returned by analyzer.py.
    Always returns a clean list of suggestions.
    """

    suggestions = []

    # If no routines exist
    if analysis.get("total_study_minutes", 0) == 0 and analysis.get("total_screen_minutes", 0) == 0:
        return ["No routines logged. Please add routine entries for meaningful AI suggestions."]

    # Total minutes
    study = analysis.get("total_study_minutes", 0)
    screen = analysis.get("total_screen_minutes", 0)
    best_hour = analysis.get("best_study_hour")

    # 1. Study suggestions
    if study == 0:
        suggestions.append("You haven't logged any study sessions. Try to study at least 1 hour a day.")
    elif study < 60:
        suggestions.append("You studied less than 1 hour today. Try increasing it for better progress.")
    else:
        suggestions.append(f"Great! You studied {study} minutes today. Keep it up!")

    # 2. Screen suggestions
    if screen > 180:
        suggestions.append("Your screen time is high today. Try to reduce it to stay more productive.")
    else:
        suggestions.append(f"Good job keeping screen time to {screen} minutes.")

    # 3. Productive hour suggestion
    if best_hour is not None:
        suggestions.append(
            f"You seem most productive around {best_hour}:00 — plan your study sessions during this time."
        )
    else:
        suggestions.append(
            "I couldn't detect your most productive hour. Log more study entries to analyze this better."
        )

    return suggestions
