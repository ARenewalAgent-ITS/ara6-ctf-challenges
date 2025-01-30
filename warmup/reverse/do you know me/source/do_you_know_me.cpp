#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

/* 
Do you know me? 
I have alzheimer, so I often forget who I am. 
I'm very sure that the code below is a mechanism I prepared beforehand if this ever happen to me. 
But foolish enough, I made it too complicated for this goldfish brain of mine. 
Can you help me remember who I truly am? 
*/

// NOTE: WRAP FLAG ARA6{}

class ARA6 {
    private: 
        // I think this has something to do with my password
        int
            key_a = 4,
            key_b = 1,
            key_c = 7,
            key_d = 2,
            key_e = 5;

        // what is this gibberish?
        string
            obfuscated1 = "O`OD",
            obfuscated2 = "bv?Cm",
            obfuscated3 = "?Cm",
            obfuscated4 = "ev>m",
            obfuscated5 = "?mB{";
    
    public: 
        // I think this shifts characters of a string by [key] much
        string rotate_or_shift(string *input, int key) {
            string result = *input;
            for (int i = 0; i < (*input).length(); ++i) {
                result[i] = ((*input)[i] + key) % 256;
            }
            return result;
        }

        void group_rotate_or_shift(string *input1, string *input2, string *input3, string *input4, string *input5, int key) {
            *input1 = rotate_or_shift(input1, key);
            *input2 = rotate_or_shift(input2, key);
            *input3 = rotate_or_shift(input3, key);
            *input4 = rotate_or_shift(input4, key);
            *input5 = rotate_or_shift(input5, key);
        }

        // bypass my own password?
        void password_check () {
            string password;
            cout << "Enter password: ";
            cin >> password;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            if (password == "\x6D\x79\x50\x34\x35\x35\x77\x30\x72\x64") {
                summation(key_a, key_b, key_c, key_d, key_e);
            } else if (password == "\x72\x33\x34\x6C\x50\x34\x35\x35\x77\x30\x72\x64\x3F") {
                summation(key_e, key_d, key_c, key_b, key_a);
            } else if (password == "\x6d\x59\x31\x64\x33\x6e\x74\x31\x66\x31\x33\x72") {
                summation(key_a, key_d, key_c, key_b, key_e);
            } else if (password == "\x74\x68\x31\x73\x31\x73\x54\x68\x33\x43\x30\x72\x72\x33\x63\x74\x50\x34\x35\x35\x77\x30\x72\x64") {
                summation(key_c, key_d, key_e, key_b, key_a);
            } else {
                cout << "For the one who managed to find the right path, shall know who I truly am." << endl;
                password_check();
            }
        }
        
        int summation (int a, int b, int c, int d, int e) {
            int temp = d;
            a += c;
            b += e; 
            d = a;
            a -= e; 
            temp = c;
            c -= e;
            return  (a / b + c * d - e);
        }

        // wait... why does this function do not work?
        /* void pass_check(int pass) {
            if (pass == (((40c + 30d - 10b + 21a - 5e)-7c-5d)/2e) ) {
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, ((500a + 200b + 100c + 50d + 20e -200e) /10d) );
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, (20b -70c +300a / 50 e -100c));
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, (50c + 100d - 200e + 10b - 5a));
                return;
            } else if (pass == ((((10a + 12b + 15c + 17d + 200e - b)/d)/e)-(d-b)-(10d + 16e)) ) {
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, (-20a + 50b + 100c - 200d + 500e) );
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, (-70b + 100c + 200d - 500e + 10a) );
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, (-100c + 200d - 500e + 10a + 50b) );
                return;
            } else if (pass == ((1000b + 5000a / 200e) * 0a + (200c -100a) / 50d - b) ) {
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, (-20a + 50b + 100c - 200d + 500e) );
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, (-50a + 100b - 200c + 500d - 100e) );
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, 20a /10b + 5c - 10d + 20e);
                return;
            } else if (pass == (18a + 15b + 12c + 9d + 6e - 500b + 50a +14c)) {
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, ((400a + 200b + 100c + 50d - 1000e) /100d) +2e);
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, ((150c + 100d - 200e + 10b - 5a) / 5d) / (-a) - b);
                group_rotate_or_shift(obfuscated1, obfuscated2, obfuscated3, obfuscated4, obfuscated5, (50c + 100d - 200e + 10b - 5a) / 5d + 8e + a - 3b);
            } else {
                cout << "Man, y\'ll be tripin\'" << endl;
            }
        } */


};

int main() {
    ARA6 ctf; 
    ctf.password_check();
    ctf.pass_check(); 

    // wait... i think this program works no longer

    return 0;
}