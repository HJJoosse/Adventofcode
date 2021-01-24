import qualified Data.Text      as T
import qualified Data.Text.IO   as TIO

import Data.Maybe               (isNothing)

upDatecoord :: T.Text -> [Int]
upDatecoord dir
    | fst dirSplit == T.pack "L"    = [-dist,0]
    | fst dirSplit == T.pack "R"    = [dist,0]
    | fst dirSplit == T.pack "U"    = [0,dist]
    | otherwise                     = [0,-dist]
    where 
        dirSplit = T.splitAt 1 dir
        dist = read . T.unpack $ snd dirSplit 

getMovements :: [T.Text] -> [[Int]]
getMovements inList = do
    map upDatecoord inList

trackCoords :: [[Int]] -> [[Int]] -> [[Int]]
trackCoords movList startPoint = do
    let moves = head movList
    let movListnew = tail movList
    let newPos = zipWith (+) (last startPoint) moves
    let startPoint = startPoint++[newPos]
    if null [movListnew]
        then
            startPoint
        else
            trackCoords movListnew startPoint

day3solver :: FilePath -> IO ()
day3solver fileName = do
    inputLines <- readFile fileName
    let inputList = map T.pack $ lines inputLines
    let inputDirs = map (T.splitOn (T.pack ",")) inputList
    let movsA = getMovements . head $ inputDirs
    let movsB = getMovements . last $ inputDirs
    print (trackCoords movsA [[0,0]])
