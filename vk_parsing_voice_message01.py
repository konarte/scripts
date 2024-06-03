#!/usr/bin/env python3
 
from html.parser import HTMLParser
 
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for i in range (0,len(attrs)):
                if attrs[i][0]=='data-mp3':
                    print(attrs[i][1])
                    print(attrs[i+1][1])
                    print('-------------')
 
if __name__ == "__main__":
    with open('1.html', encoding='Windows-1251') as fin:
        p = MyHTMLParser()
        p.feed(fin.read())
        p.close()


'''
See form
[('id', 'audiomsgpl_245934301_445424111'),
('class', 'audio-msg-track clear_fix audio-msg-track_player-attached'),
('aria-label', 'Вторимое письмо'),
('onclick', 'return AudioMessagePlayer.togglePlay(this,event);'),
('data-duration', '5'),
('data-mp3', 'https://cs540103.userapi.com/c804331/u245934301/audio/7eb1a23ffc.mp3'),
('data-ogg', 'https://cs540103.userapi.com/c804331/u245934301/audio/7eb1a23ffc.ogg')]
'''
