def generate_schedule(timeline):

    weeks = max(1, timeline // 7)

    phases = [
        "Site Preparation",
        "Foundation Work",
        "Structural Work",
        "Brickwork & Walls",
        "Plastering",
        "Electrical & Plumbing",
        "Finishing & Painting"
    ]

    schedule = {}
    phase_duration = max(1, weeks // len(phases))

    current_week = 1
    for phase in phases:
        end_week = current_week + phase_duration
        schedule[phase] = f"Week {current_week} to {end_week}"
        current_week = end_week + 1

    return schedule