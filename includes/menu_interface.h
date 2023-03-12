#pragma once

#include "SDL2/SDl.h"

#include "interface.h"

class MenuInterface : public Interface {

    public:
        MenuInterface(SDL_Window *window, SDL_Renderer *renderer);
        ~MenuInterface();

        void TreatEvents();
        void Draw();
};