# CaloriTrack Backend Application

## Preparations

First, you need to create a GCP service account that allows you to create, read, and delete objects in storage buckets. Then, download the credentials as a `json` file and name it `credentials.json`. Also, ensure the service account is associated with your bucket.

## How to Run it?

There are two ways to run this. You can run it using the source code or you can use the docker image instead.

### Run with Source Code
- Ensure you have python installed. We recommend you to use python 3.12.3 or higher
- Clone this repo
- Create a `.env` file on the root directory and add all the required variables based on `env.example` file
- Add `credentials.json` file to the root directory
- Open your favorite terminal. Ensure you are currently at the root directory of the project
- Create a virtual environment by running `python -m venv env`
- Run the virtual environment. If you use Windows Powershell, run `env\Scripts\activate.ps1`. If you're using Windows Command Prompt, run `env\Scripts\activate.bat`. If you're using Linux or Mac OS, run `source env/bin/activate`.
- Install the required libraries by running `pip install -r requirements.txt` on the terminal
- Run `python manage.py migrate`
- Run `python manage.py runserver`
- Now the application is running on localhost:8000

### Run with Docker Image
- Ensure you have Docker installed on your machine
- To run it, just run `docker run --name <CONTAINER_NAME> -d -p <HOST_PORT>:8000 -e SECRET_KEY <SECRET_KEY> -e GS_BUCKET_NAME <GS_BUCKET_NAME> -e GS_PROJECT_ID -v <PATH_TO_CREDENTIALS>/credentials.json:/credentials.json <GS_PROJECT_ID> farkhansyawal/capstone:latest`
- Now, you can access it via localhost:<HOST_PORT>. Another thing, by using docker image, this application will allow another connection outside your device so please consider it if you are using the image in development