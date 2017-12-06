
var banks: [Int] = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]

var combos = Set<String>()

print(banks)

var count: Int = 0

let str = (banks.map{String($0)}).joined(separator: ",")
combos.insert(str)

var curr: String = ""

while true {
    //print("iterating")
    
    var index=0
    var value=0
    for (i, e) in banks.enumerated() {
        //print("Item \(i): \(e)")
        if e>value {
            index=i
            value=e
        }
    }
    
    banks[index]=0
    while value>0 {
        index=(index+1) % banks.count
        banks[index]=banks[index]+1
        value=value-1
    }
    
    count=count+1
    
    curr=(banks.map{String($0)}).joined(separator: ",")

    if combos.contains(curr) {
        break
    }
    
    combos.insert(curr)

}

print("Answer is: ", count)
print("State is: ", banks)


