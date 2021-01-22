module Y2019.Day2 where

import qualified Data.Text as T
import qualified Data.Map.Strict as M

addOrmult :: Int -> Int  -> Int  -> Int 
addOrmult 1 = (+)
addOrmult 2 = (*)
addOrmult _ = (-)

returnInt :: Int -> M.Map Int Int -> Int
returnInt ix mapList = do
    let tuplInterest = M.toList mapList !! ix
    snd tuplInterest 

part1Solver :: Int -> M.Map Int Int -> M.Map Int Int
part1Solver ix inList
    | ixVal `elem` [1,2]    = part1Solver (ix+4) $ M.insert posC inVal inList 
    | otherwise             = inList
    where 
        ixVal = returnInt ix inList
        valA = returnInt (returnInt (ix+1) inList) inList
        valB = returnInt (returnInt (ix+2) inList) inList
        posC = returnInt (ix+3) inList
        op = addOrmult ixVal
        inVal = op valA valB
        


day2solver :: String -> IO ()
day2solver fileName = do
    contents <-  readFile fileName
    let contentText = T.pack contents
    let inputValues = T.split (==',') contentText
    let inputs = Prelude.map (read . T.unpack) inputValues :: [Int]
    let initList = M.insert 2 2 $ M.insert 1 12 $ M.fromList $ zip [0..] inputs
    print $ snd . head . M.toList . part1Solver 0 $ initList