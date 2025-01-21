#include "Local.h"
#include <iostream>

Local::Local(const std::string &adresse) : adresse(adresse) {}

void Local::afficher() const {
    std::cout << "Adresse du local: " << adresse << std::endl;
}

