use std::fs;


pub fn day1_solver() -> (i32,i32) {
    let a1: i32 = part1();
    let a2: i32 = part2();

    return (a1,a2)
}

fn part1() -> i32 {
    let input = fs::read_to_string("../../data/input_d1.txt").expect("no such file");
    let input_split: Vec<Vec<&str>> = input.split("\n\n")
                    .map(|x| x.split("\n").collect())
                    .collect();
    let mut highest: i32 = 0;
    for elf in input_split {
        let elf_int: Vec<i32> = elf.iter()
                                .map(|y| y.parse().unwrap())
                                .collect();
        let elf_sum: i32 = elf_int.iter().sum();
        if elf_sum > highest {
            highest = elf_sum;
        }
    }
    return highest
}

fn part2() -> i32 {
    let input = fs::read_to_string("../../data/input_d1.txt").expect("no such file");
    let input_split: Vec<Vec<&str>> = input.split("\n\n")
                    .map(|x| x.split("\n").collect())
                    .collect();
    let mut highest_three: Vec<i32> = vec![0,0,0];
    for elf in input_split {
        let elf_int: Vec<i32> = elf.iter()
                                .map(|y| y.parse().unwrap())
                                .collect();
        let elf_sum: i32 = elf_int.iter().sum();
        if elf_sum > highest_three[0] {
            highest_three[0] = elf_sum;
            highest_three.sort();
        }
    }
    return highest_three.iter().sum()
}