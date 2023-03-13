#pragma once

#include "SDL2/SDL.h"

#include "interface.hpp"

class MenuInterface : public Interface {

    public:
        MenuInterface(SDL_Window *window, SDL_Renderer *renderer);
        ~MenuInterface();

        void TreatEvents();
        void Draw();
};