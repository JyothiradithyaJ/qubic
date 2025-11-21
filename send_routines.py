import requests

API = "http://127.0.0.1:8000"

# ---------------------------
# 1. Seed Routine Logs
# ---------------------------
routine_data = [
    {"activity": "Study", "duration": 120},
    {"activity": "Study", "duration": 90},
    {"activity": "Screen", "duration": 200},
    {"activity": "Exercise", "duration": 30},
    {"activity": "Break", "duration": 15},
    {"activity": "Study", "duration": 60},
]

# ---------------------------
# 2. Seed Tasks
# ---------------------------
task_data = [
    {"title": "Math Assignment", "deadline": "2025-02-01", "priority": 2},
    {"title": "Complete Python Project", "deadline": "2025-02-05", "priority": 1},
    {"title": "Read Chapter 4", "deadline": "2025-02-03", "priority": 3},
]

def seed_routines():
    print("\nSeeding Routine Logs...")
    for entry in routine_data:
        r = requests.post(f"{API}/routine/add", json=entry)
        print("Routine:", r.json())


def seed_tasks():
    print("\nSeeding Tasks...")
    for task in task_data:
        r = requests.post(f"{API}/tasks/add", json=task)
        print("Task:", r.json())


def verify():
    print("\nVerifying Seed...")
    routines = requests.get(f"{API}/routine/list").json()
    tasks = requests.get(f"{API}/tasks/list").json()
    print("\nRoutines in DB:", routines)
    print("\nTasks in DB:", tasks)


if __name__ == "__main__":
    print(" Starting Seeding Script...")
    
    seed_routines()
    seed_tasks()
    verify()

    print("\n Seeding Complete! Now test AI Recommendations.\n")

