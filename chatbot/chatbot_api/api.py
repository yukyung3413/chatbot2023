import hashlib
import hmac
import base64
import time
import requests
import json


class ChatbotMessageSender:

    # chatbot api gateway url
    ep_path = 'https://5vdrmo3dq4.apigw.ntruss.com/custom/v1/10349/47f09d02238cde8667e642440beb80e827f078c9620a81d15304d89adff569a7'
    # chatbot custom secret key
    secret_key = 'Wkp6VW16ZkhoZmp6a2hzZEVibmJBcVd3RGFRZGNFWm8='

    def req_message_send(self):
        question = ''
        timestamp = self.get_timestamp()
        request_body = {
            'version': 'v2',
            'userId': 'U47b00b58c90f8e47428af8b7bddcda3d1111111',
            'timestamp': timestamp,
            'bubbles': [
                {
                    'type': 'text',
                    'data': {
                        'description': question
                    }
                }
            ],
            'event': 'send'
        }

        ## Request body
        encode_request_body = json.dumps(request_body).encode('UTF-8')

        ## make signature
        signature = self.make_signature(self.secret_key, encode_request_body)

        ## headers
        custom_headers = {
            'Content-Type': 'application/json;UTF-8',
            'X-NCP-CHATBOT_SIGNATURE': signature
        }

        print("## Timestamp : ", timestamp)
        print("## Signature : ", signature)
        print("## headers ", custom_headers)
        print("## Request Body : ", encode_request_body)

        ## POST Request
        response = requests.post(headers=custom_headers, url=self.ep_path, data=encode_request_body)

        return response

    @staticmethod
    def get_timestamp():
        timestamp = int(time.time() * 1000)
        return timestamp

    @staticmethod
    def make_signature(secret_key, request_body):

        secret_key_bytes = bytes(secret_key, 'UTF-8')

        signing_key = base64.b64encode(hmac.new(secret_key_bytes, request_body, digestmod=hashlib.sha256).digest())

        return signing_key


if __name__ == '__main__':

    res = ChatbotMessageSender().req_message_send()

    print(res.status_code)
    if(res.status_code == 200):
        print(res.text)
        #print(res.read().decode("UTF-8"))