from speedtest import SpeedTest
from twitter import Twitter

from dotenv import load_dotenv

load_dotenv()

# ------------------------ SpeedTest
speed_test = SpeedTest()
speed_test.execute()
speed_test_data = speed_test.get_collected_data()
message = speed_test.generate_message()
# ------------------------ Twitter
tweet = Twitter()
tweet.login_process()
tweet.write_tweet(message)
