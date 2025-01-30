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
                cout << "Ini hasil summation: " << summation(key_a, key_b, key_c, key_d, key_e);
            } else if (password == "\x72\x33\x34\x6C\x50\x34\x35\x35\x77\x30\x72\x64\x3F") {
                cout << "Ini hasil summation: " << summation(key_e, key_d, key_c, key_b, key_a);
            } else if (password == "\x6d\x59\x31\x64\x33\x6e\x74\x31\x66\x31\x33\x72") {
                cout << "Ini hasil summation: " << summation(key_a, key_d, key_c, key_b, key_e);
            } else if (password == "\x74\x68\x31\x73\x31\x73\x54\x68\x33\x43\x30\x72\x72\x33\x63\x74\x50\x34\x35\x35\x77\x30\x72\x64") {
                cout << "Ini hasil summation: " << summation(key_c, key_d, key_e, key_b, key_a);
            } else {
                cout << "For the one who manage to find the right path, shall know who I truly am." << endl;
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
        void pass_check(int pass) {
            string 
                temp1 = obfuscated1,
                temp2 = obfuscated2,
                temp3 = obfuscated3,
                temp4 = obfuscated4,
                temp5 = obfuscated5;
            if (pass == ((((40*key_c) + (30*key_d) - (10*key_b) + (21*key_a) - (5*key_e))-(7*key_c)-(5*key_d))/(2*key_e)) ) {
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (((500*key_a) + (200*key_b) + (100*key_c) + (50*key_d) + (20*key_e) -(200*key_e)) /(10*key_d)) );
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, ((20*key_b) -(70*key_c) +(300*key_a) / (50*key_e) -(100*key_c)));
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, ((50*key_c) + (100*key_d) - (200*key_e) + (10*key_b) - (5*key_a)));
                cout << temp1 << temp2 << temp3 << temp4 << temp5 << endl;
                return;
            } else if (pass == (((((10*key_a) + (12*key_b) + (15*key_c) + (17*key_d) + (200*key_e) - key_b)/key_d)/key_e)-(key_d-key_b)-((10*key_d) + (16*key_e))) ) {
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (-(20*key_a) + (50*key_b) + (100*key_c) - (200*key_d) + (500*key_e)) );
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (-(70*key_b) + (100*key_c) + (200*key_d) - (500*key_e) + (10*key_a)) );
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (-(100*key_c) + (200*key_d) - (500*key_e) + (10*key_a) + (50*key_b)) );
                cout << temp1 << temp2 << temp3 << temp4 << temp5 << endl;
                return;
            } else if (pass == (((1000*key_b) + (5000*key_a) / (200*key_e)) * (0*key_a) + ((200*key_c) -(100*key_a)) / (50*key_d) - key_b) ) {
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (-(20*key_a) + (50*key_b) + (100*key_c) - (200*key_d) + (500*key_e)) );
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (-(50*key_a) + (100*key_b) - (200*key_c) + (500*key_d) - (100*key_e)) );
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (20*key_a) /(10*key_b) + (5*key_c) - (10*key_d) + (20*key_e));
                cout << temp1 << temp2 << temp3 << temp4 << temp5 << endl;
                return;
            } else if (pass == ((18*key_a) + (15*key_b) + (12*key_c) + (9*key_d) + (6*key_e) - (500*key_b) + (50*key_a) +(14*key_c))) {
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (((400*key_a) + (200*key_b) + (100*key_c) + (50*key_d) - (1000*key_e)) /(100*key_d)) +(2*key_e));
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, (((150*key_c) + (100*key_d) - (200*key_e) + (10*key_b) - (5*key_a)) / (5*key_d)) / (-key_a) - key_b);
                group_rotate_or_shift(&temp1, &temp2, &temp3, &temp4, &temp5, ((50*key_c) + (100*key_d) - (200*key_e) + (10*key_b) - (5*key_a)) / (5*key_d) + (8*key_e) + key_a - (3*key_b));
                cout << temp1 << temp2 << temp3 << temp4 << temp5 << endl;
            } else {
                cout << "Man, y\'ll be tripin\'" << endl;
            }
        }

        // all of the getter functions
        int get_key_a() { return key_a; }
        int get_key_b() { return key_b; }
        int get_key_c() { return key_c; }
        int get_key_d() { return key_d; }
        int get_key_e() { return key_e; }
        string get_obfuscated1() { return obfuscated1; }
        string get_obfuscated2() { return obfuscated2; }
        string get_obfuscated3() { return obfuscated3; }
        string get_obfuscated4() { return obfuscated4; }
        string get_obfuscated5() { return obfuscated5; }
};

int main() {
    ARA6 ctf; 
    // check all the summation results by either bypassing every  password check using the below function
    ctf.password_check();
    cout << endl;

    // OR by just printing out all the results for the summation function after bypassing the password check using the below method
    cout << "Ini hasil summation1: " << ctf.summation(ctf.get_key_a(), ctf.get_key_b(), ctf.get_key_c(), ctf.get_key_d(), ctf.get_key_e()) << endl;
    cout << "Ini hasil summation2: " << ctf.summation(ctf.get_key_e(), ctf.get_key_d(), ctf.get_key_c(), ctf.get_key_b(), ctf.get_key_a()) << endl;
    cout << "Ini hasil summation3: " << ctf.summation(ctf.get_key_a(), ctf.get_key_d(), ctf.get_key_c(), ctf.get_key_b(), ctf.get_key_e()) << endl;
    cout << "Ini hasil summation4: " << ctf.summation(ctf.get_key_c(), ctf.get_key_d(), ctf.get_key_e(), ctf.get_key_b(), ctf.get_key_a()) << endl;

    // after finding out all of the results for the summations, we can check the relativity of it to the condition the pass_check function has by just checking what the conditions values are
    int 
        key_a = ctf.get_key_a(),
        key_b = ctf.get_key_b(),
        key_c = ctf.get_key_c(),
        key_d = ctf.get_key_d(),
        key_e = ctf.get_key_e();
    cout << "Ini hasil pass_check1: " << ((((40*key_c) + (30*key_d) - (10*key_b) + (21*key_a) - (5*key_e))-(7*key_c)-(5*key_d))/(2*key_e)) << endl;
    cout << "Ini hasil pass_check2: " << (((((10*key_a) + (12*key_b) + (15*key_c) + (17*key_d) + (200*key_e) - key_b)/key_d)/key_e)-(key_d-key_b)-((10*key_d) + (16*key_e))) << endl;
    cout << "Ini hasil pass_check3: " << (((1000*key_b) + (5000*key_a) / (200*key_e)) * (0*key_a) + ((200*key_c) -(100*key_a)) / (50*key_d) - key_b) << endl;
    cout << "Ini hasil pass_check4: " << ((18*key_a) + (15*key_b) + (12*key_c) + (9*key_d) + (6*key_e) - (500*key_b) + (50*key_a) +(14*key_c)) << endl;

    /* 
    from this we can see that the pass_check function's conditions are the results of the summation functions
    So now we can just use the pass_check function one by one to get the real end results for the pass_check function
    */

    ctf.pass_check(33);
    cout << endl;
    ctf.pass_check(18); 
    cout << endl;
    ctf.pass_check(9);
    cout << endl;
    ctf.pass_check(17);
    cout << endl;


    return 0;
}