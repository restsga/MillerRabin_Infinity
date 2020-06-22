import random
import numpy as np

#素数判定(ミラーラビン)
def miller_rabin(n):
    #自然数以外は判定しない
    if n<=0:
        return False
    #2は素数
    if n==2:
        return True
    #1は素数でない
    if n==1:
        return False
    #2以外の偶数は素数でない
    if n&1==0:
        return False

    #ここまででnは必ず奇数となる(=n-1は偶数)
    #n-1,0で開始
    d=n-1
    count=0

    #(2**s)*dのdを求める
    #2で割り切れる間割り続ける
    while d&1==0:
        d=d>>1
        count+=1

    #表示用カウンタ
    message_count=0
    message_k=0

    #底a(1～n-1の整数)を順に処理
    for a in range(1,n):

        #素数の可能性があればTrue
        flag=False
        
        #経過表示
        if message_count>=1000:
            message_count-=1000
            message_k+=1
            print(str(message_k)+"k")

        #(a**d)%n==1ならば素数の可能性あり
        if pow(a,d,n)==1:
            flag=True

        #0～count-1について(a**((2**k)*d))%n==n-1ならば
        #素数の可能性あり
        for k in range(0,count):
            if pow(a,d,n)==n-1:
                flag=True
            d=d<<1

        #全てFalseのまま通過した場合は確実に合成数
        if flag==False:
            return False

        #表示用カウンタを増加
        message_count+=1

    #全てのサンプルについて合成数と判定されなければ
    #一定以上の確率で素数
    return True

##メイン部分##
n=5555555999955555555559999999955555559999999999555559999999909955555999999999999955999999999995555999999995555555999999999995555555599999999955555559999995555555555599999955559955555999999559955555555999999955555555555999995555555555555559955555555555555599

if miller_rabin(n):
    print(str(n))
    print("は高確率で素数")
else:
    print("合成数")

