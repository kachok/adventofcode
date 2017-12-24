Imports System
Imports System.Text
Imports System.IO
Imports System.Text.RegularExpressions

Module Program
Public Function isNumeric(input As String) As Boolean
    Return Regex.IsMatch(input.Trim, "\A-{0,1}[0-9.]*\Z")
End Function

Public Function printRegisters(registers as Dictionary(of String, Long)) As String
    Dim s=""
    For Each kvp As KeyValuePair(Of String, Long) In registers
        'console.writeline("KVP item")
        Dim v1 As String = kvp.Key
        Dim v2 As Long = kvp.Value
        
        s=s+"key: "+v1+" val: "+ v2.toString +" | "
    Next
    
    'Console.WriteLine("--->"+s)

    return s
End Function

Public Function getRegister(r As String, registers as Dictionary(of String, Long)) As Long
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

            Dim freq=0
            Dim recovered=0
            Dim input As String = "set i 31,set a 1,mul p 17,jgz p p,mul a 2,add i -1,jgz i -2,add a -1,set i 127,set p 622,mul p 8505,mod p a,mul p 129749,add p 12345,mod p a,set b p,mod b 10000,snd b,add i -1,jgz i -9,jgz a 3,rcv b,jgz b -1,set f 0,set i 126,rcv a,rcv b,set p a,mul p -1,add p b,jgz p 4,snd a,set a b,jgz 1 3,snd b,set f 1,add i -1,jgz i -11,snd a,jgz f -16,jgz a -19"

            'input="set a 1,add a 2,mul a a,mod a 5,snd a,set a 0,rcv a,jgz a -1,set a 1,jgz a -2"
            Dim registers = New Dictionary(of String, Long)


            Dim strArr() As String
            strArr = input.Split(",")
    
            For count = 0 To strArr.Length - 1
                Console.WriteLine(strArr(count))
                
                Dim cmdArr() As String
                cmdArr = strArr(count).Split(" ")

                if cmdArr(0)="snd" then
                    Dim x = cmdArr(1)
                    Dim xval=x
                    if not isNumeric(x) then
                        xval=getRegister(x,registers)
                    end if

                    if xval>0 then
                        freq=xval
                    end if
                    Console.WriteLine("snd "+xval)
                else if cmdArr(0)="set" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers)
                    end if
                    registers.item(x)=yval
                    Console.WriteLine(registers.item(x))
                    

                    Console.WriteLine("set")
                else if cmdArr(0)="add" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers)
                    end if
                    registers.item(x)=getRegister(x,registers)+yval
                    Console.WriteLine("add")
                else if cmdArr(0)="mul" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers)
                    end if

                    registers.item(x)=getRegister(x,registers)*yval                    
                    Console.WriteLine("mul")
                else if cmdArr(0)="mod" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers)
                    end if
                    Console.WriteLine(getRegister(x,registers))
                    Console.WriteLine(yval)
                    Console.WriteLine(y)
                    Console.WriteLine(getRegister(y,registers))
                    
                    registers.item(x)=getRegister(x,registers) mod yval
                    Console.WriteLine("mod")
                else if cmdArr(0)="rcv" then
                    Dim x = cmdArr(1)
                    Dim xval=x
                    if not isNumeric(x) then
                        xval=getRegister(x,registers)
                    end if                    
                    if xval<>0 then
                        recovered=freq
                        exit for
                    end if
                    Console.WriteLine("rcv")
                else if cmdArr(0)="jgz" then
                    Dim x = cmdArr(1)
                    Dim y = cmdArr(2)
                    Dim xval=x
                    if not isNumeric(x) then
                        xval=getRegister(x,registers)
                    end if                    
                    Dim yval=y
                    if not isNumeric(y) then
                        yval=getRegister(y,registers)
                    end if

                    if xval>0 then
                        count=count+yval-1
                    end if
                    Console.WriteLine("jgz")
                else
                    Console.WriteLine(">"+cmdArr(0)+"<")
                
                end if

                console.writeline("count: "+count.tostring)
                Console.WriteLine(">>>"+printRegisters(registers))
                
            Next
            

        Console.Writeline("Answer is:")
        Console.Writeline(freq.tostring)

    End Sub
End Module
