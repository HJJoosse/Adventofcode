import Data.List as L

startPoint ::  Integer
startPoint = 172851

endPoint :: Integer
endPoint = 675869

isIncrementing :: String -> Bool 
isIncrementing input
    | input == L.sort input = True
    | otherwise             = False

hasDouble :: String -> Int -> Bool 
hasDouble input ix
    | ix          == length input -1    = False 
    | input !! ix == input !! (ix + 1)  = True 
    | otherwise                         = hasDouble input (ix+1)

mapInput :: String  -> [(Char,Int)]
mapInput input = zip uniqueVals $ map (\x -> length (filter (==x) input)) uniqueVals
    where uniqueVals = [x| x<-['1'..'9'], x `elem` input]

hasValiddouble :: String -> Bool
hasValiddouble input
    | not $ null [True|x<- mapInput input, snd x == 2]  = True 
    | otherwise                                         = False

main :: IO ()
main = do
    let incrementingPasses = [x|x <- [startPoint..endPoint], isIncrementing $ show x]
    print $ length [x|x<- incrementingPasses, hasDouble (show x) 0]
    print $ length [x|x<- incrementingPasses, hasValiddouble (show x)]
