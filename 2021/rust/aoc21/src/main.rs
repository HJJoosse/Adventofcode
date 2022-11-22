use days::day2::*;
pub mod days;

fn main() {
    let answer: (i32,i32) = day2_solver();
    print!("Part 1: {}",answer.0);
    print!("\nPart 2: {:?}",answer.1);
}   
