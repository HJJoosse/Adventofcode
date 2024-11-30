// day 1 of adventofcode
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

stringstream test("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet");
stringstream test2("two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen");

int part1(vector<string> input_list){
    int sum = 0;
    for (string s : input_list) {
        vector<char> sum_vec;
        for (char c: s) {
            if (isdigit(c)) {
                sum_vec.push_back(c);
            }
            
        }
        int sum_line = (sum_vec[0]-'0')*10 + (sum_vec[sum_vec.size()-1]-'0');
        sum += sum_line;
    }
    return sum;
}

int string_to_int(string ){
    
}

int part2(vector<string> input_list){
    int sum = 0;
    for (string s: input_list)


    return sum
}

int main() {
    char test_real[] = "test or input?\n";
    char answer1[5];
    cout << test_real;
    cin >> answer1;
    vector<string> input_list;
    if (strcmp(answer1,"test") == 0) {
        string s;
        while(getline(::test, s)){
            input_list.push_back(s);
        }
    }
    else{
        fstream myfile;
        myfile.open("../data/input_d1.txt",ios::in);
        if (myfile.is_open()){ //checking whether the file is open
            string tp;
            while(getline(myfile, tp)){ //read data from file object and put it into string.
                input_list.push_back(tp); //print the data of the string
            }
            myfile.close(); //close the file object.
        }
    }

    int answer = part1(input_list);
    int answer2 = part2(input_list);
    cout << answer << endl;
}

