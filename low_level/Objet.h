#ifndef OBJET_H
#define OBJET_H

#include <string>

class Objet {
public:
    Objet(const std::string &nom, int quantite);
    void afficher() const;

private:
    std::string nom;
    int quantite;
};

#endif

