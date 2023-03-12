#define SDL_MAIN_HANDLED

#include <stdlib.h>
#include <stdio.h>

#include <SDL2/SDL.h>

#include "interface.h"
#include "controller.h"

int main(int agrc , char *argv[]){

    printf("Starting...");

    if(SDL_Init(SDL_INIT_VIDEO) < 0){
        fprintf(stderr, "Error (SDL_Init) : %s\n", SDL_GetError());
        exit(EXIT_FAILURE);
    }

    CreateInterface();
    GameLoop();

    return EXIT_SUCCESS;
}