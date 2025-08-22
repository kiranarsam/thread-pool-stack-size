#include <iostream>
#include "sample.hpp"

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


int main(int argc, char**argv)
{
  Sample sam(32);
  processSample(sam);
  greet();

  return 0;
}