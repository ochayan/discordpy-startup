import random

if messae.content == "スロット":
    slot_list = ['\U00002660', '\U00002663', '\U00002665', '\U00002666', ':seven:']
    A = random.choice(slot_list)
    B = random.choice(slot_list)
    C = random.choice(slot_list)
    await client.send_message(message.channel, "%s%s%s" % (A, B, C))
