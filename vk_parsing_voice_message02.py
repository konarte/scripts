from BeautifulSoup import BeautifulSoup #подключаем суп =)

soup = BeautifulSoup(htmlText) #загружаем html в суп =)
divs = soup.findAll(name = ‘div’, attrs = {'class':'error'}) #ищем дивы
for div in divs:
print “”.join(div.findAll(text = True)) #выводим весь текст из divа
