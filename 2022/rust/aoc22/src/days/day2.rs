use std::fs;

pub fn day2_solver() -> (i32,i32) {
    let a1: i32 = part1();
    let a2: i32 = part2();

    return (a1,a2)
}

fn part1() -> i32 {
    let Ok(lines) = read_lines("../../data/input_d1.txt");
}

fn part2() -> i32 {
    return 0
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}