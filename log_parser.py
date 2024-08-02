import re

class LogParser:
    def __init__(self):
        pass

    def parse_log(self, filepath):
        """Parses a syslog file and extracts log entries."""
        entries = []
        with open(filepath, 'r') as file:
            for line in file:
                # Assuming syslog standard format
                match = re.match(r'<\d+>\w{3} +\d+ \d{2}:\d{2}:\d{2} [\w-]+ [\w-]+: (.*)', line)
                if match:
                    entries.append(match.group(1))
        return entries