module Main where

reverseList :: [a] -> [a]
reverseList = foldr (\x acc -> acc ++ [x]) []

main :: IO ()
main = print $ reverseList [1,2,3,4,5,6,7]
