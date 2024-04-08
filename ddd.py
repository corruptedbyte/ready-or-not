#include <iostream>
#include <string>
#include <fstream>
#include <ctime>

using namespace std;

enum commands {
    EXIT = 0,
    WRITE = 1,
    TRUNCATE = 2
};

struct diaryLog {
    string filename;
    string header;
    int mood;
};

void addSentence(ofstream& Diary, diaryLog& log) {
    Diary.open(log.filename, ios::app);
    string input;
    cout << "Diary > ";
    cin.ignore(1);
    getline(cin, input);

    cout << endl;

    Diary << input;
    Diary << "\n";

    Diary.close();
}

int main() {

    diaryLog log;
    cout << "Log name (*.*): ";
    cin >> log.filename;
    cout << endl;

    cout << "Enter your mood (0/10): ";
    cin >> log.mood;
    cout << endl;

    ofstream Diary;

    time_t now;
    char* dt;


    cout << "What's the header for today's log > ";

    cin.ignore(1);
    getline(cin, log.header);

    cout << endl;

    Diary.open(log.filename, ios::app);

    now = time(0);
    dt = ctime(&now);
    Diary << dt;

    Diary << endl << "Log: " << log.header << endl;
    Diary << "Mood: " << log.mood << "/10" << endl << endl;

    Diary.close();

    int option = 0;
    bool active = true;
    cout << "===============================================" << endl;
    cout << "1 - Add a new sentence" << endl << "2 - Erase the log" << endl << "0 - Exit" << endl;
    cout << "===============================================" << endl << endl;

    while (active) {
        cout << "Your option: ";
        cin >> option;
        cout << endl;
        switch (option) {
            case EXIT: {
                active = false;
                break;
            }

            case WRITE: {
                addSentence(Diary, log);
                break;
            }

            case TRUNCATE: {
                Diary.open(log.filename, ios::trunc);
                Diary.close();
                break;
            }

            default: {
                cout << "Unknown command!";
            }
        }
    }
}
