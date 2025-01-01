FROM python:latest

# Create a new user "appuser" with a home directory
RUN groupadd -r appuser && useradd -r -m -g appuser appuser

USER appuser

# Copy files to container
COPY --chown=appuser:appuser . /home/appuser/chatbot
WORKDIR /home/appuser/chatbot

# Create virtual environment
RUN python -m venv venv

# Set PATH to include the virtual environment
ENV PATH="/home/appuser/chatbot/venv/bin:$PATH"

# Install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# docker build --build-arg OPENAI_KEY -t bot_image --no-cache .
# docker run -it -p 127.0.0.1:8000:8000 --name bot_app_container bot_image