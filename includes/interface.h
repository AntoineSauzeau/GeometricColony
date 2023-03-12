#pragma once

#include "SDL2/SDL.h"

#define MENU_PAGE 0
#define GAME_PAGE 1

enum class Page {MENU, GAME};

class Interface {

    public:
        Interface();
        virtual ~Interface();

        virtual void TreatEvents() = 0;
        virtual void Draw() = 0;

    protected:
        int interfaceWidth;
        int interfaceHeight;

        SDL_Window *window = NULL;
        SDL_Renderer *renderer = NULL;
};
