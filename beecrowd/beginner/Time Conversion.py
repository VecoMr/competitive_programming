n=int(input())
print(f"{(n-60*(((n-n%60)//60)%60))//(60*60)}:{((n-n%60)//60)%60}:{n%60}")