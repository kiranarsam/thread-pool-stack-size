#pragma once

class Sample
{
  private:
    int id;
  public:
    explicit Sample(int id);
    int getId();
    void printSample();
};