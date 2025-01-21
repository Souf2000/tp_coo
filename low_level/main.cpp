#include <iostream>
#include <nlohmann/json.hpp>
#include <cpr/cpr.h>
#include "Ville.h"
#include "Objet.h"
#include "Local.h"
#include "SiegeSocial.h"

void afficher_ville() {
    Ville ville("Toulouse");
    ville.afficher();
}

void afficher_objet() {
    // Simuler un objet JSON
    nlohmann::json json_data = {{"nom", "Chaise"}, {"quantite", 50}};
    Objet objet(json_data["nom"], json_data["quantite"]);
    objet.afficher();
}

void afficher_local() {
    Local local("123 Rue Nationale");
    local.afficher();
}

void afficher_siegesocial() {
    SiegeSocial siege("456 Boulevard de Paris");
    siege.afficher();
}

int main() {
    afficher_ville();
    afficher_objet();
    afficher_local();
    afficher_siegesocial();
    
    // Exemple d'utilisation de CPR pour faire une requête HTTP
    cpr::Response r = cpr::Get(cpr::Url{"http://httpbin.org/get"});
    std::cout << "Status Code: " << r.status_code << std::endl;
    std::cout << "Text: " << r.text << std::endl;

    return 0;
}

