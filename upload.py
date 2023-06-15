#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


# In[ ]:


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
                '/Users/asra/Desktop/new.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    return service


# In[ ]:


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


# In[ ]:


# Access Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']
drive_service = access_google_drive()

if drive_service is not None:
    # Example: Upload a file
    local_file_path = '/Users/asra/Desktop/image.png'
    drive_file_path = 'path/in/drive/file.jpg'
    upload_file(drive_service, local_file_path, drive_file_path)


# In[ ]:




