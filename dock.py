import docker
import os
from tqdm import tqdm

client = docker.from_env()

# Pulling Fedora. From ChatGPT
def dock_fedora():
    try:
        # Pull the image
        image = client.api.pull('fedora:latest', stream=True, decode=True)
    
        # Display progress bar
        # got the idea from bottom answer: 
        # https://stackoverflow.com/questions/65896588/how-to-capture-docker-pull-status
        for line in tqdm(image, desc='Pulling image', unit="MB"):
            pass  # This loop consumes the generator to trigger tqdm updates
    except docker.errors.APIError as e:
        print(f"An error occurred: {e}")

def dock_echo():
    try: 
        text_example = client.containers.run("fedora:latest", "echo man")
        # remove 'b':
        # https://stackoverflow.com/questions/37016946/remove-b-character-do-in-front-of-a-string-literal-in-python-3
        # remove '\n':
        # https://www.geeksforgeeks.org/python-string-strip/
        out = text_example.decode("utf-8").strip()
        return out
    # Found near the end of the run function in the manual:
    # https://docker-py.readthedocs.io/en/stable/containers.html#docker.models.containers.ContainerCollection.run
    except (docker.errors.APIError, docker.errors.DockerException) as e:
        return f"An error occurred: {e}"


# Running ls command
def dock_ls():
    current_directory = os.getcwd()
    try:
        # Run the 'ls' command in a new container with the current directory mounted
        result = client.containers.run(
            "fedora:latest",
            "ls",
            volumes={current_directory: {'bind': '/host', 'mode': 'rw'}},
            remove=True
        )
        # Decode bytes to string and remove trailing newline
        output = result.decode('utf-8').strip()
    
        return output
    except docker.errors.APIError as e:
        return f"An error occurred: {e}"



#dock_fedora()