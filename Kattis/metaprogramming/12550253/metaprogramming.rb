d={}
$<.map{|i|a,*l=i.split
a=='define'?d[l[1]]=l[0]:puts((d[l[0]]&&d[l[-1]])?eval(l.map{|i| d[i] || i.gsub(/(?<!\=)\=(?!\=)/, '==') }.join):'undefined')}
