#include "SiegeSocial.h"
#include <iostream>

SiegeSocial::SiegeSocial(const std::string &adresse) : adresse(adresse) {}

void SiegeSocial::afficher() const {
    std::cout << "Adresse du siège social: " << adresse << std::endl;
}

