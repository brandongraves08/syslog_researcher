# Syslog Researcher

## What it does

The Syslog Researcher is a comprehensive tool designed for the continuous monitoring, analyzing, and researching of system logs. It now includes a real-time syslog server that listens on port 514, allowing for direct ingestion of syslog messages.

## How to use it

1. **Real-time Syslog Server**: The system can directly receive syslog messages on port 514.
2. **Parsing Logs**: Use `log_parser.py` to parse syslog files or messages.
3. **Analyzing Logs**: After parsing, use `log_analyzer.py` to analyze the logs for specific patterns or issues.
4. **Researching Issues**: Use `issue_researcher.py` to research common issues found in the logs.
5. **Generating Documentation**: Finally, use `documentation_generator.py` to generate documentation based on the analysis.

This setup allows for both the processing of traditional syslog files and the handling of real-time syslog messages, providing a versatile tool for system log analysis.