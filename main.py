import socket
import sys
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import log_parser
import log_analyzer
import issue_researcher
import documentation_generator

class SyslogServer:
    def __init__(self, host='0.0.0.0', port=514):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        print(f'Syslog server listening on {self.host}:{self.port}')

    def listen(self):
        while True:
            data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
            print(f'Message from {addr}: {data}')
            threading.Thread(target=self.process_message, args=(data,)).start()

    def process_message(self, data):
        try:
            # Assuming data is a byte string; decode if necessary
            message = data.decode('utf-8')
            # Here you would parse, analyze, and process the message
            # For demonstration, just print the message
            print(f'Processing message: {message}')
            # Integrate with existing processing functions
            # parsed_data = log_parser.parse(message)
            # analysis_results = log_analyzer.analyze(parsed_data)
            # issues_found = issue_researcher.research(analysis_results)
            # documentation_generator.generate(issues_found)
        except Exception as e:
            print(f'Error processing message: {e}')

class Watcher:
    DIRECTORY_TO_WATCH = "."  # Directory to watch for new syslog files

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is created.
            print(f"New syslog file detected: {event.src_path}")
            try:
                parsed_data = log_parser.parse(event.src_path)
                analysis_results = log_analyzer.analyze(parsed_data)
                issues_found = issue_researcher.research(analysis_results)
                documentation_generator.generate(issues_found)
                print("File processed successfully.")
            except Exception as e:
                print(f"Error processing file {event.src_path}: {e}")

if __name__ == "__main__":
    syslog_server = SyslogServer()
    threading.Thread(target=syslog_server.listen).start()
    w = Watcher()
    w.run()
