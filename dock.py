import docker
import os
#from tqdm import tqdm

client = docker.from_env()

try: 
    text_example = client.containers.run("fedora:latest", "echo man")
    # remove 'b':
    # https://stackoverflow.com/questions/37016946/remove-b-character-do-in-front-of-a-string-literal-in-python-3
    # remove '\n':
    # https://www.geeksforgeeks.org/python-string-strip/
    out = text_example.decode("utf-8").strip()
    print(out)
# Found near the end of the run function in the manual:
# https://docker-py.readthedocs.io/en/stable/containers.html#docker.models.containers.ContainerCollection.run
except docker.errors.APIError as e:
    print(f"An error occurred: {e}")


# Running ls command
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
    
    print(output)
except docker.errors.APIError as e:
    print(f"An error occurred: {e}")

# Pulling Fedora. From ChatGPT
#try:
#    # Pull the image
#    image = client.pull('fedora:latest', stream=True, decode=True)
#
#    # Display progress bar
#    for line in tqdm(image, desc='Pulling image'):
#        pass  # This loop consumes the generator to trigger tqdm updates
#except docker.errors.APIError as e:
#    print(f"An error occurred: {e}")
