import matplotlib.pyplot as plt

def draw_gantt_chart(processes):
    """Draw Gantt Chart for Process Execution Timeline"""
    start_times = [p['start_time'] for p in processes]
    burst_times = [p['burst_time'] for p in processes]
    process_ids = [p['id'] for p in processes]

    plt.figure(figsize=(10, 5))

    for i, process in enumerate(processes):
        plt.barh(f"P{process_ids[i]}", burst_times[i], left=start_times[i], edgecolor='black', color='skyblue')

        # Add process ID as label in the center of each bar
        mid_point = start_times[i] + burst_times[i] / 2
        plt.text(mid_point, f"P{process_ids[i]}", f"P{process_ids[i]}", ha='center', va='center', color='black', fontsize=10, fontweight='bold')

    plt.xlabel('Time')
    plt.title('Gantt Chart')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def calculate_metrics(processes):
    """Calculate and Print Performance Metrics"""
    total_waiting_time = sum(p['waiting_time'] for p in processes)
    total_turnaround_time = sum(p['turnaround_time'] for p in processes)

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
