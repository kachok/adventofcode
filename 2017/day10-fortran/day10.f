        program day10
            integer :: input(16)

            integer :: array(256)
            integer :: curr, length, skipsize

            input=(/94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243/)


            curr=1
            skipsize=0
            !print *, "Hello World!"

            ! initialize circular list (aka array)
            do i = 1 , 256
                array ( i ) = i-1
                
            end do

            ! loop thru input
            do i = 1 , 16
                length=input(i)

                print *, array
                print *, " length ", length
                print *, " curr ", curr
                print *, " skipsize ", skipsize

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
                if (curr>256) then
                    curr=curr-256
                end if

                ! increment skip at the end of each loop
                skipsize=skipsize+1

                print *, " "
            end do


            print *, array

            print *, "answer: ", array(1)*array(2)
        end program day10
