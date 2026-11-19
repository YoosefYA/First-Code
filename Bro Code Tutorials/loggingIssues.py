log_file = None
try:
    log_file = open("log.txt", 'w')
    log_file.write("Application Started.\n")
    log_file.write("User 'admin' logged in\n")
except IOError as e:
    print(f"Error writing initial log: {e}")