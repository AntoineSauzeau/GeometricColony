#pragma once

#include "interface_manager.h"

#define FPS 30

class Controller{
    public:
        Controller();
        void GameLoop();
    
    private:
        bool exitB = false;
        InterfaceManager *interfaceManager;
};
