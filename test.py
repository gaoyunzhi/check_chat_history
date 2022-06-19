#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater
import yaml
from telegram_util import matchKey

with open('token') as f:
	token = f.read().strip()

bot = Updater(token, use_context=True).bot

def test(file_name, setting_name):
	with open(setting_name) as f:
		setting = yaml.load(f, Loader=yaml.FullLoader)
	with open(file_name) as f:
		chat_history = yaml.load(f, Loader=yaml.FullLoader)
	sent = set()
	target = bot.get_chat(setting['target'])
	for message in chat_history['messages'][::-1]:
		if not matchKey(message, setting['keywords']):
			continue
		try:
			user_id = int(message.get('from_id').split('user')[-1])
		except:
			print(message)
			continue
		if user_id in sent:
			continue
		name = message.get('from')
		text = message.get('text')
		if name or text:
			print(message)
			continue
		text = ' '.join(text.split())
		log_markdown = '[%s](tg://user?id=%d) %d %s' % (name, user_id, user_id, text)
		log_html = '<a href="tg://user?id=%d">%s</a> %d %s' % (user_id, name, user_id, text)
		try:
			target.send_message(log_markdown, parse_mode='markdown')
		except:
			target.send_message(log_markdown, parse_mode='log_html')

if __name__ == '__main__':
	test('db/1.json', 'db/setting.ymal')

