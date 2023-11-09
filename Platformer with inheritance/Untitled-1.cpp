#include<iostream>
#include <SFML/Graphics.hpp>
using namespace std;
int main() {
	//game set up (you'll need these lines in every game)
    sf::RenderWindow screen(sf::VideoMode(800,800), "breakout"); //set up screen
    sf::Event event; //set up event queue
    sf::Clock clock; //set up the clock (needed for game timing)
    const float FPS = 60.0f; //FPS
    screen.setFramerateLimit(FPS); //set FPS

    //load in images
    sf::Texture brick;
    brick.loadFromFile("brick.png");
    sf::Sprite wall;
    wall.setTexture(brick);

    int map[10][10] = {
        1,1,1,1,1,1,1,1,1,1,
        1,0,0,0,0,0,0,0,0,1,
        1,1,1,1,1,0,1,1,0,1,
        1,0,1,0,0,0,1,0,0,1,
        1,0,0,0,1,1,0,0,1,1,
        1,1,0,0,0,1,0,0,0,1,
        1,0,0,1,0,0,0,1,0,1,
        1,0,1,1,1,0,1,1,0,1,
        1,0,0,0,0,0,0,0,0,1,
        1,1,1,1,1,1,1,1,1,1
    };

    //################### HOLD ONTO YOUR BUTTS, ITS THE GAME LOOP###############################################################
    while (screen.isOpen()) {//keep window open until user shuts it down

        while (screen.pollEvent(event)) { //look for events-----------------------

            //this checks if the user has clicked the little "x" button in the top right corner
            if (event.type == sf::Event::EventType::Closed)
                screen.close();

        }//end event loop---------------------------------------------------------------
                //render section-----------------------------------------
        screen.clear(); //wipes screen, without this things smear
        for (int rows = 0; rows<10; rows++)
            for (int cols = 0; cols < 10; cols++) {
                if (map[rows][cols] == 1) {
                    wall.setPosition(cols*80, rows*80);
                    screen.draw(wall);
                }
            }
        screen.display(); //flips memory drawings onto screen

    }//######################## end game loop ###################################################################################

    cout << "goodbye!" << endl;
} //end of main