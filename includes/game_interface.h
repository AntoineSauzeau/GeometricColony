#pragma once

#include "interface.h"

class GameInterface : public Interface {

    public:
        GameInterface();
        ~GameInterface();

        void TreatEvents();
        void Draw();
};