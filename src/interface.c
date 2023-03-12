#include "interface.h"

#include <stdio.h>

#include "menu_interface.h"
#include "game_interface.h"

static SDL_Window *window = NULL;
static SDL_Renderer *renderer = NULL;

static int page = MENU_PAGE;

int interfaceWidth = 500;
int interfaceHeight = 500;

static void CreateWindow();
static void CreateRenderer();

void CreateInterface(){
    CreateWindow();
    CreateRenderer();
}

void CreateWindow(){
    if((window = SDL_CreateWindow("Game Window", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, interfaceWidth, interfaceHeight, SDL_WINDOW_RESIZABLE | SDL_WINDOW_OPENGL)) == NULL){
        fprintf(stderr, "Error (SDL_CreateWindow) : %s\n", SDL_GetError());
        exit(EXIT_FAILURE);
    }
}

void CreateRenderer(){
    if((renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)) == NULL){
        fprintf(stderr, "Error (SDL_CreateRenderer) : %s", SDL_GetError());
        exit(EXIT_FAILURE);
    }
}

void FreeInterface(){
    SDL_DestroyWindow(window);
    SDL_DestroyRenderer(renderer);
}

void TreatEvents(){
    SDL_Event e;
    while(SDL_PollEvent(&e)){
        if(page == MENU_PAGE){
            EventMenuInterface(&e);
        }
        else if(page == GAME_PAGE){
            EventGameInterface(&e);
        }
    }
}

void DrawInterface(){
    if(page == MENU_PAGE){
        DrawMenuInterface(renderer);
    }
    else if(page == GAME_PAGE){
        DrawGameInterface(renderer);
    }
}