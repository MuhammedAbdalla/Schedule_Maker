/*

 Copyright Muhammed Abdalla 2021 
 muhabda@bu.edu muhabdalla718@gmail.com

*/
#include <iostream>
#include <fstream>
#include <string>
#include <string_view>
#include <vector>
#include <map>
#include "classes.h"

using namespace std;

string isClassValid(string name) {
    string departments[4] = {"BE", "EC", "EK", "ME"};
    if (name.size() != 5) 
        return "-1"; 
    string department = name.substr(0,2);

    bool found = false;
    for (string d : departments)
        if (d == department)
            found = true;     

    if (!found) 
        return "-1";

    string course_num = name.substr(2);
    try {
        stoi(course_num);
    } catch(exception e) {
        cout << "course number not valid\n";
        return "-1";
    }
    return ("ENG " + department + " " + course_num);
}

int main() {
    vector<string> courses;
    string line, input;

    cout << "Enter your courses (Ex. BE209) \'q\' to submit: \n";
    cout << "Course 1: ";

    while(getline(cin, input)) {
        if (input == "q" or input == "Q")
            break;
        string out = isClassValid(input);
        if (out != "-1")
            courses.push_back(out);
        else
            cout << input << " is not a valid eng course\n";
        cout << "Course " << courses.size()+1 << ": ";
    }
    cout << "N/A" << endl;
    cout << "You have entered " << courses.size() << " classes" << endl;

    ifstream file;
    ofstream ofile;
    vector <string> approved_courses;
    file.open("courses.txt");
    while (getline(file, line)) {
        for (string c : courses) {
            int pos = line.find(":");
            if (c == line.substr(0,pos))
               approved_courses.push_back(line);
        }
    }
    file.close();
    ofile.open("courses.txt");
    for (string a_c : approved_courses)
        ofile.write(a_c.c_str(), a_c.size()).write("\n",1);
    ofile.close();
}