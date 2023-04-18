FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variables for PostgreSQL
ENV POSTGRES_HOST=localhost
ENV POSTGRES_DB=your_database
ENV POSTGRES_USER=your_username
ENV POSTGRES_PASSWORD=your_password

# Expose the port for the Flask app
EXPOSE 5000

# Start the Flask app
CMD [ "python", "app.py" ]