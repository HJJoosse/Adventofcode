module Y2019.Day2 where

import System.IO

fuelAdder :: Integer -> Integer
fuelAdder x = div x 3 - 2

totalFuel :: Integer -> Integer 
totalFuel x 
    | fuelToadd <= 0    = 0
    | otherwise         = fuelToadd + totalFuel fuelToadd
    where fuelToadd = fuelAdder x

solvePart1 :: [Integer] -> Integer
solvePart1 = sum . map fuelAdder

solvePart2 :: [Integer] -> Integer 
solvePart2 = sum . map totalFuel

day1solver :: String -> IO ()
day1solver fileName = do
    inputLines <- readFile fileName
    let inputList = lines inputLines
    let masses = map read inputList :: [Integer]
    print (solvePart1 masses)
    print (solvePart2 masses)
