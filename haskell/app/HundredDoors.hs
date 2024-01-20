module App.HundredDoors where

run :: Int -> [Int]
run n = takeWhile (< n) [k*k | k <- [1..]]
