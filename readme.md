# Read text message content from Twillio webhooks

## Motivation
This project initially started out as a way to get around the Chat-GPT requirement for a phonenumber, but this proved fruitless since they can detect Twillio numbers as not being "real" numbers. However, this script can still be used to read incoming text messages to your Twillio number for other reasons.

It's likely this scirpt can be used to parse the payload sent by Twillio and set up a Slack webhook to read the messages as well without all the coding.

## Setup
- Have vanilla python set up on your machine.
- Reserve an IP for the host on your router.
- Forward a port for the host on the router. The port specified in the script is 42069.
    - You will want to ensure you're in a single NAT topology for this to work.
- Run `python receive_twillio_texts.py` from the directory of this script.
- Set up a [Twillio account](http://twillio.com/)
- Set up a phone number in Twillio.
- Set up a webhook for the phone number in Twillio under the messages section when managing the phone number.
- Webhook address should be: `http://YOUR-PUBLIC-IP-GOES-HERE:42069`
    - If you updated the port this script runs on, change `42069` to the port number you specified. 
- Send a text message to your Twillio phone number.

