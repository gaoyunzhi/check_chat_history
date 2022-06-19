#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater
import yaml

with open('token') as f:
	token = f.read().strip()

bot = Updater(token, use_context=True).bot

def test(file_name, setting_name):


if __name__ == '__main__':
	test('db/1.json', 'db/setting')