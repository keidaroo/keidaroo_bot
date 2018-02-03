
import datetime
import random
from datetime import timedelta

import tweepy
from tweepy.api import API
from tweepy.auth import OAuthHandler
from tweepy.streaming import Stream, StreamListener

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

kuskemeigen = ['twitterはじめました', 'よかった', '今日から競プロを頑張ります',
               'ディープラーニングってどれ位層が深いとディープって呼ばれるのだろうか', '英語が読めるようになりたいなぁ',
               '英語が読めるようになりたいなぁ', '10円ガムおいしい 今日は一つあたりが出ました。',
               '今日も10円ガムが一つ当たりました。 4つ買ったので、すごくおいしい',
               'codeforces出ます', '無性に何かが作りたい気分', 'Kickするよ'
               ]

member = ['accidentガチャ', 'たんちゃんガチャ', 'RIANガチャ', 'niiガチャ', 'とがガチャ', 'bwamガチャ',
          'kakuガチャ', 'はねガチャ', 'けいだろうガチャ', 'なふもたんガチャ', 'らろんずガチャ', 'ぞへガチャ',
          'ミドリムシガチャ', 'じぇらんガチャ', 'よわそうガチャ', 'カコハテガチャ', 'ヴァネロピガチャ', 'ndifixガチャ',
          '物理好きガチャ',
          'mokoガチャ', 'うしガチャ', 'Trumpガチャ', '安倍晋三ガチャ', 'えいやガチャ', "sei0oガチャ",
          'ヒトデマンガチャ', 'ふぁぼんガチャ', 'たかしよガチャ', 'たつやんガチャ', '補集合ガチャ', 'beetガチャ',
          'カコハテガチャ', 'らびガチャ', 'ちくわガチャ']

memberid = ['accidentSHI', 'tancahn2380', 'RianDigital', 'nii1531', '57tggx',
            'babcs2035', 'kakudtm', 'hane1046', 'keidaroo', 'Nafmo2',
            'rullonz', 'zohe_alak',
            'kjuner8', 'Yukkuri_Jeran', 'yowasou_zako', 'kakko_hatena',
            'Vane11ope', 'ndifix', 'butsurizuki', 'e28880AIe28883', 'ei1333',
            'realDonaldTrump', 'AbeShinzo', 'eiya5498513', 'sei0o',
            'wait_sushi', 'syobon_hinata', 'tayo1325', 'tatuyan_edson',
            'complement_real', 'beet_aizu', 'kakko_hatena', 'rabi10090314', 'i_chikuwa_']

kinku = ['t.co', '定期', 'ポストに', 'ツイ廃結果', 'ガチャ']


def Follows():
    all_friends = list()
    for friend in tweepy.Cursor(api.friends_ids).items():
        all_friends.append(friend)
    return all_friends


def getfollowers():
    all_followers = list()
    for friend in tweepy.Cursor(api.followers_ids).items():
        all_followers.append(friend)
    return all_followers


class AbstractedlyListener(StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        print(u"{text}".format(text=status.text))
        # print(u"{name}({screen}) {created} via {src}\n".format(
    #        name=status.author.name, screen=status.author.screen_name,
    #        created=status.created_at, src=status.source))
        if status.author.screen_name == 'Keidarou':
            return
        if status.text.find('twitter.com') != -1:
            return
        if status.author.screen_name == 'SpidCorCandy':
            if status.text[0:2] != 'RT' and status.text[0] != '@':
                api.create_favorite(status.id)
                if random.randrange(0, 100) <= 9:
                    api.retweet(status.id)
        if 'RT' in status.text:
            return
        if 'AC' in status.text and 'ACM' not in status.text and status.author.screen_name == 'keidaroo':
            st = '@' + status.author.screen_name + ' ぽまえはもっと精進しろ！ｗ\n' + str(datetime.datetime.now())
            api.update_status(st, status.id)
            return
        if 'ねむい' in status.text and status.author.screen_name == 'keidaroo':
            st = '@' + status.author.screen_name + ' 「睡眠なんて死んでからいつでもできる」\n' + str(datetime.datetime.now())
            api.update_status(st, status.id)
            return
        # if status.author.screen_name == 'tancahn2380' or status.author.screen_name == 'Yukkuri_Jeran' or status.author.screen_name == 'keidaroo':
        #    if '@' in status.text or 'RT' in status.text:
        #        return
        #    st = '@' + status.author.screen_name + 'キ リ ト か な ー や っ ぱ り w w\n' + str(datetime.datetime.now())
        #    api.update_status(st, status.id)
        #    return
        if status.text.find('Kuske') != -1 and status.text.find('ガチャ') != -1:
            if(status.text.find('RT') != -1):
                return
            # もしKuskeガチャがひかれたら
            ran = random.randrange(0, len(kuskemeigen))
            st = '@' + status.author.screen_name + ' ' + kuskemeigen[ran]
            api.update_status(st, status.id)
        else:
            for mem in member:
                st = 'ごめんこれバグ！ｗ'
                if status.text.find(mem) != -1:  # メンバーがいる
                    target = memberid[member.index(mem)]
                    ran = random.randrange(0, 20)
                    itr = 0
                    for tweet in tweepy.Cursor(api.user_timeline,
                                               screen_name=target,
                                               exclude_replies=True).items():
                        if 'RT' in tweet.text:
                            continue
                        if tweet.text.find('t.co') != -1:
                            continue
                        flag = False
                        for kinsi in kinku:
                            if kinsi in tweet.text:
                                flag = True
                                break
                        if flag is True:
                            continue
                        if '@'in tweet.text:
                            continue
                        if len(status.text) > 130:
                            continue
                        st = '@' + status.author.screen_name + ' ' + tweet.text

                        if itr >= ran:
                            break
                        itr += 1
                    api.update_status(st, status.id)
                    return


if __name__ == '__main__':
    st = '起動しました！！ ' + str(datetime.datetime.now())
    api.update_status(st)
    all_follow = Follows()
    all_follower = getfollowers()
    '''for flwr in all_follower:
        if(flwr not in all_follow):
            api.create_friendship(flwr)
    for flw in all_follow:
        if(flw not in all_follower):
            api.destroy_friendship(flw)
    '''

    stream = Stream(auth, AbstractedlyListener(), secure=True)
    stream.userstream()
    # public_tweets=api.home_timeline()
# python3 tp.py
