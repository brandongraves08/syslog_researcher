class LogAnalyzer:
    def __init__(self):
        pass

    def identify_critical_logs(self, logs):
        """Identifies critical logs from a list of log entries."""
        critical_logs = []
        for log in logs:
            if 'error' in log.lower() or 'critical' in log.lower():
                critical_logs.append(log)
        return critical_logs