def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as f:
        for line in f:
            logs.append(line.strip())

    return logs
