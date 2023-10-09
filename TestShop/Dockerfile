# Use the official Python image
FROM python

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY req.txt /app/
RUN pip install --no-cache-dir -r req.txt

# Copy project files into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Start the application
CMD ["gunicorn", "TestShop.wsgi:application", "--bind", "0.0.0.0:8000"]
