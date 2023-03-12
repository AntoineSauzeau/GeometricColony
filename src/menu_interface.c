#include "menu_interface.h"

#include "colors.h"
#include "interface.h"

void EventMenuInterface(SDL_Event *e){

    if(e->type == SDL_QUIT){
        exit(EXIT_SUCCESS);
    }
}

void DrawMenuInterface(SDL_Renderer *renderer){

    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
    SDL_RenderClear(renderer);

    

    SDL_RenderPresent(renderer);
}