#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

stringstream test("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green");
// stringstream test2("two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen");


int part1(vector<string> input_list){
    for (string s : input_list) {
        string game_id = s.substr(0,s.find(":"));
        cout << game_id << endl;
        string combinations = s.substr(s.find(":")+1,s.length());
               
        cout << combinations << endl;
    }
    return 0;
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
        myfile.open("../data/input_d2.txt",ios::in);
        if (myfile.is_open()){ //checking whether the file is open
            string tp;
            while(getline(myfile, tp)){ //read data from file object and put it into string.
                input_list.push_back(tp); //print the data of the string
            }
            myfile.close(); //close the file object.
        }
    }

    int answer = part1(input_list);
    // int answer2 = part2(input_list);
    cout << answer << endl;
}

