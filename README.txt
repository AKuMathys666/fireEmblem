Project Fire Emblem.

Bonjour, si vous lisez ce message, c'est que vous souhaitez jouer à notre jeu.
Nous vous en remercions.

Pour pouvoir executer le jeux, il vous faudrat un version de python en 3.6 minimum.
Le logiciel Pygame, si vous ne l'avez pas sur votre poste, veuillez ouvrir un terminal en administrateur
et executer la commande "pip3 install pygame".
Un serveur xampp, si vous en avez pas un, copiez le lien suivant pour acceder a la page des versions disponibles :
https://www.apachefriends.org/fr/download.html
Le logiciel PyMysql, si vous ne l'avez pas sur votre poste, veuillez ouvrir un terminal en administrateur
et executer la commande "pip3 install pymysql"

Lancer via le panneau de control Xampp Apache et Mysql.
Il se peut que vous ayez un probleme lors de l'execution du serveur Apache.
Si c'est le cas, cliquez sur le bouton "configure" et modifiez le champ "Listen" en mettent le port 8080 par exemple.
Si cette fois le serveur Apache se lance, ouvrez un navigateur, entrez dans l'url "localhost:port" (le champ port
correspond au numéro du port mis dans dans le champ "Listen" dans le fichier de configuration modifie precedemment.
Une fois que vous avez accès a la page, cliquez en haut a droite sur l'onglet "phpMyadmin".
Cliquez sur l'onglet "Importer" et importez le fichier "fire_emblem_db.sql" fournit.

Vous pouvez maintenant executer avec pygame le fichier "combat.py"



							ENJOY !!!



             ,,########################################,,
          .*##############################################*
        ,*####*:::*########***::::::::**######:::*###########,
      .*####:    *#####*.                 :*###,.#######*,####*.
     *####:    *#####*                      .###########*  ,####*
  .*####:    ,#######,                        ##########*    :####*
  *####.    :#########*,                       ,,,,,,,,.      ,####:
    ####*  ,##############****************:,,               .####*
     :####*#####################################**,        *####.
       *############################################*,   :####:
        .#############################################*,####*
          :#####:*****#####################################.
            *####:                  .,,,:*****###########,
             .*####,                            *######*
               .####* :*#######*               ,#####*
                 *###############*,,,,,,,,::**######,
                   *##############################:
                     *####*****##########**#####*
                      .####*.            :####*
                        :####*         .#####,
                          *####:      *####:
                           .*####,  *####*
                             :####*####*
                               *######,
                                 *##,

            ___     -._
            `-. """--._ `-.
               `.      "-. `.
 _____           `.       `. \       G O K U 
`-.   """---.._    \        `.\
   `-.         "-.  \         `\
      `.          `-.\          \_.-""""""""--._
        `.           `                          "-.
          `.                                       `.    __....-------...
--..._      \                                       `--"""""""""""---..._
__...._"_-.. \                       _,                             _..-""
`-.      """--`           /       ,-'/|     ,                   _.-"
   `-.                 , /|     ,'  / |   ,'|    ,|        _..-"
      `.              /|| |    /   / |  ,'  |  ,' /        ----"""""""""_`-
        `.            ( \  \      |  | /   | ,'  //                 _.-"
          `.        .'-\/'""\ |  '  | /  .-/'"`\' //            _.-"
    /'`.____`-.  ,'"\  ''''?-.V`.   |/ .'..-P''''  /"`.     _.-"
   '(   `.-._""  ||(?|    /'   >.\  ' /.<   `\    |P)||_..-"___.....---
     `.   `. "-._ \ ('   |     `8      8'     |   `) /"""""    _".""
       `.   `.   `.`.b|   `.__            __.'   |d.'  __...--""
         `.   `.   ".`-  .---      ,-.     ---.  -'.-""
           `.   `.   ""|      -._      _.-      |""
             `.  .-"`.  `.       `""""'       ,'
               `/     `.. ""--..__    __..--""
                `.      /7.--|    """"    |--.__
                  ..--"| (  /'            `\  ` ""--..
               .-"      \\  |""--.    .--""|          "-.
              <.         \\  `.    -.    ,'       ,'     >
             (P'`.        `%,  `.      ,'        /,' .-"'?)
             P    `. \      `%,  `.  ,'         /' .'     \
            | --"  _\||       `%,  `'          /.-'   .    )
            |       `-.""--..   `%..--"""\\"--.'       "-  |
            \          `.  .--"""  "\.\.\ \\.'       )     |