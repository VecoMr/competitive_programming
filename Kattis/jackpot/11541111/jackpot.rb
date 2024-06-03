n = gets.to_i
n.times do |i|
    a = gets.to_i
    l = gets.to_s.split().map(&:to_i)
    lcm = l[0]
    l.each do |x|
        lcm = (lcm*x).abs/x.gcd(lcm)
    end
    if lcm > 10**9 then
        puts "More than a billion."
    else
        puts lcm
    end
end