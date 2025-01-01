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

# Build Sphinx documentation
WORKDIR /home/appuser/chatbot/docs
RUN make html
WORKDIR /home/appuser/chatbot/docs/build/html

EXPOSE 8001

ENTRYPOINT ["python3", "-m", "http.server", "8001"]

# docker build -t bot_image --no-cache .
# docker run -it -p 127.0.0.1:8001:8001 --name bot_docs_container bot_image