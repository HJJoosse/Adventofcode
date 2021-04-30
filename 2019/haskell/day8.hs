import qualified Data.Text as T


batchsize :: Int 
batchsize = 25*6

getLayer :: [Int] -> [Int]
getLayer inList = take batchsize inList

getRest :: [Int] -> [Int]
getRest pxs = drop batchsize pxs

isLessZeros :: Int -> Int -> Bool 
isLessZeros a b
    | a < b = True
    | otherwise = False 

calculateProduct :: Int -> Int -> Int -> Bool -> Int
calculateProduct one two prod check
    | check = one*two
    | otherwise = prod

changeZeros :: Int -> Int -> Bool -> Int 
changeZeros zeros leastZeros check
    | check = zeros
    | otherwise = leastZeros

calculateLeastZeros :: [Int] -> Int -> Int -> Int
calculateLeastZeros pixels leastAmountZeros productOnesTwos
    | null $ getRest pixels = productOnesTwos
    | otherwise  = calculateLeastZeros (getRest pixels) leastAmountZeros productOnesTwos
    where 
        layer = getLayer pixels
        ones = length [x | x <- layer, x == 1]
        twos = length [x | x <- layer, x == 2]
        zeros = length [x | x <- layer, x == 0]
        isLess = isLessZeros zeros leastAmountZeros
        leastAmountZeros = changeZeros zeros leastAmountZeros isLess
        productOnesTwos = calculateProduct ones twos productOnesTwos isLess

day8solver :: FilePath -> IO ()
day8solver fileName = do
    inputLines <- readFile fileName
    let contentText = T.pack inputLines
    let inputValues = T.split (==',') contentText
    let inputs = Prelude.map (read . T.unpack) inputValues :: [Int]
    print $ calculateLeastZeros inputs batchsize 0
