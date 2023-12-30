def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        return 0

processed_ids = '/home/ec2-user/local_results.txt'
total_ids = '/home/ec2-user/scripts/partial_ids.txt'

completed_tasks = count_lines(processed_ids)
total_tasks = count_lines(total_ids)


percent_completed = (completed_tasks / total_tasks) * 100

output = f"""
# HELP processed_tasks_percent The percentage of tasks completed
# TYPE processed_tasks_percent gauge
tasks_completed_percent{{label="tasks"}} {percent_completed:.2f}
"""

with open('/home/ec2-user/custom_prom_metrics/processed_tasks.prom', 'w') as metric_file:
    metric_file.write(output)