import qualified Data.Text as T
import qualified Data.Text.IO as TIO

day3solver :: FilePath -> IO ()
day3solver fileName = do
    inputLines <- readFile fileName
    let inputList = lines inputLines
    
    print inputList


