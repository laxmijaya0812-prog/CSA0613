# Job Scheduling with Deadlines
# Design and Analysis of Algorithms - CO4_AT1

def job_scheduling(jobs):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Create time slots
    slots = [None] * (max_deadline + 1)

    total_profit = 0

    # Schedule each job
    for job_id, deadline, profit in jobs:

        # Check slots from deadline towards the first slot
        for slot in range(deadline, 0, -1):

            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break

    # Display the schedule
    print("Scheduled Jobs:", end=" ")

    for slot in range(1, max_deadline + 1):
        if slots[slot] is not None:
            print(slots[slot], end=" ")

    print()
    print("Max Profit =", total_profit)


# Number of jobs
n = 4

# Deadlines and profits
deadlines = [2, 1, 2, 1]
profits = [100, 19, 27, 25]

# Create jobs
jobs = []

for i in range(n):
    jobs.append((f"J{i + 1}", deadlines[i], profits[i]))

# Call the function
job_scheduling(jobs)
