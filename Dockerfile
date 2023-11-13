FROM python:latest

WORKDIR /app

# compy requirement.txt file to the working directory
COPY requirements.txt .

# Install any necessary packages
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the working directory
COPY . .

# Expose any necessary ports
EXPOSE 8000

# set the permision to the start script
RUN chmod +x start.sh

# start the application
CMD ["./start.sh"]


