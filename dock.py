import docker
client = docker.from_env()

# check if docker is running, raise exception if false.
# Or don't and just go through a bunch of files per step.

"""
Things one can do:
list containers:
client.containers.list()

run containers:
client.containers.run("ubuntu", "echo hello world")

building containers:
" docker build -t getting-started . " is the same as
" client.images.build(path = "./", tag = "getting-started") "

pulling:
client.images.pull(fedora:39) doesn't work
client.images.pull(platform="fedora:39") doesn't work
client.images.pull("fedora:latest") DOES
"""