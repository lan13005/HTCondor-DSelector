// using ofstream constructors.
#include <iostream>
#include <fstream>

void codeThatDoesNothing(bool useproof = 1, string path = "") 
{

        std::cout << "Doing nothing!" << endl;
        std::ofstream outfile ("test.txt");
        outfile << "Saving doing nothing to txt file!" << std::endl;
        outfile.close();

	return;
}
