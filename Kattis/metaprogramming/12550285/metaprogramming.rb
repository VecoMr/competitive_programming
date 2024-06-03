d={}
$<.map{|i|a,*l=i.split;a[0]=='d'?d[l[1]]=l[0]:puts(d[l[0]]&&d[l[-1]]?eval(l.map{|j|d[j]||j.gsub(/(?<!\=)\=(?!\=)/,'==')}.join):'undefined')}
