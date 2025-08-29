#include <iostream>
#include "sample.hpp"
#include "lcddisplay.hpp"

static void hi(void *arg)
{
 arg;
 std::cout << "Hi\n";
}

static void sayHello()
{
  std::cout << "Hello\n";
}

static void greet()
{
  std::cout << "Greets\n";
  hi((void *)"hi");
  sayHello();
}

void processSample(Sample &sample)
{
  auto value = sample.getId();
  std::cout << "Value = " << value << "\n";
  sample.printSample();
}

void processDisplay(Display &display)
{
  display.showScreen();
}


int main(int argc, char**argv)
{
  Sample sam(32);
  processSample(sam);
  greet();

  LcdDisplay ld;
  processDisplay(ld);

  return 0;
}