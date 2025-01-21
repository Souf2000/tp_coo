#ifndef SIEGESOCIAL_H
#define SIEGESOCIAL_H

#include <string>

class SiegeSocial {
public:
    SiegeSocial(const std::string &adresse);
    void afficher() const;

private:
    std::string adresse;
};

#endif

