#pragma once
#include "display.hpp"

class LcdDisplay: public Display
{
  public:
    LcdDisplay();
    void showScreen() override;
};