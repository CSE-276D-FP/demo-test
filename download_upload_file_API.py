import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload



def access_google_drive():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_CSE276D.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file(service, local_file_path, drive_file_path):
    file_ = {'name': os.path.basename(drive_file_path)}
    media = MediaFileUpload(local_file_path, resumable=True)
    request = service.files().create(body=file_, media_body=media)
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print("Uploaded %d%%." % int(status.progress() * 100))
    print("File uploaded successfully.")

def download_file(service, drive_file_path, local_file_path):
    request = service.files().get_media(fileId=drive_file_path)
    fh = open(local_file_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        if status:
            print("Downloaded %d%%." % int(status.progress() * 100))
    print("File downloaded successfully.")
    
    
    
    # Access Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']
drive_service = access_google_drive()

if drive_service is not None:
    # Example: Upload a file
    local_file_path = 'path/to/local/file.jpg'
    drive_file_path = 'path/in/drive/file.jpg'
    upload_file(drive_service, local_file_path, drive_file_path)

    # Example: Download a file
    drive_file_path = 'drive_file_id'
    local_file_path = 'path/to/local/downloaded/file.jpg'
    download_file(drive_service, drive_file_path, local_file_path)
else:
    print("Access failed. Please check your access token or internet connection.")

