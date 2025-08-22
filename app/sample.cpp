#include "sample.hpp"
#include <iostream>

Sample::Sample(int id) : id(id)
{

}

int Sample::getId()
{
  return id;
}

void Sample::printSample()
{
  std::cout << "The value of id = " << id << "\n";
}