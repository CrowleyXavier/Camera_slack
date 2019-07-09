# coding: utf-8

import os
import time
import picamera
import requests
import sys
import cv2
from slackbot.bot import respond_to
from slacker import Slacker
from slackbot.bot import listen_to

#picture 指定したチャンネルで「picture」とメッセージを送ると写真を撮ってその画像を送ります
#'picture'部分を変更して好きな文字にしてください
@listen_to('picture')
def takepicture_func(message):
    #撮影した画像の保存場所を指定する
    image_pass = ''
    cc = cv2.VideoCapture(0)
    img = cc.read()
    rr,cv2.imwrite(image_pass,img)

    # bot accountのトークンを入れる
    token= ''
    slacker = Slacker(token)
    #チャンネル名を入れる
    channel_name = '#'+ ''
    #チャンネルのIDを入れる
    channel_ID = ''

    result = slacker.files.upload(image_pass,channels = [channel_ID])
