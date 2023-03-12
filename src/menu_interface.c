#include "menu_interface.h"

MenuInterface::MenuInterface(SDL_Window *window, SDL_Renderer *renderer){
    this->window = window;
    this->renderer = renderer;
}

MenuInterface::~MenuInterface(){
    
}

void MenuInterface::TreatEvents(){

    SDL_Event e;
    while(SDL_PollEvent(&e)){
        if(e.type == SDL_QUIT){
            exit(EXIT_SUCCESS);
        }
    }
}

void MenuInterface::Draw(){

    SDL_SetRenderDrawColor(renderer, 50, 150, 200, 255);
    SDL_RenderClear(renderer);

    SDL_RenderPresent(renderer);
}