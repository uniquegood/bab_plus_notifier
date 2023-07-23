import slack_sdk
import datetime as dt
import os

def slackMessageFormat(imageUrl):
    now = dt.datetime.now()
    today = now.strftime("%y년 %m월 %d일")
    title = today + " 오늘의 메뉴는???"

    return [
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": today + " 오늘의 메뉴는???"
			}
		},
        {
            "type": "image",
            "title": {
                "type": "plain_text",
                "text": today + " 오늘의 메뉴는???",
                "emoji": True
            },
            "image_url": imageUrl,
			"alt_text": "image1"
        }
    ]


def slackErrorMessageFormat(msg):
    now = dt.datetime.now()
    today = now.strftime("%y년 %m월 %d일")

    return [
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":alert: `Error` 메뉴를 불러오지 못했습니다.\n```" + today + "\n" + msg + "```"
			}
		},
    ]

def sendSlackMessage(imageUrl) :
    slackToken = os.getenv("TEST_TOKEN")
    channel = os.getenv("TEST_CHANNEL")
    client = slack_sdk.WebClient(token = slackToken)
    client.chat_postMessage(channel = channel, blocks = slackMessageFormat(imageUrl))

def sendSlackErrorMessage(msg) :
    slackToken = os.getenv("TEST_TOKEN")
    channel = os.getenv("TEST_CHANNEL")
    client = slack_sdk.WebClient(token = slackToken)
    client.chat_postMessage(channel = channel, blocks = slackErrorMessageFormat(msg))

