#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CANDIDATES 10


// Define a structure to represent candidate data
struct Candidate {
    int number;
    char name[50];
    int age;
    char gender;
    char state[50];
};

struct Data {
    char name[50];
    int votes;
};




void clrscr() {
    printf("\033[2J\033[1;1H");
}


void Result( void ){

    printf("=================================================================================\n");
    printf("                            Welcome to Online Voting System                      \n");
    printf("=================================================================================\n");

    printf("\n\n[ Result ]\n\n");

    // Run Python code
    system("python D:\\.vscode\\OVS\\Getvote.py");

    // Open the file
    FILE *file = fopen("D:\\.vscode\\OVS\\Data.txt", "r");

    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    // Initialize data array
    struct Data candidates[MAX_CANDIDATES];
    int numCandidates = 0;

    // Read data from the file
    char line[100];
    while (fgets(line, sizeof(line), file) != NULL) {
        char name[50];
        int votes;
        // Parse the line to extract candidate name and votes
        if (sscanf(line, "%[^:]: %d votes", name, &votes) == 2) {
            // Add candidate to the array
            strcpy(candidates[numCandidates].name, name);
            candidates[numCandidates].votes = votes;
            numCandidates++;
        }
    }

    // Close the file
    fclose(file);

    // Find the candidate with the highest number of votes
    int maxVotes = 0;
    char winner[50];
    for (int i = 0; i < numCandidates; i++) {
        if (candidates[i].votes > maxVotes) {
            maxVotes = candidates[i].votes;
            strcpy(winner, candidates[i].name);
        }
    }

    // Print the winner
    printf("The candidate with the highest number of votes is: %s with %d Votes\n", winner , maxVotes );

    printf("\n\n--------------------------------------------------------------------------------------\n");
}







// Function to print the home screen
void printHomeScreen() {
    printf("=================================================================================\n");
    printf("                            Welcome to Online Voting System                      \n");
    printf("=================================================================================\n");
    printf("\nChoose an option:\n\n");
    printf("[ 1 ] Candidates Data\n");
    printf("[ 2 ] Vote Data\n");
    printf("[ 3 ] Result\n");
    printf("[ 4 ] Exit\n\n");
    printf("Enter your choice: ");

}



int Vote( void ) {

    printf("=================================================================================\n");
    printf("                            Welcome to Online Voting System                      \n");
    printf("=================================================================================\n");

    printf("\n[ Vote Details ]\n\n");

    // Run Python code
    system("python D:\\.vscode\\OVS\\Getvote.py");

    // Open the file
    FILE *file = fopen("D:\\.vscode\\OVS\\Data.txt", "r");

    // Check if the file opened successfully
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Read and print each character until end of file
    int ch;
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    // Close the file
    fclose(file);

    printf("\n--------------------------------------------------------------------------------------\n");


    return 0 ;
}




// Function to initialize candidate data
void initializeCandidates(struct Candidate candidates[]) {
    // Example data for 6 candidates (compile time initialization)
    struct Candidate exampleData[6] = {
        {1, "VELUCHAMY P ", 57, 'M', "Tamil Nadu"},
        {2, "AISHA GUPTA A ", 40, 'F', "Maharashtra"},
        {3, "ARJUN SHARMA S", 45, 'M', "Himachal Pradesh "},
        {4, "ANANYA SINGH A", 34, 'F', "Bihar"},
        {5, "ADITYA  G", 51, 'M', "Gujarat "},
        {6, "MEERA REDDY M", 55, 'F', "Telangana"}
    };

    // Copy example data to the provided array
    for (int i = 0; i < 6; i++) {
        candidates[i] = exampleData[i];
    }
}

// Function to print candidate data
void printCandidates(struct Candidate candidates[]) {
    printf("=================================================================================\n");
    printf("                            Welcome to Online Voting System                      \n");
    printf("=================================================================================\n");

    printf("\n[ Candidate Data ]\n\n");
    printf("--------------------------------------------------------------------------------------\n");
    printf("Number\tName\t\t\tAge\tGender\tState\n");
    printf("--------------------------------------------------------------------------------------\n");

    // Iterate over each candidate and print their data
    for (int i = 0; i < 6; i++) {
        printf("%d\t%-20s\t%d\t%c\t%s\n", candidates[i].number, candidates[i].name, candidates[i].age, candidates[i].gender, candidates[i].state);
    }

    printf("--------------------------------------------------------------------------------------\n");

}


int main() {
    int choice ;
    char enter[4] ;
    

    // Create an array to store candidate data
    struct Candidate candidates[6];
    // Initialize candidate data
    initializeCandidates(candidates);

    do{
        clrscr();
        // Print the home screen
        printHomeScreen();

        scanf( "%d", &choice ) ;

        if( choice == 1 ) {

            clrscr();
            // Print candidate data
            printCandidates(candidates);
            printf("\n\n[ Enter 'exit' to Continue ] : ") ;
            scanf("%s", enter );
            
        }

        if( choice == 2 ) {

            clrscr();
            //Vote Data
            Vote( );
            printf("\n\n[ Enter 'exit' to Continue ] : ") ;
            scanf("%s", enter );

        }

        if( choice == 3 ) {

            clrscr();
            //Result
            Result();
            printf("\n\n[ Enter 'exit' to Continue ] : ") ;
            scanf("%s", enter );

        }

        

        

    }while( choice != 4 ) ;    



    

    return 0;
}

