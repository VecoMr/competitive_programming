#include <iostream>
#include <cstdint>

int main()
{
    int nb_branche = 0;
    int hauteur_courante = 0;
    int max_hauteur = 0;
    int reponse = 0;
    int max_saut = 0;
    int valeur_courante = 0;

    std::cin >> nb_branche;
    for (; nb_branche > 0; nb_branche--) {
        std::cin >> valeur_courante;
        if (valeur_courante > max_saut) {
            max_saut = valeur_courante;
        }
        hauteur_courante += valeur_courante;
        if (hauteur_courante > max_hauteur) {
            max_hauteur = hauteur_courante;
            reponse = max_saut;
        }
    }
    std::cout << reponse << std::endl;
    return 0;
}
