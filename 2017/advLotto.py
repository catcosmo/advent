# BETRIEBSANLEITUNG ADVENTSKALENDER 2018

import datetime

wg = {
    0: 'peter',
    1: 'julia',
    2: 'jule',
    3: 'julz',
    4: 'hein',
    5: 'manou',
    6: 'kutzi',
    7: 'cat'
}

now = datetime.datetime.now()

jackpot = now.day % 8

print 'adventskalendergluckskind des tages ist ' + wg[jackpot] + '!'

# HOHOHO!

# Losungshinweis 1: google([modulo, datetime, python])
# Losungshinweis 2: dies ist 1 python script das die richtige antwort ausgibt wenn man es ausfuhrt.
#                   ihr findet es hier: https://github.com/catcosmo/advent/blob/master/advLotto.py