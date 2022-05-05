import requests, datetime, time
from discord.ext import commands, tasks

token = '***********************************************************'
bot = commands.Bot(command_prefix='!')

client_id = '******************************'
client_secret = '******************************'
streamer_name = 'USF_Esports'

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)
keys = r.json()
headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']}

@bot.event
async def on_ready():
    social_check.start()
    print('bot active')



@tasks.loop(seconds=5)
async def social_check():
    stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)
    stream_data = stream.json()
    if len(stream_data['data']) == 1:
        start_time = str(stream_data['data'][0]['started_at'])[0:-1]
        start_obj = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S')
        current_time = datetime.datetime.utcnow() - datetime.timedelta(seconds=300)
        if start_obj > current_time:
            channel = bot.get_channel(************************)
            await channel.send('USF Esports is now live on https://www.twitch.tv/usf_esports ! Go check it out!')
            time.sleep(600)

bot.run(token)
