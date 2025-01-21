#include "Objet.h"
#include <iostream>

Objet::Objet(const std::string &nom, int quantite) : nom(nom), quantite(quantite) {}

void Objet::afficher() const {
    std::cout << "Nom de l'objet: " << nom << ", Quantité: " << quantite << std::endl;
}

