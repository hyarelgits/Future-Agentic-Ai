# import redis library
import redis

# create Redis connection
r = redis.Redis(

    # Redis host
    host="localhost",

    # Redis port
    port=6379,

    # auto convert bytes to string
    decode_responses=True
)

# save chat message
def save_chat(user,message):

    # push message into Redis list
    r.lpush(

        # key name
        f"chat:{user}",

        # message value
        message
    )

# get messages
def get_chat(user):

    # return last ten chats
    return r.lrange(

        # redis key
        f"chat:{user}",

        # start position
        0,

        # end position
        10
    )
