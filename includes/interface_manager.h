#pragma once

#include "interface.h"
#include "menu_interface.h"
#include "game_interface.h"

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