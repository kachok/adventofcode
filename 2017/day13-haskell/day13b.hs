import System.IO  
import System.Directory  
import Data.List  
import Data.List.Split 
import Control.Monad


main = do        
    handle <- openFile "day13.input" ReadMode  
    contents <- hGetContents handle 

    let arr = lines contents

    print arr

    putStrLn "blah" 

    let answer delay = do

        let check n = if n == 0 then 1 else 0

        let parse i = do
            let s = splitOn ": " i
            let level=read (s!!0) :: Int
            let depth=read (s!!1) :: Int
            let cycle = depth * 2 - 2
            let val = (check ((level+delay) `mod` (cycle)))

            return val

        results <- forM arr parse
        --print results
        if (sum results) == 0 then print delay else return ()

    putStrLn "answer is: "
    forM_ [3897600..3897700] $ \i -> do
        --print ">>>>>>"
        --print i
        answer i
        --print (answer i)    

-- 3897604
