import subprocess
import time
import requests

def execute_program():
    # Replace 'http://localhost:8000/run_program' with the appropriate URL
    url = 'http://localhost:8000/client.py'
    
    try:
        # Introduce a delay before triggering the execution (optional)
        time.sleep(5000)  # Adjust the delay as needed
        
        # Make a GET request to trigger the execution
        response = requests.get(url)
        
        # Check the response status
        if response.status_code == 200:
            print("Program executed successfully")
        else:
            print(f"Failed to execute program. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

if __name__ == "__main__":
    # Start the program to be executed in the localhost server
    program_path = 'video_to_audio.py'  # Replace with the path to your Python program
    
    # Start the program in a separate process
    subprocess.Popen(['python', program_path])
    
    # Call the function to trigger the execution via HTTP request
    execute_program()
