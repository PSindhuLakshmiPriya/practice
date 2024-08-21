N = int(input())
M = int(input())
workers = [f'W{i}' for i in range(1, N)]
current_task = [None] * N
tasks = []
for _ in range(M):
    task_name, task_type, time = input().split()
    tasks.append((task_name, task_type, int(time)))
current_time = 0
output = []
for task in tasks:
    task_name, task_type, time = task
    if task_type == 'Machine':
        for i, worker in enumerate(workers):
            if current_task[i] is None:
                current_task[i] = task_name
                output.append((worker, task_name, current_time))
                break
    else:
        while None in current_task:
            current_time += 1
            for i in range(N):
                if current_task[i] is None:
                    continue
                if current_task[i] == task_name:
                    current_task[i] = None
                    output.append((workers[i], task_name, current_time))
                    break
output.sort(key=lambda x: (x[2], x[1]))
for result in output:
    print(f'{result[0]} {result[1]} {result[2]}')
