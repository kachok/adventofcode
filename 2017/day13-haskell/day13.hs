import System.IO  
import System.Directory  
import Data.List  
import Data.List.Split 
import Control.Monad

main = do        
    handle <- openFile "day13.input" ReadMode  
    contents <- hGetContents handle 

    let arr = lines contents

    putStrLn "blah" 

    --let sum = 0

    let check n = if n == 0 then 1 else 0

    let parse i = do
        let s = splitOn ": " i
        let level=read (s!!0) :: Int
        let depth=read (s!!1) :: Int
        let count=count+1

        --print "--"
        --print level
        --print (depth * 2 - 2)
        let cycle = depth * 2 - 2
        --print ((level) `mod` (cycle))

        let val = (check ((level) `mod` (cycle)))*(level*depth)
        print val

        --putStrLn "---"


        return val

    
    results <- forM arr parse
    putStrLn "answer is: "
    print (sum results)


        