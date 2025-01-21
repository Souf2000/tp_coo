#ifndef LOCAL_H
#define LOCAL_H

#include <string>

class Local {
public:
    Local(const std::string &adresse);
    void afficher() const;

private:
    std::string adresse;
};

#endif

