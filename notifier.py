import slack
def notify(message,channel,username,icon_emoji):
    token  = "Your Token" ## you can get it from here https://api.slack.com/custom-integrations/legacy-tokens    
    client = slack.WebClient(token=token)
    try:
        client.chat_postMessage(channel=channel,text=message,username=username,icon_emoji=icon_emoji)
    except:
        pass
message   = "test"
channel   = "#general"
username  = "MyBot"
icon_emoji= ":robot_face"
notify(message,channel,username,icon_emoji)
