from random import choice
from emoji import emojize
from datetime import datetime
from pymongo import MongoClient

from settings import MONGO_DB, MONGO_LINK, USER_EMOJI

client = MongoClient(MONGO_LINK)

db = client[MONGO_DB]

def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({'user_id': effective_user.id})
    if not user:
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "username": effective_user.username,
            "chat_id": chat_id,
            "emoji": emojize(choice(USER_EMOJI), use_aliases=True)
        }
        db.users.insert_one(user)
    return user

def save_form(db, user_id, form_data):
    user = db.users.find_one({"user_id": user_id})
    form_data['created'] = datetime.now()
    if 'form' not in user:
        db.users.update_one(
            {'_id': user['_id']},
            {'$set': {'form': [form_data]}}
        )
    else:
        db.users.update_one(
            {'_id': user['_id']},
            {'$push': {'form': [form_data]}}
        )

def subscribe_user(db, user_data):
    if not user_data.get('subscribed'):
        db.users.update_one(
            {'_id': user_data['_id']},
            {'$set': {'subscribed': True}}
        )

def unsubscribe_user(db, user_data):
   db.users.update_one(
        {'_id': user_data['_id']},
        {'$set': {'subscribed': False}}
    )
        
def get_subscribed(db):
    return db.users.find({'subscribed': True})