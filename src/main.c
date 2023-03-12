#define SDL_MAIN_HANDLED

#include <stdlib.h>
#include <iostream>

#include <SDL2/SDL.h>

#include "interface.h"
#include "controller.h"

int main(int agrc , char *argv[]){

    std::cout << "Starting..." << std::endl;

    if(SDL_Init(SDL_INIT_VIDEO) < 0){
       std::cerr << "Error (SDL_Init) : " << SDL_GetError() << std::endl;
        exit(EXIT_FAILURE);
    }

    Controller controller;
    controller.GameLoop();

    return EXIT_SUCCESS;
}