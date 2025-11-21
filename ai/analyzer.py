from datetime import datetime
import pandas as pd


def analyze_routines(routines):
    """
    Analyzes routine logs and extracts:
    - total study minutes
    - total screen minutes
    - best productive hour
    """

    # If no routines exist
    if len(routines) == 0:
        return {
            "total_study_minutes": 0,
            "total_screen_minutes": 0,
            "best_study_hour": None,
            "message": "No routines to analyze"
        }

    # Convert routine objects to list of dicts
    data = []
    for r in routines:
        # Ensure timestamp exists
        ts = r.timestamp if hasattr(r, "timestamp") else datetime.now()
        data.append({
            "activity": r.activity,
            "duration": r.duration,
            "timestamp": ts
        })

    # Create DataFrame
    df = pd.DataFrame(data)

    # Extract hour from timestamp
    df["hour"] = df["timestamp"].apply(lambda t: t.hour)

    # Total minutes calculated
    total_study = df[df["activity"].str.lower() == "study"]["duration"].sum()
    total_screen = df[df["activity"].str.lower() == "screen"]["duration"].sum()

    # Best productive hour (most study)
    study_df = df[df["activity"].str.lower() == "study"]
    if len(study_df) > 0:
        best_hour = int(study_df.groupby("hour")["duration"].sum().idxmax())
    else:
        best_hour = None

    # Return clean JSON
    return {
        "total_study_minutes": int(total_study),
        "total_screen_minutes": int(total_screen),
        "best_study_hour": best_hour,
        "message": "Analysis completed successfully"
    }

