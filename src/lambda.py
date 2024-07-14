import os
import openai


def lambda_handler(event, context):
    openai.api_key = os.environ["OPENAI_API_KEY"]

    response = openai.Completion.create(engine="text-davinci-003", prompt="Say this is a test", max_tokens=5)

    return {"statusCode": 200, "body": response.choices[0].text.strip()}
