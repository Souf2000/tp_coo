#ifndef VILLE_H
#define VILLE_H

#include <string>

class Ville {
public:
    Ville(const std::string &nom);
    void afficher() const;

private:
    std::string nom;
};

#endif

