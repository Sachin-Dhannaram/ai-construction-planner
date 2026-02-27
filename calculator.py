def calculate_project(area, floors, timeline):

    total_area = area * floors

    cost_per_sqft = 1800

    labor_percentage = 0.30
    material_percentage = 0.60
    overhead_percentage = 0.10

    total_cost = total_area * cost_per_sqft

    labor_cost = total_cost * labor_percentage
    material_cost = total_cost * material_percentage
    overhead_cost = total_cost * overhead_percentage

    # Recommended timeline (simple realistic formula)
    recommended_timeline = max(30, int(total_area / 50))

    # Workforce base calculation
    base_workers = max(10, int(total_area / 300))

    if timeline < recommended_timeline:
        timeline_pressure = "High (Compressed Schedule)"
        base_workers += 5
    elif timeline > recommended_timeline:
        timeline_pressure = "Relaxed"
    else:
        timeline_pressure = "Normal"

    # Worker breakdown
    masons = int(base_workers * 0.25)
    helpers = int(base_workers * 0.30)
    steel_workers = int(base_workers * 0.15)
    carpenters = int(base_workers * 0.20)
    supervisors = max(1, int(base_workers * 0.10))

    # Material estimation
    cement_bags = int(total_area * 0.4)
    steel_kg = int(total_area * 3.5)
    sand_cuft = int(total_area * 1.8)

    return {
        "total_area_sqft": total_area,
        "total_cost": total_cost,
        "labor_cost": labor_cost,
        "material_cost": material_cost,
        "overhead_cost": overhead_cost,
        "recommended_timeline_days": recommended_timeline,
        "timeline_pressure": timeline_pressure,
        "worker_distribution": {
            "masons": masons,
            "helpers": helpers,
            "steel_workers": steel_workers,
            "carpenters": carpenters,
            "supervisors": supervisors,
            "total_workers": base_workers
        },
        "materials": {
            "cement_bags": cement_bags,
            "steel_kg": steel_kg,
            "sand_cuft": sand_cuft
        }
    }