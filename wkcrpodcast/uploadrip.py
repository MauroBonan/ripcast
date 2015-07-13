import datetime
import soundcloud

# create a client object with access token
client = soundcloud.Client(
    client_id='d722828ad5b6a1851f675006dc50952b',
    client_secret='5a064c038b3e3451f4bdc0237ee4cb75',
    redirect_url='',
)

date = datetime.datetime.now().date().isoformat()

# upload audio file
track = client.post('/tracks', track={
    'title': 'Bird Flight {date}'.format(date=date),
    'asset_data': open('file.mp3', 'rb')
})

# print track link
print track.permalink_url
