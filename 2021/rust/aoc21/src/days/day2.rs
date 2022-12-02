use crate::days::tools::*;

const INPUT: &str = "/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d2.txt";

pub fn day2_solver() -> (i32,i32) {
    let input_data: Vec<String> = input_reader(INPUT);
    let input_clean: Vec<String> = input_data.iter()
                                    .filter(|s| !s.is_empty())
                                    .map(|s| s.to_string())
                                    .collect();
    let a1 = part1(&input_clean);
    let a2 = part2(&input_clean);
    return (a1, a2)
}

fn part1(input: &Vec<String>) -> i32 {
    let mut post: [i32; 2] = [0,0];
    for s in input {
        let i: Vec<&str> = s.trim()
        .split_whitespace()
        .collect();
        let dist: i32 = i[1].parse().unwrap();
        if i[0] == "forward" {
            post[0] += dist;
        
        } else if i[0] == "up" {
            post[1] -= dist;
        } else {
            post[1] += dist;
        }
    }
    return post[0]*post[1]
}

fn part2(input: &Vec<String>) -> i32 {
    let mut post: [i32; 3] = [0,0,0];
    for s in input {
        let i: Vec<&str> = s.trim()
        .split_whitespace()
        .collect();
        let dist: i32 = i[1].parse().unwrap();
        if i[0] == "forward" {
            post[0] += dist;
            post[1] += dist*post[2]
        
        } else if i[0] == "up" {
            post[2] -= dist;
        } else {
            post[2] += dist;
        }
    }
    return post[0]*post[1]
}