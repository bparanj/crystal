module Main where

import Test.QuickCheck
import HundredDoors

prop_run :: Int -> Property
prop_run n = n > 0 ==> all (< n) xs && (null xs || maximum xs < n)
  where xs = run n

main :: IO ()
main = quickCheck prop_run
