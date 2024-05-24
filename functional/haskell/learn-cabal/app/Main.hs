module Main where
import Data.Char
import Data.Text

countNonPrintableCharactersInText :: Text -> Int
countNonPrintableCharactersInText = Data.Text.length . Data.Text.filter (not . isPrint)

countNonPrintableCharacters :: String -> Int
countNonPrintableCharacters = Prelude.length . Prelude.filter (not . isPrint)

countNonPrintableCharactersStringAndText :: String -> (Int, Int)
countNonPrintableCharactersStringAndText input = ( countNonPrintableCharacters input , countNonPrintableCharactersInText $ pack input)

main :: IO ()
main = print $ countNonPrintableCharactersStringAndText "\v\t\aHello\r\n\t\t"