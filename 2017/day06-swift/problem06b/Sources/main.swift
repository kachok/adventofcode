
// Using final state from output of problem06 part 1
var banks: [Int] = [14, 13, 12, 11, 9, 8, 8, 6, 6, 4, 4, 3, 1, 1, 0, 12]

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


