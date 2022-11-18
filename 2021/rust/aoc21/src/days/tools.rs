use std::fs;

pub fn input_reader(data_file: &str) -> Vec<String> {
    let contents = fs::read_to_string(data_file).expect("no such file");
    let contents_new: Vec<String> = contents.split("\n").map(|s| s.to_string()).collect();
    
    return contents_new
}

pub fn string_to_int(data_str: Vec<String>) -> Vec<i32> {
    let data_int: Vec<i32> = data_str.iter()    // (1) Make iter
    .map(|s| s.trim())                          // (2) Trim the string
    .filter(|s| !s.is_empty())                  // (3) remove empty
    .map(|s| s.parse().unwrap())                // (4) parse for integer 
    .collect();                       
    return data_int
}

