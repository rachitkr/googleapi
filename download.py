from __future__ import print_function
import io
import pickle
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaIoBaseDownload

file_id = '1GSpgSXLF_aagCyP0Vjip7Ht59y3LdSm1q9sYbvB_Hjs'
with open('token.pickle', 'rb') as token:
    creds = pickle.load(token)
service = discovery.build('drive', 'v3', credentials=creds)
request = service.files().export_media(fileId=file_id,
                                             mimeType='text/csv')
fh = io.FileIO('Test.csv', 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))
