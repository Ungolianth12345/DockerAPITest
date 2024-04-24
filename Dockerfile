FROM continuumio/anaconda3:latest

# Set the working directory
WORKDIR /home

ENV PYTHONUNBUFFERED=1


# Install Jupyter Lab
RUN conda install -c conda-forge jupyterlab

# Expose the Jupyter port
EXPOSE 8888

# Command to run Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/home"]
