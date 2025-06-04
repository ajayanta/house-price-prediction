#base image
FROM python:3.10
#workdir 
WORKDIR /app
# copy 
COPY . .
# run
RUN pip install --no-cache-dir -r requirements.txt
# port
EXPOSE 8501
# command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


