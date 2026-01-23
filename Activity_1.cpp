#include "mbed.h"
#include "vector"
using namespace std;
Serial pc(SERIAL_TX,SERIAL_RX);
// Digital InOut Pins
DigitalIn button(USER_BUTTON);
DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);

void lightUpYellow(){
    led1 = 1;
    led2 = 0;
    led3 = 0;
}
void lightUpBlue(){
    led1 = 0;
    led2 = 1;
    led3 = 0;
}
void lightUpRed(){
    led1 = 0;
    led2 = 0;
    led3 = 1;
}
void closeAll(){
    led1 = 0;
    led2 = 0;
    led3 = 0;
    pc.printf("All light closed\n");
}
// light up one of the leds according to count
void light(int i){
    if ( i % 3 == 0){
            lightUpYellow();
            pc.printf("led1\n");
            wait(1);
        } else if ( i % 3 == 1){
            lightUpBlue();
            wait(1);
            pc.printf("led2\n");
        } else {
            lightUpRed();
            wait(1);
            pc.printf("led3\n");
        }
}
int main() {
    pc.baud(9600);
    pc.printf("Start\n");
    int count = 0;
    int n = 5; // length of sequence
    vector <int> sequence;
    //bool going = true; //true to keep going
    while (sequence.size() < n) {
        light(count);
    
        if (button == 1){
            pc.printf("button clicked!\n");
            sequence.push_back(count);
            
            if (sequence.size() >= n){
                pc.printf("sequence filled!\n");
                closeAll();
                break;
            }   
        }
        count += 1;
    }
    wait(1);
    pc.printf("start replay!\n");
    for (int num : sequence){
        light(num);
    }
    pc.printf("replay ends\n");
    closeAll();
}
