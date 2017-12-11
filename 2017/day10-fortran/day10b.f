        program day10
            integer :: input2(55)

            integer :: answer(16)

            integer :: array(256)
            integer :: curr, length, skipsize
            character(50) :: input
            character :: ch

            input="94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243"
            !convert input to ascii and add tail
            do i = 1 , 50
                input2(i) = iachar(input(i:i))
            end do            
            input2(51)=17
            input2(52)=31
            input2(53)=73
            input2(54)=47
            input2(55)=23

            curr=1
            skipsize=0
            !print *, "Hello World!"

            ! initialize circular list (aka array)
            do i = 1 , 256
                array ( i ) = i-1
                
            end do

            !do it 64 times
            do k=1, 64

                ! loop thru input
                do i = 1 , 55
                    length=input2(i)

                    !print *, array
                    !print *, " length ", length
                    !print *, " curr ", curr
                    !print *, " skipsize ", skipsize

                    do j=1, length/2
                        j1=curr+j-1
                        if (j1>256) then
                            j1=j1-256
                        end if

                        j2=curr+length-j
                        if (j2>256) then
                            j2=j2-256
                        end if

                        a=array(j1)
                        b=array(j2)
                        array(j1)=b
                        array(j2)=a
                    end do

                    ! move current position by length
                    curr=curr+length+skipsize
                    do while (curr>256)
                        curr=curr-256
                    end do

                    ! increment skip at the end of each loop
                    skipsize=skipsize+1

                    !print *, " "
                end do

            end do

            print *, array

            print *, "answer: ", array(1)*array(2)


            do i=1,16
                answer(i)=array(i*16-15)
                print *, ">>i ",i
                print *, ">>i*16-15 ", i*16-15

                do i2=2,16
                    answer(i)=xor(answer(i),array(i*16-15+i2-1))
                    print *, ">>i*16-15+i2-1 ",i*16-15+i2-1

                end do

                print *, "----"
            end do



            print *, "answer: ", answer
        end program day10

        !use https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html
        !and https://convertcase.net/ for formatting output