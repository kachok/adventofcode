$count = 0

$min = 1000000000
$min_i = 0
$min_line=""

array=[]

File.open("problem20.input", "r") do |f|
    f.each_line do |line|
        puts $count, line
      arr=line.split(" ")
      #$a=arr(1)
      p = arr[0][3..-2].split(",")
      v = arr[1][3..-2].split(",")
      a = arr[2][3..-2].split(",")

      hash={:active=>1, :p=>{:x=>p[0].to_i, :y=>p[1].to_i, :z=>p[2].to_i}, :v=>{:x=>v[0].to_i, :y=>v[1].to_i, :z=>v[2].to_i}, :a=>{:x=>a[0].to_i, :y=>a[1].to_i, :z=>a[2].to_i}}

      total=a[0].to_i.abs+a[1].to_i.abs+a[2].to_i.abs
      
      array.push(hash)
        


    end
  end

  $i = 0
  $num = 500
  
  while $i < $num  do
    $j = 0
    $tot = 1000

    while $j < $tot  do
        array[$j][:v][:x]=array[$j][:v][:x]+array[$j][:a][:x]
        array[$j][:v][:y]=array[$j][:v][:y]+array[$j][:a][:y]
        array[$j][:v][:z]=array[$j][:v][:z]+array[$j][:a][:z]

        array[$j][:p][:x]=array[$j][:p][:x]+array[$j][:v][:x]
        array[$j][:p][:y]=array[$j][:p][:y]+array[$j][:v][:y]
        array[$j][:p][:z]=array[$j][:p][:z]+array[$j][:v][:z]
  
        $dist=array[$j][:p][:x].abs+array[$j][:p][:y].abs+array[$j][:p][:z].abs
  
        if $dist<$min
            $min=$dist
            $min_j=$j
        end

      $j +=1
    end    



    $j = 0
    $tot = 1000
    
    $min=10000000
    $min_j=-1

    while $j < $tot  do
        array[$j][:v][:x]=array[$j][:v][:x]+array[$j][:a][:x]
        array[$j][:v][:y]=array[$j][:v][:y]+array[$j][:a][:y]
        array[$j][:v][:z]=array[$j][:v][:z]+array[$j][:a][:z]

        array[$j][:p][:x]=array[$j][:p][:x]+array[$j][:v][:x]
        array[$j][:p][:y]=array[$j][:p][:y]+array[$j][:v][:y]
        array[$j][:p][:z]=array[$j][:p][:z]+array[$j][:v][:z]
  
        $dist=array[$j][:p][:x].abs+array[$j][:p][:y].abs+array[$j][:p][:z].abs
  
        if $dist<$min
            $min=$dist
            $min_j=$j
        end

      $j +=1
    end    

    puts "closest particle"
    puts $min_j

    $i +=1
  end

  #puts "answer is:"
  #puts $min_i
  #puts $min
  #puts $min_line

  #puts array
  # File is closed automatically at end of block

