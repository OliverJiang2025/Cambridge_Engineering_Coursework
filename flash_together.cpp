/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"

// Green LED
DigitalOut led1(LED1);
// Blue LED
DigitalOut led2(LED2);
// Red LED
DigitalOut led3(LED3);


void select_led(int l)
{
        if (l==-1) {
                led1 = true;
                led2 = true;
                led3 = true;
        }
        else if (l==0) {
                led1 = false;
                led2 = false;
                led3 = false;
        }
}



int main() {
         int t=0;
         int count = 0;
         while(true) {
                select_led(t);
                wait(0.5);
                t = (t == 0) ? -1 : 0;
                
        }
}
