using System;
 
public class HelloWorld
{
    static public void Main ()
    {
        int last=50000000;
        int[] buff = new int[last+1];
        int[] nums = new int[last+1];
        int curr = 0;
        int step= 363;
        buff[0]=0;
        nums[0]=0;

        int answer=0;

        for (int i=1; i<=last;i++){
            if (i % 1000000 ==0) {
                Console.WriteLine ("i: "+ i);
            }

            for (int j=0; j<step;j++){
                curr=nums[curr];
            }

            buff[i]=i;            
            nums[i]=nums[curr];
            nums[curr]=i;
            curr=i;
        }

        answer=buff[nums[0]];
        Console.WriteLine ("answer is: ");
        Console.WriteLine (answer);

        
    }
}