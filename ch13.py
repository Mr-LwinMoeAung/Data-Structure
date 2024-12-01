print('*** Converting hh.mm.ss to seconds ***')
hh,mm,ss=input('Enter hh mm ss : ').split()
hh=int(hh)
mm=int(mm)
ss=int(ss)

hh1=hh*60*60
mm1=mm*60

box=[hh,mm,ss]

for i in range(1,len(box)):
    if box[i]>=60 or '-' in str(box[i]):
        print(f'mm({box[i]}) is invalid!')
        exit()

ans=hh1+mm1+ss

print(f'{hh:02d}:{mm:02d}:{ss:02d} = {ans:,} seconds')