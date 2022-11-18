use days::day1::*;
pub mod days;

fn main() {
    let answer = day1_solver();
    print!("Part 1: {:?}",answer.0);
    print!("\nPart 2: {:?}",answer.1);
}   
