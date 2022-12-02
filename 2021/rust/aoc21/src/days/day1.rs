use crate::days::tools::*;

const INPUT: &str = "../../data/input_d1.txt";


pub fn day1_solver() -> (i32,i32) {
    let data: Vec<String> = input_reader(INPUT);
    let data_int: Vec<i32> = string_to_int(data);
    let p1: i32 = part1(&data_int);
    let p2: i32 = part2(&data_int);
    return (p1,p2);
}

fn part1(int_vec: &Vec<i32>) -> i32 {
    let mut answer = 0;
    for i in 0..int_vec.len()-1 {
        if int_vec[i] <= int_vec[i+1] {
            answer += 1;
        }
    }
    return answer;
}

fn part2(int_vec: &Vec<i32>) -> i32 {
    let mut answer = 0;
    for i in 0..int_vec.len()-3 {
		if int_vec[i..i+3].iter().sum::<i32>() < int_vec[i+1..i+4].iter().sum::<i32>() {
			answer += 1;
		}
	}
	return answer;
}