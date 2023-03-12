#pragma once

#include "SDL2/SDL.h"

#define MENU_PAGE 0
#define GAME_PAGE 1

extern int interfaceWidth;
extern int interfaceHeight;

void CreateInterface();
void FreeInterface();
void TreatEvents();
void DrawInterface();