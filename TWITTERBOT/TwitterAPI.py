import tweepy
import configparser
import logging
#creat logger and config parser
logger = logging.getLogger()
config = configparser.ConfigParser()
#Read config.ini
config.read('config.ini')
#Set corresponding values from the config
API_KEY = config['API_KEY']['APIKEY']
API_KEY_SECRET = config['API_KEY_SECRET']['APIKEYSECRET']
ACCESS_TOKEN = config['ACCESS_TOKEN']['ACCESSTOKEN']
ACCESS_TOKEN_SECRET = config['ACCESS_TOKEN_SECRET']['ACCESSTOKENSECRET']
#Function to check if the supplied keys are valid & create the api object
def createAPI():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Authentication Failed, please check that your keys are correct!')
        raise e
    return api
   