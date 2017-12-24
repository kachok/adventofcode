Imports System
Imports System.Text
Imports System.IO
Imports System.Text.RegularExpressions

Module Program
Public Function isNumeric(input As String) As Boolean
    Return Regex.IsMatch(input.Trim, "\A-{0,1}[0-9.]*\Z")
End Function

Public Function printRegisters(registers as Dictionary(of String, Decimal)) As String
    Dim s=""
    For Each kvp As KeyValuePair(Of String, Decimal) In registers
        'console.writeline("KVP item")
        Dim v1 As String = kvp.Key
        Dim v2 As Decimal = kvp.Value
        
        s=s+"key: "+v1+" val: "+ v2.toString +" | "
    Next
    
    'Console.WriteLine("--->"+s)

    return s
End Function

Public Function getRegister(r As String, registers as Dictionary(of String, Decimal)) As Decimal
    'console.writeline("|"+r+"|")
    if not registers.ContainsKey(r) then
        'console.writeline(">> value of "+r+" = "+"0")
        return 0
    else
        'console.writeline(">> value of "+r+" = "+registers.Item(r).toString())
        return registers.Item(r)
    end if    
    
End Function

    Sub Main(args As String())

            Dim answer=0 
            Dim freq=0
            Dim recovered=0
            Dim input As String = "set i 31,set a 1,mul p 17,jgz p p,mul a 2,add i -1,jgz i -2,add a -1,set i 127,set p 622,mul p 8505,mod p a,mul p 129749,add p 12345,mod p a,set b p,mod b 10000,snd b,add i -1,jgz i -9,jgz a 3,rcv b,jgz b -1,set f 0,set i 126,rcv a,rcv b,set p a,mul p -1,add p b,jgz p 4,snd a,set a b,jgz 1 3,snd b,set f 1,add i -1,jgz i -11,snd a,jgz f -16,jgz a -19"

            'input="set a 1,add a 2,mul a a,mod a 5,snd a,set a 0,rcv a,jgz a -1,set a 1,jgz a -2"
            'input="snd 1,snd 2,snd p,rcv a,rcv b,rcv c,rcv d"
            Dim registers = {New Dictionary(of String, Decimal),New Dictionary(of String, Decimal)}

            Dim pos = {0,0}

            Dim st = {New Queue(of Decimal),New Queue(of Decimal)}
            Dim state = {"begin", "begin"}

            Dim strArr() As String
            strArr = input.Split(",")

            Dim curr=0

            registers(0).item("p")=0
            registers(1).item("p")=1

            While True
                Dim count=pos(curr)

                Console.WriteLine("-------------")
                'Console.WriteLine("curr: "+curr.tostring)
                'Console.WriteLine("count: "+count.tostring)
                Console.WriteLine("cmd: "+strArr(count)+" curr: "+curr.tostring)
            
                if pos(curr)<0 or pos(curr)>40 then
                    console.writeline("OVERFFLOW")
                    Exit While
                end if

                    Console.writeline(state(0)+" "+state(1)+" "+st(0).count.tostring+" "+st(1).count.tostring)
                    Console.WriteLine(">>>"+printRegisters(registers(0)))
                    Console.WriteLine(">>>"+printRegisters(registers(1)))

                if state(0)="wait" and state(1)="wait"  then
                    Console.writeline(state(0)+" "+state(1)+" "+st(0).count.tostring+" "+st(1).count.tostring)
                    Console.WriteLine(">>>"+printRegisters(registers(0)))
                    Console.WriteLine(">>>"+printRegisters(registers(1)))
                end if

                if state(0)="wait" and state(1)="wait" and st(0).count=0 and st(1).count=0 then
                    console.writeline("EXIT 1!")
                    Exit While
                end if

                'Console.writeline(state(0)+" "+state(1)+" "+st(0).count.tostring+" "+st(1).count.tostring)

                'Console.WriteLine("curr: "+curr.tostring)
                'Console.WriteLine("count: "+count.tostring)
                'Console.WriteLine("cmd: "+strArr(count))
                
                Dim cmdArr() As String
                cmdArr = strArr(count).Split(" ")

                if cmdArr(0)="snd" then
                    Dim x = cmdArr(1)
                    Dim xval=x

                    if not isNumeric(x) then
                        xval=getRegister(x,registers(curr))
                    end if

                    if curr=1 then
                        answer=answer+1
                    end if
                    st( (curr+1) mod 2).Enqueue(xval)

                    'state( (curr+1) mod 2)="not wait"
                    pos(curr)=pos(curr)+1                        
                else if cmdArr(0)="set" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers(curr))
                    end if
                    registers(curr).item(x)=yval
                    'Console.WriteLine(registers(curr).item(x))
                    

                    'Console.WriteLine("set")
                    
                    pos(curr)=pos(curr)+1                        
                else if cmdArr(0)="add" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim yval as Decimal
                    if not isNumeric(y) then
                        yval =getRegister(y,registers(curr))
                    else
                        yval=y
                    end if
                    registers(curr).item(x)=getRegister(x,registers(curr))+yval
                    'Console.WriteLine("add")
                    
                    pos(curr)=pos(curr)+1                        

                else if cmdArr(0)="mul" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers(curr))
                    end if

                    registers(curr).item(x)=getRegister(x,registers(curr))*yval                    
                    'Console.WriteLine("mul")
                    
                    pos(curr)=pos(curr)+1                        

                else if cmdArr(0)="mod" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers(curr))
                    end if                        
                    registers(curr).item(x)=getRegister(x,registers(curr)) mod yval
                    pos(curr)=pos(curr)+1                        
                else if cmdArr(0)="rcv" then
                    if st(curr).count=0 then
                        state(curr)="wait"
                        curr=(curr+1) mod 2
                    else
                        state(curr)="not wait"
                        Dim x = cmdArr(1)
                        registers(curr).item(x)=st(curr).Dequeue()
                        pos(curr)=pos(curr)+1                        
                    end if
                else if cmdArr(0)="jgz" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim xval=x
                    if not isNumeric(x) then
                        xval=getRegister(x,registers(curr))
                    end if                    
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers(curr))
                    end if

                    if xval>0 then
                        pos(curr)=pos(curr)+yval
                    else
                        pos(curr)=pos(curr)+1                        
                    end if
                else
                    Console.WriteLine(">"+cmdArr(0)+"<")
                
                end if
            End While 
            

        Console.Writeline("Answer is:")
        Console.Writeline(answer.tostring)

    End Sub
End Module
