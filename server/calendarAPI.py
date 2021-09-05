from googleapiclient.discovery import build
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

# Used for requests that require authorization
# Returns an authorised object used for making API calls
def apiOAuth():

    SCOPES = "https://www.googleapis.com/auth/calendar"
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=SCOPES)

    try:
        creds = pickle.load(open("./tokens/calendarToken.pkl", "rb"))
    except:
        creds = flow.run_local_server()
        pickle.dump(creds, open("./tokens/calendarToken.pkl", "wb"))

    # print(creds)
    service = build("calendar", "v3", credentials = creds)

    return service


# Returns a list containing all of a user's calendars
def calendarListList(auth):

    page_token = None
    calendars = []

    while True:
        calendar_list = auth.calendarList().list(pageToken=page_token).execute()

        for calendar_list_entry in calendar_list['items']:
            calendars.append(calendar_list_entry["id"])

        page_token = calendar_list.get('nextPageToken')

        if not page_token:
            break

    return calendars


# Returns a single calendar referenced by supplied 
def calendarListGet(auth, id):
    calendar_list_entry = auth.calendarList().get(calendarId=id).execute()

    return calendar_list_entry


# Returns a list of all events associated with the calendar referenced by calId
def eventList(auth, calId):
    page_token = None
    listEvents = []

    while True:
        events = auth.events().list(calendarId = calId, pageToken=page_token).execute()
        
        for event in events['items']:
            listEvents.append(event)

        page_token = events.get('nextPageToken')

        if not page_token:
            break

    return listEvents


# Returns a single event specified by event id
def eventGet(auth, calId, eventId):
    event = auth.events().get(calendarId = calId, eventId = eventId).execute()

    return event


# Inserts a new event into the calendar referenced by supplied id
def eventInsert(auth, calId, noti, event):

    auth.events().insert(calendarId = calId, sendNotifications = noti, body = event).execute()


# Update an existing event with new information
def eventUpdate(auth, calId, event):

    auth.events().update(calendarId = calId, eventId = event["id"], body = event).execute()


# Delete an existing event
def eventDelete(auth, calId, eventId):

    auth.events().delete(calendarId = calId, eventId = eventId).execute()


# Moves an event from one calendar to another (changes the organizer)
def eventMove(auth, calId, eventId, destCalId):

    auth.events().move(calendarId = calId, eventId = eventId, destination = destCalId).execute()









# GMTOffset = '+01:00'

# eventData = {
#     "id": "upqjigdujbgo1po7p901ms164g",
#     "summary": "Test",
#     "start": {"dateTime": "2021-09-03T15:00:00%s" % GMTOffset},
#     "end": {"dateTime": "2021-09-03T18:00:00%s" % GMTOffset}
# }
