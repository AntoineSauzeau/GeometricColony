#pragma once

#include "interface.hpp"

class GameInterface : public Interface {

    public:
        GameInterface();
        ~GameInterface();

        void TreatEvents();
        void Draw();
};