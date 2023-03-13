#pragma once

#include "interface.hpp"
#include "menu_interface.hpp"
#include "game_interface.hpp"

class InterfaceManager{

    public:
        InterfaceManager();

        Interface *GetCurrentInterface();

        MenuInterface *menuInterface;
        GameInterface *gameInterface;
        Interface *currentInterface;

        Page page = Page::MENU;

        SDL_Window *window = NULL;
        SDL_Renderer *renderer = NULL;

    private:
        void CreateWindow();
        void CreateRenderer();
};