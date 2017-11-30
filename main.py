#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: DeathByte


from PIL import Image, ExifTags
import header

class Choice_One(object):
    def __init__(self, next):
        self.__next = next

    def do(self, handler):
        if handler == '1':
            try:
                print 'Type the img path'
                img_path = raw_input()
                img = Image.open(img_path)
                exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
                print exif
                return ''
            except Exception as e:
                raise e.message
        else:
            return self.__next.do(handler)

class Choice_Zero(object):
    def __init__(self, next):
        self.__next = next
    
    def do(self, handler):
        if handler == '0':
            return '0'
        else:
            return self.__next.do(handler)

class No_Choice(object):
    def do(self, handler):
        pass

class main(object): # Chain-Resposibilty Pattern ;)
    def __init__(self):
        choice = ''

        while choice != '0':
            print '(1) Reading Img Metadata, (0) Exit'
            choice = raw_input()

            job = Choice_One(
                Choice_Zero(
                    No_Choice()
                )
            )
            job.do(choice)


if __name__ == '__main__':
    header.put()
    main()