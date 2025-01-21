#include "Ville.h"
#include <iostream>

Ville::Ville(const std::string &nom) : nom(nom) {}

void Ville::afficher() const {
    std::cout << "Nom de la ville: " << nom << std::endl;
}

