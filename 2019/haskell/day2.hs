import qualified Data.Text as T

part1solver :: [Integer] -> Integer 
part1solver inputs
    | x == 1 = take 3 inputs
    | x == 2 = take 3 inputs
    | otherwise  = fst newList
    where x = fst inputs

day2solver :: String -> IO ()
day2solver fileName = do
    contents <-  readFile fileName
    let contentText = T.pack contents
    let inputValues = T.split (==',') contentText
    let inputs = map (read . T.unpack) inputValues :: [Integer]
    print inputs