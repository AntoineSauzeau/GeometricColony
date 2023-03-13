#include "interface_manager.hpp"

#include <iostream>

InterfaceManager::InterfaceManager(){
    CreateWindow();
    CreateRenderer();

    menuInterface = new MenuInterface(window, renderer);
    currentInterface = menuInterface;
}

void InterfaceManager::CreateWindow(){
    if((window = SDL_CreateWindow("Fenetre", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 500, 500, 0)) == NULL){
        std::cerr << "Error (SDL_CreateWindow) : " << SDL_GetError() << std::endl;
        exit(EXIT_FAILURE);
    }
}


void InterfaceManager::CreateRenderer(){
    if((renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)) == NULL){
        std::cerr << "Error (SDL_CreateRenderer) : " << SDL_GetError() << std::endl;
        exit(EXIT_FAILURE);
    }
}

Interface *InterfaceManager::GetCurrentInterface(){
    return currentInterface;
}