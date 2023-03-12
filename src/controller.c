#include "controller.h" 

#include "interface.h"

#include <stdbool.h>
#include <time.h>
#include <math.h>
#include <synchapi.h>
#include <stdio.h>

static bool exitB = false;

void GameLoop(){

    while(!exitB){

        printf("loop\n");

        clock_t tStart = clock();

        TreatEvents();
        DrawInterface();

        clock_t tEnd = clock();
        float iterDuration = (tEnd - tStart) / CLOCKS_PER_SEC;
        if(iterDuration < (1./FPS)){
            Sleep(((1./FPS) - iterDuration) * pow(10, 3));
        }
    }
}