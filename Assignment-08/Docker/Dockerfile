FROM python

# Expose port you want your app on
EXPOSE 8501

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

# Copy app code and set working directory
COPY . .
WORKDIR /app

# Run
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
################################################################################okkkkkkkkkkkkkkkkkkkkkk

# FROM python

# EXPOSE 8501


# RUN pip install -U pip

# RUN pip install streamlit
# RUN pip install opencv-python
# RUN pip install pillow
# RUN pip install numpy
# RUN pip install python-multipart
# COPY . .
# WORKDIR /app



# # Run
# ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

####################################################################################okkkkkkkkkkkkkkkkkkkkkkkk
